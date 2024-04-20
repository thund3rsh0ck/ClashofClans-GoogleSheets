# Clash of Clans Google Sheets Integration

Connect Clash of Clans API to Google Sheets for War Stats and Member Roster.

## Features
- Classic War Tracker
- Member Roster Tracker

## Setup Instructions

### Step 1: Set Up Google Sheets API

1. Create a Project on Google Developers Console:
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project.
   
2. Enable the Google Sheets API:
   - In your project dashboard, navigate to Library, search for "Google Sheets API", and enable it.
   
3. Create Credentials:
   - In the APIs & Services > Credentials, click Create Credentials and choose Service account.
   - Fill out the necessary details. After creating the service account, click on it.
   - Go to the Keys tab, click on Add Key, and select Create new key. Choose JSON as the key type and download the JSON file. This file contains your credentials.
   - Save that file as `clash.json`.
   
4. Share your Sheet:
   - Open your Google Sheets document.
   - Click on the Share button and share it with the `client_email` found in your JSON credentials file, with at least "Editor" permissions.

### Step 2: Install Dependencies

Install the necessary Python libraries if you haven't already:
```pip install gspread oauth2client requests```

### Step 3: Configuration

Finally, change anything between `[ ]` in the Python files to your own.

For the Google sheet, create the following tabs:
Botdata with the following columns:
```Date	Type	User	Attacked?```

Rosterv2 with the following column headers:
```Name	Rank	Tag	Donations	Donations Received	Rank in Clan	League```


