from googleapiclient.discovery import build


def get_sheets_service(creds):
    service = build("sheets", "v4", credentials=creds)
    return service


def append_row(service, spreadsheet_id, values):
    body = {"values": [values]}

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="Sheet1!A:D",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body,
    ).execute()
