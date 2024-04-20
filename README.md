# ClashofClans-GoogleSheets
Connecting Clash of Clans API to Sheets for War Stats and Member Roster

# Setup Instructions
Step 1: Set Up Google Sheets API

Create a Project on Google Developers Console:

Go to the Google Developers Console.

Create a new project.

Enable the Google Sheets API:

In your project dashboard, navigate to Library, search for "Google Sheets API", and enable it.

Create Credentials:

In the APIs & Services > Credentials, click Create Credentials and choose Service account.

Fill out the necessary details. After creating the service account, click on it.

Go to the Keys tab, click on Add Key, and select Create new key. Choose JSON as the key type and download the JSON file. This file contains your credentials.

Share your Sheet:

Open your Google Sheets document.

Click on the Share button and share it with the client_email found in your JSON credentials file, with at least "Editor" permissions.

Step 2: Install gspread and oauth2client

Install the necessary Python libraries if you haven't already:

'''pip install gspread oauth2client requests'''
