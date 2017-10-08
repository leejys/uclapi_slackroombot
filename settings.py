import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

#dotenv_path = join(dirname(__file__), '.env')
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


UCL_API_TOKEN=os.environ.get("UCL_API_TOKEN")
OAUTH_TOKEN=os.environ.get("OAUTH_TOKEN")
OAUTH_TOKEN_2=os.environ.get("OAUTH_TOKEN_2")
CLIENT_SECRET=os.environ.get("CLIENT_SECRET")
CLIENT_SECRET_2=os.environ.get("CLIENT_SECRET_2")
SLACK_BOT_TOKEN=os.environ.get("SLACK_BOT_TOKEN")
BOT_ID=os.environ.get("BOT_ID")

