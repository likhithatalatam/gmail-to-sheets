from gmail_service import get_gmail_service
from email_parser import get_plain_text_body
from sheets_service import get_sheets_service, append_row

SPREADSHEET_ID = "1m0uVpZZmEGuLGn5Xhce7qoHXGb38uCAx3itYIm_To_Q"


def fetch_unread_emails(service, sheets_service):
    results = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX", "UNREAD"], maxResults=5)
        .execute()
    )

    messages = results.get("messages", [])

    if not messages:
        print("No unread emails found.")
        return

    print(f"Found {len(messages)} unread emails:\n")

    for msg in messages:
        msg_id = msg["id"]

        message = (
            service.users()
            .messages()
            .get(userId="me", id=msg_id, format="full")
            .execute()
        )

        headers = message["payload"]["headers"]
        data = {h["name"]: h["value"] for h in headers}

        sender = data.get("From", "")
        subject = data.get("Subject", "")
        date = data.get("Date", "")
        body = get_plain_text_body(message)

        # Append to Google Sheet
        append_row(sheets_service, SPREADSHEET_ID, [sender, subject, date, body])

        # Mark as read
        service.users().messages().modify(
            userId="me", id=msg_id, body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        print("Added email to Google Sheet:", subject)


gmail_service = get_gmail_service()
sheets_service = get_sheets_service(gmail_service._http.credentials)

fetch_unread_emails(gmail_service, sheets_service)
