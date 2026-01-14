## Gmail to Google Sheets Automation

## Project Overview

This project is a Python automation system that reads unread emails from a Gmail inbox and logs them into a Google Sheet automatically.

The system uses:

- Gmail API to read emails

- Google Sheets API to store data

- OAuth 2.0 authentication for secure access

Each qualifying email is added as a new row in Google Sheets with the following details:

- From – Sender email address

- Subject – Email subject

- Date – Date and time received

- Content – Email body (plain text)

## High-Level Architecture / Flow

Gmail Inbox (Unread Emails)
↓
OAuth 2.0 Authentication
↓
Python Script
↓
Email Parsing
↓
Google Sheets (Rows Added)

## Technologies Used

- Python 3

- Google Gmail API

- Google Sheets API

- OAuth 2.0

- Google API Python Client

## OAuth 2.0 Authentication Flow

The application uses OAuth 2.0 (Desktop App) authentication.

- On the first run, the browser opens and the user grants permission.

- Google generates an access token (token.json) which is reused for subsequent runs.

- The app runs in testing mode, so a “Google hasn’t verified this app” warning appears (expected behavior).

## Security Note:

credentials.json and token.json are never committed to GitHub and are excluded using .gitignore.

## Project Structure

gmail-to-sheets/
│
├── src/
│ ├── gmail_service.py # Gmail OAuth & API connection
│ ├── sheets_service.py # Google Sheets API helper
│ ├── email_parser.py # Extracts plain-text email body
│ └── main.py # Main workflow controller
│
├── credentials/
│ └── credentials.json # OAuth credentials
│
├── proof/
│ ├── terminal_proof.png
│ ├── google_sheet_proof.png
│ ├── oauth_warning.png
│ └── git_status.png
│
├── state.json # Stores processed email IDs
├── .gitignore
├── requirements.txt
└── README.md

## Duplicate Prevention & State Management

To prevent duplicate rows:

- The script stores processed Gmail message IDs in a local file called state.json.

- On each run, the script checks this state file and skips emails that were already processed.

- Emails are also marked as read after processing.

## Why this approach?

- Ensures idempotent execution

- Prevents duplicate entries even if the script is run multiple times

- Simple and reliable for local automation

## Setup Instructions

1️. Clone the Repository
git clone https://github.com/likhithatalatam/gmail-to-sheets.git
cd gmail-to-sheets

2️. Install Dependencies
pip install -r requirements.txt

3️. Add OAuth Credentials

Place credentials.json inside the credentials/ folder

Do NOT commit this file

4️. Run the Script
python src/main.py

## Proof of Execution

Screenshots are provided in the proof/ folder:

- Gmail OAuth consent screen

- Terminal output showing successful execution

- Google Sheet populated with real email data

- Git status confirming secrets are not committed

## Challenges Faced & Solutions

Challenge:

OAuth scope errors occurred when adding new permissions.

Solution:

- Deleted existing token.json

- Re-authenticated with updated scopes

This ensured correct access for both Gmail and Sheets APIs

## Limitations

- Some emails are HTML-only, so plain-text content may be empty.

- Attachments are not processed.

- Designed for single-user automation, not multi-user deployment.

## Author

Likhitha Talatam

## Final Notes

- The script processes only unread emails

- No duplicate rows are created

- Secure handling of credentials is ensured

- Fully compliant with assignment requirements
