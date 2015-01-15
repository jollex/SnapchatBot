# SnapchatBot
A snapchat bot that uploads all incoming pictures to its story

## Requirements
This script needs two python libraries to run: [requests](http://docs.python-requests.org/en/latest/) and [pycrypto](https://pypi.python.org/pypi/pycrypto).

## Usage
1. Either change 'secrets.USERNAME' and 'secrets.PASSWORD' in main.py to the username and password for the snapchat account you want to automate, or create a secrets.py file with two variables USERNAME and PASSWORD set to the username and password respectively.
2. Simply run main.py to add all incoming friend requests and upload all incoming snaps to the account's story.
3. If you want, set a cron job to run the script every minute or however long you want.
4. That's it!

## Acknowledgements
I used a python wrapper for the Snapchat API which can be found [here](https://github.com/martinp/pysnap). Small modifications were made to pysnap.py to allow for posting to the story.
