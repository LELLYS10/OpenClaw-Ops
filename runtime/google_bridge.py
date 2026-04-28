#!/usr/bin/env python3
import json
import sys
import urllib.parse
import urllib.request
import urllib.error
import datetime as dt
import re
import unicodedata

TOKEN_FILE = "/data/.google-auth/token.json"
TIMEOUT = 25
SHEETS_MIME = "application/vnd.google-apps.spreadsheet"


def load_token():
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_token(data):
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def refresh_if_needed(data):
    expiry = data.get("expiry", "")
    try:
        exp = dt.datetime.fromisoformat(expiry.replace("Z", "+00:00"))
    except Exception:
        exp = dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=1)
    if exp > dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=5):
        return data
    payload = urllib.parse.urlencode(
        {
            "client_id": data["client_id"],
            "client_secret": data["client_secret"],
            "refresh_token": data["refresh_token"],
            "grant_type": "refresh_token",
        }
    ).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="ignore")
        if "invalid_grant" in detail:
            print("ERRO_GOOGLE_TOKEN_REVOGADO")
            sys.exit(2)
        raise
    data["token"] = body["access_token"]
    data["expiry"] = (
        dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=int(body.get("expires_in", 3600)))
    ).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    save_token(data)
    return data


def api_get(url, params=None):
    data = refresh_if_needed(load_token())
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {data['token']}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode())


def gmail_unread():
    data = api_get(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages",
        {"q": "is:unread", "maxResults": 10},
    )
    msgs = data.get("messages", [])
    if not msgs:
        print("Nenhum email não lido.")
        return
    print(f"EMAILS_NAO_LIDOS: {len(msgs)}")
    for msg in msgs:
        meta = api_get(
            f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{msg['id']}",
            {"format": "metadata", "metadataHeaders": ["From", "Subject", "Date"]},
        )
        headers = {h["name"]: h["value"] for h in meta.get("payload", {}).get("headers", [])}
        print("---")
        print("id:", msg["id"])
        print("from:", headers.get("From", "?"))
        print("subject:", headers.get("Subject", "(sem assunto)"))
        print("date:", headers.get("Date", "?"))


def drive_recent():
    data = api_get(
        "https://www.googleapis.com/drive/v3/files",
        {
            "pageSize": 10,
            "fields": "files(id,name,mimeType,modifiedTime,webViewLink)",
            "orderBy": "modifiedTime desc",
            "q": "trashed = false",
        },
    )
    files = data.get("files", [])
    if not files:
        print("Nenhum arquivo recente no Drive.")
        return
    print(f"DRIVE_RECENTES: {len(files)}")
    for item in files:
        print("---")
        print("id:", item.get("id"))
        print("name:", item.get("name"))
        print("type:", item.get("mimeType"))
        print("modified:", item.get("modifiedTime"))
        print("link:", item.get("webViewLink"))


def list_sheets_files(limit=20):
    data = api_get(
        "https://www.googleapis.com/drive/v3/files",
        {
            "pageSize": limit,
            "fields": "files(id,name,mimeType,modifiedTime,webViewLink)",
            "orderBy": "modifiedTime desc",
            "q": f"trashed = false and mimeType = '{SHEETS_MIME}'",
        },
    )
    return data.get("files", [])


def sheets_list():
    files = list_sheets_files(limit=20)
    if not files:
        print("Nenhuma planilha encontrada.")
        return
    print(f"PLANILHAS: {len(files)}")
    for item in files:
        print("---")
        print("id:", item.get("id"))
        print("name:", item.get("name"))
        print("modified:", item.get("modifiedTime"))
        print("link:", item.get("webViewLink"))


def calendar_today():
    now = dt.datetime.now(dt.timezone.utc)
    start = now.astimezone().replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + dt.timedelta(days=1)
    data = api_get(
        "https://www.googleapis.com/calendar/v3/calendars/primary/events",
        {
            "timeMin": start.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
            "timeMax": end.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
            "singleEvents": "true",
            "orderBy": "startTime",
            "maxResults": 15,
        },
    )
    items = data.get("items", [])
    if not items:
        print("Nenhum evento hoje.")
        return
    print(f"AGENDA_HOJE: {len(items)}")
    for item in items:
        start_val = item.get("start", {}).get("dateTime") or item.get("start", {}).get("date")
        print("---")
        print("summary:", item.get("summary", "(sem título)"))
        print("start:", start_val)
        print("status:", item.get("status"))


def norm(text):
    base = unicodedata.normalize("NFKD", (text or "").strip().lower())
    ascii_text = "".join(ch for ch in base if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", ascii_text)


def find_sheet_file(name_or_id):
    if re.fullmatch(r"[A-Za-z0-9_-]{20,}", name_or_id or ""):
        meta = api_get(
            f"https://www.googleapis.com/drive/v3/files/{name_or_id}",
            {"fields": "id,name,mimeType,webViewLink"},
        )
        if meta.get("mimeType") != SHEETS_MIME:
            raise SystemExit("ERRO_PLANILHA_ID_INVALIDO")
        return meta
    target = norm(name_or_id)
    files = list_sheets_files(limit=100)
    exact = [item for item in files if norm(item.get("name")) == target]
    if exact:
        return exact[0]
    partial = [item for item in files if target and target in norm(item.get("name"))]
    if partial:
        return partial[0]
    raise SystemExit("ERRO_PLANILHA_NAO_ENCONTRADA")


def get_sheet_metadata(spreadsheet_id):
    return api_get(
        f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}",
        {"fields": "properties.title,sheets.properties(sheetId,title,hidden,index)"},
    )


def get_values(spreadsheet_id, sheet_name, cell_range):
    encoded_range = urllib.parse.quote(f"{sheet_name}!{cell_range}", safe="!:'")
    data = api_get(
        f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{encoded_range}",
        {"majorDimension": "ROWS"},
    )
    return data.get("values", [])


def candidate_sheet_names(meta):
    props = [s.get("properties", {}) for s in meta.get("sheets", [])]
    visible = sorted([p for p in props if not p.get("hidden")], key=lambda p: p.get("index", 9999))
    hidden = sorted([p for p in props if p.get("hidden")], key=lambda p: p.get("index", 9999), reverse=True)
    names = [p["title"] for p in visible]
    for item in hidden:
        if item["title"] not in names:
            names.append(item["title"])
    return names


def detect_header(values):
    for idx, row in enumerate(values):
        row_norm = [norm(cell) for cell in row]
        has_name = any(cell in {"nome", "cliente"} for cell in row_norm)
        has_status = any(cell in {"situacao", "status"} for cell in row_norm)
        has_due = any(cell.startswith("dtvenc") or cell.startswith("datavenc") or cell == "venc" for cell in row_norm)
        if has_name and has_status and has_due:
            return idx, row_norm
    return None, None


def row_to_map(header, row):
    data = {}
    for idx, key in enumerate(header):
        value = row[idx] if idx < len(row) else ""
        data[key] = value.strip() if isinstance(value, str) else value
    return data


def first_key(header, options):
    for option in options:
        for key in header:
            if key == option or key.startswith(option):
                return key
    return None


def pick_interest_column(header):
    for options in (["12", "12%"], ["juros"], ["9", "9%"], ["jean"]):
        key = first_key(header, options)
        if key:
            return key
    return None


def extract_overdue_from_sheet(spreadsheet_id, sheet_name):
    values = get_values(spreadsheet_id, sheet_name, "A1:Z500")
    if not values:
        return None
    header_idx, header = detect_header(values)
    if header is None:
        return None
    status_key = first_key(header, ["situacao", "status"])
    due_key = first_key(header, ["dtvenc", "datavenc", "venc"])
    name_key = first_key(header, ["nome", "cliente"])
    interest_key = pick_interest_column(header)
    if not all([status_key, due_key, name_key, interest_key]):
        return None
    rows = []
    for raw_row in values[header_idx + 1 :]:
        mapped = row_to_map(header, raw_row)
        status = norm(str(mapped.get(status_key, "")))
        if status not in {"vencido", "atrasado"}:
            continue
        rows.append(
            {
                "juros": str(mapped.get(interest_key, "")).strip(),
                "nome": str(mapped.get(name_key, "")).strip(),
                "data": str(mapped.get(due_key, "")).strip(),
            }
        )
    return {"sheet_name": sheet_name, "interest_key": interest_key, "rows": rows}


def sheet_overdue(name_or_id):
    sheet_file = find_sheet_file(name_or_id)
    meta = get_sheet_metadata(sheet_file["id"])
    for sheet_name in candidate_sheet_names(meta):
        result = extract_overdue_from_sheet(sheet_file["id"], sheet_name)
        if result is None:
            continue
        print(f"PLANILHA_VENCIDOS: {len(result['rows'])}")
        print(f"planilha: {sheet_file.get('name')}")
        print(f"aba: {result['sheet_name']}")
        print(f"juros_coluna: {result['interest_key']}")
        for item in result["rows"]:
            print("---")
            print("JUROS:", item["juros"])
            print("NOME:", item["nome"])
            print("DATA:", item["data"])
        return
    raise SystemExit("ERRO_CABECALHO_NAO_ENCONTRADO")


def usage():
    print("uso: google_bridge.py gmail-unread | drive-recent | sheets-list | calendar-today | sheet-overdue <nome-ou-id>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "gmail-unread":
        gmail_unread()
    elif cmd == "drive-recent":
        drive_recent()
    elif cmd == "sheets-list":
        sheets_list()
    elif cmd == "calendar-today":
        calendar_today()
    elif cmd == "sheet-overdue":
        if len(sys.argv) != 3:
            usage()
            sys.exit(1)
        sheet_overdue(sys.argv[2])
    else:
        usage()
        sys.exit(1)
