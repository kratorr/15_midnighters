import requests
import pytz
import collections
from pytz import timezone
from datetime import datetime


def load_attempts(url):
    pages = 10
    for page in range(1, pages+1):
        params = {"page": page}
        response_json = requests.get(url, params=params).json()
        for record in response_json["records"]:
            yield {
                'username': record["username"],
                'timestamp': record["timestamp"],
                'timezone': record["timezone"],
            }


def get_midnighters(records):
    midnighters = collections.defaultdict(list)
    utc = pytz.utc
    for record in records:
        username = record["username"]
        record_timezone = timezone(record["timezone"])
        utc_record_datetime = utc.localize(
            datetime.utcfromtimestamp(record["timestamp"])
        )
        record_local_datetime = utc_record_datetime.astimezone(record_timezone)
        local_start_night = record_local_datetime.replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        local_end_night = record_local_datetime.replace(
            hour=6, minute=0, second=0, microsecond=0
        )
        if local_end_night > record_local_datetime > local_start_night:
            midnighters[username].append(
                record_local_datetime.strftime("%D %R")
            )
    return midnighters


if __name__ == "__main__":
    api_url = "http://devman.org/api/challenges/solution_attempts/"
    records = []
    for record in load_attempts(api_url):
        records.append(record)
    midnighters = get_midnighters(records)
    for username, send_times in midnighters.items():
        print(username, "sent for review: ")
        for send_time in send_times:
            print(send_time)
        print()