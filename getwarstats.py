import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
from dateutil import parser


def update_war_stats():
    # Define the scope
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('clash.json', scope)

    # Authorize the clientsheet
    client = gspread.authorize(creds)

    # Sheets setup
    sheet = client.open_by_url("[INSERT SPREADSHEET URL HERE]")

    worksheet = sheet.worksheet('[INSERT TAB NAME]')

    # CoC API Setup
    url = "https://api.clashofclans.com/v1/clans/[CLAN TAG WITH URL ENCODING]/currentwar"
    headers = {
        'Authorization': 'Bearer [API_KEY]'  # Replace '[API_KEY]' with your actual API key
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        #records = worksheet.get_all_records()
        #print(records)
        updates = []
        start_time = data['startTime']  # Get the start time
        formatted_time = parser.parse(start_time).strftime('%m/%d/%Y')
        for member in data['clan']['members']:
            user = member['name']
            wartype = "Classic War"
            attacked = "Y" if member.get('attacks') else "N"  # Check if 'attacks' list exists and is not empty

            # Append the extracted data to our list
            updates.append([formatted_time, wartype, user, attacked])

        # Writing to Google Sheets
        for update in updates:
            worksheet.append_row(update)  # Append each row to the sheet

        print("Data updated successfully.")
        pass
    except gspread.exceptions.SpreadsheetNotFound:
        print("d.")
    except Exception as e:
        print("An error occurred:", e)


update_war_stats()
