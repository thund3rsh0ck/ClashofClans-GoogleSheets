import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
from dateutil import parser

# Define the scope
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('clash.json', scope)

# Authorize the clientsheet
client = gspread.authorize(creds)

# Sheets setup
sheet = client.open_by_url("[GOOGLE SHEETS URL]")

worksheet = sheet.worksheet('[TAB NAME]')

# CoC API Setup
url = "https://api.clashofclans.com/v1/clans/[CLAN TAG URL ENCODED]/members"
headers = {
    'Authorization': 'Bearer [API KEY]'  # Replace 'API_KEY' with your actual API key
}

try:
    response = requests.get(url, headers=headers)
    data = response.json()
    #records = worksheet.get_all_records()
    #print(records)
    updates = []
    for item in data['items']:
        name = item['name']
        role = item['role']
        tag = item['tag']
        donations = item['donations']
        donationsrec = item['donationsReceived']
        rank = item['clanRank']
        league = item['league']['name']

        # Append the extracted data to our list
        updates.append([name, role, tag, donations, donationsrec, rank, league])
    # Writing to Google Sheets
    values = worksheet.get_all_values()
        # Clear all rows starting from the second row
    if len(values) > 1:
        worksheet.delete_rows(2, len(values))
        print(f"All rows (from row 2) in Rosterv2 tab cleared successfully.")
    else:
        print("No rows to clear.")
    for update in updates:
        worksheet.append_row(update)  # Append each row to the sheet
    print("Data updated successfully.")
    pass
except gspread.exceptions.SpreadsheetNotFound:
    print("d.")
except Exception as e:
    print("An error occurred:", e)
