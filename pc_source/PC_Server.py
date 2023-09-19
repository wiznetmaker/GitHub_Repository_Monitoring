import requests
import time

# GitHub Personal Access Token
TOKEN = "Your Tokens"

# GitHub API URL for searching repositories
SEARCH_API_URL = "https://api.github.com/search/repositories"

def fetch_recent_w5500_repo():
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'My-App'
    }

    params = {
        'q': 'W5500',
        'sort': 'updated',
        'order': 'desc'
    }

    response = requests.get(SEARCH_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('items'):
            return data['items'][0]
    else:
        print(f"Error: {response.content}")
        return None

def main():
    prev_repo = None

    while True:
        recent_repo = fetch_recent_w5500_repo()
        if recent_repo is None:
            print("Could not fetch data. Retrying in 60 seconds.")
            time.sleep(60)
            continue

        if prev_repo is None:
            prev_repo = recent_repo
            print(f"Initial repo is {prev_repo['full_name']}. Monitoring for updates.")
        elif prev_repo['updated_at'] != recent_repo['updated_at']:
            print(f"New update found. Previous: {prev_repo['full_name']} ({prev_repo['updated_at']}), Current: {recent_repo['full_name']} ({recent_repo['updated_at']})")
            prev_repo = recent_repo

        time.sleep(10)  # 1-minute interval

if __name__ == "__main__":
    main()