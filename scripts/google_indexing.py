import argparse
import json
import os
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

def get_access_token(service_account_file):
    scopes = ["https://www.googleapis.com/auth/indexing"]
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes
    )
    credentials.refresh(Request())
    return credentials.token

def notify_google(url, action, token):
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    body = json.dumps({
        "url": url,
        "type": action # URL_UPDATED or URL_DELETED
    })
    
    response = requests.post(endpoint, data=body, headers=headers)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Google Indexing API Messenger")
    parser.add_argument("--url", required=True, help="URL to index/update")
    parser.add_argument("--action", default="URL_UPDATED", choices=["URL_UPDATED", "URL_DELETED"])
    args = parser.parse_args()

    config_path = os.path.expanduser("~/.config/gemini-seo/google-apis.json")
    
    if not os.path.exists(config_path):
        print(f"❌ Error: Google Service Account key not found at {config_path}")
        return

    print(f"⚡ Requesting instant re-crawl for: {args.url}")
    
    try:
        token = get_access_token(config_path)
        result = notify_google(args.url, args.action, token)
        
        if "urlNotificationMetadata" in result:
            print(f"✅ Success! Google received the notification for {args.url}")
            print(f"Notification ID: {result['urlNotificationMetadata']['latestUpdate']['notifyTime']}")
        else:
            print(f"❌ API Error: {json.dumps(result, indent=2)}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()