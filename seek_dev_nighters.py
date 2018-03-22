import requests
import pytz
import collections
from datetime import datetime


def load_attempts(url):
    page = 1
    count_of_pages = 1
    while True:
        params = {"page": page}
        response_json = requests.get(url, params=params).json()
        count_of_pages = response_json["number_of_pages"]
        records = response_json["records"]
        for record in records:
            yield {
                "username": record["username"],
                "timestamp": record["timestamp"],
                "timezone": record["timezone"],
            }
        page +=1
        if page > count_of_pages:
            break


def get_midnighters(records):
    start_night = 0
    end_night = 6
    midnighters = collections.defaultdict(list)
    for record in records:
        timestamp = record["timestamp"]
        timezone_record = pytz.timezone(record["timezone"])
        username = record["username"]
        record_local_datetime = datetime.fromtimestamp(
            timestamp, tz=timezone_record
        )
        if end_night > record_local_datetime.hour >= start_night:
            midnighters[username].append(
                record_local_datetime.strftime("%D %R")
            )
    return midnighters


if __name__ == "__main__":
    api_url = "http://devman.org/api/challenges/solution_attempts/"
    midnighters = get_midnighters(load_attempts(api_url))
    for username, send_times in midnighters.items():
        print(username, "sent for review: ")
        print("\n".join(send_times))

