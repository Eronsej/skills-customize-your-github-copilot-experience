import json
import requests

API_URL = "https://api.agify.io?name=michael"
OUTPUT_FILE = "api_response.json"


def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Request failed with status {response.status_code}")
    return response.json()


def display_data(data):
    name = data.get("name")
    age = data.get("age")
    count = data.get("count")

    print("API Response Summary")
    print("--------------------")
    print(f"Name: {name}")
    print(f"Predicted Age: {age}")
    print(f"Sample Size: {count}")


def save_data(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print(f"Saved API response to {filename}")


if __name__ == "__main__":
    try:
        api_data = fetch_api_data(API_URL)
        display_data(api_data)
        save_data(api_data, OUTPUT_FILE)
    except Exception as error:
        print(f"Error: {error}")
