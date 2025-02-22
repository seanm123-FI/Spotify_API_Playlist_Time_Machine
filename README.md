# Time Machine - Billboard to Spotify

This app allows users to create a Spotify playlist from the Billboard Hot 100 for a specific date.
The app scrapes the Billboard Hot 100 chart for the top 100 songs and creates a playlist on Spotify with those songs.

**Features**

Scrapes the Billboard Hot 100 chart for a specified date.
Creates a Spotify playlist with the top 100 songs from that date.
Requires a Spotify account and API credentials for authentication.
Prerequisites
Before using this app, you need:

A Spotify Developer account to create a client ID and secret.

Python 3.8+ installed.

The following Python libraries:

**requests**

**spotipy**

**beautifulsoup4**

**pprint**

You can install these libraries using pip:
_pip install requests spotipy beautifulsoup4 pprint_

# Steps to Set Up and Use the App

**1. Create a Spotify Developer App**

To access Spotify's API, you will need to create a Spotify Developer App and get your **Client ID** and **Client Secret**.

**Steps:**

Go to the Spotify Developer Dashboard.

Log in with your Spotify account.

Click Create an App.

Fill in the app details (e.g., App name: Time Machine - Billboard to Spotify, App description: Scrapes Billboard Hot 100 and creates Spotify playlist).

After creating the app, you will see your Client ID and Client Secret. These will be required in the next steps.

**2. Set Up Your Credentials in the Script**

Once you've got your **Client ID** and **Client Secret**, you need to fill them in the script.

Open the script (main.py).

Replace the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET with the credentials you received in the previous step.

SPOTIPY_CLIENT_ID = ''     
**Replace '' with your Spotify Client ID**

SPOTIPY_CLIENT_SECRET = ''        
**Replace '' with your Spotify Client Secret**


**3. Run the Script**

Clone or download the repository.

In the terminal or command prompt, navigate to the project directory.

Run the Python script:
python main.py

**5. Follow the Prompts**

You will be prompted to input a date in the format YYYY-MM-DD. For example: 2024-01-01.

The script will scrape the Billboard Hot 100 for that date, and create a Spotify playlist with the top songs.

**6. Access Your Playlist**

After the script successfully creates the playlist, you will be provided with a link to access the playlist on Spotify.

Example Output

Once you input a date, you will see the top 100 songs from that date printed to the console, and the app will create a playlist for you on Spotify.

Example:

Enter the date (YYYY-MM-DD): 2024-01-01

Created playlist 'Top 100 Songs of 2024-01-01' successfully!

**Troubleshooting**

HTTP Error: Insufficient client scope (403)

This error usually occurs if the Spotify API client is not authorized properly. Double-check the credentials and scope permissions in the Spotify Developer Dashboard.

Song Not Found on Spotify

Some songs might not be available on Spotify. The script uses exception handling to skip these songs, so no need to worry if a song is not added to the playlist.

**License**

This project is licensed under the MIT License - see the LICENSE file for details
