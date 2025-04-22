import pandas as pd

def load_to_csv(df, filename='film.csv'):
    """
    Simpan DataFrame ke file CSV tanpa index.
    """
    df.to_csv(filename, index=False)
    print(f"Data successfully saved to {filename}")

# (Optional) load to Google Sheets - requires google-sheets-api.json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def load_to_sheets(df, spreadsheet_id, creds_file='google-sheets-api.json'):
    """
    Simpan DataFrame ke Google Sheets (range A1).  
    spreadsheet_id: ID pada URL Google Sheets.
    """
    creds = service_account.Credentials.from_service_account_file(creds_file)
    service = build('sheets', 'v4', credentials=creds)
    values = [df.columns.tolist()] + df.astype(str).values.tolist()
    body = {'values': values}
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='A1',
        valueInputOption='RAW',
        body=body
    ).execute()
    print(f"Data successfully written to Google Sheets: {spreadsheet_id}")