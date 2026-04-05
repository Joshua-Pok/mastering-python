import urllib.request
import json

from models import User

from validation import parse_users

class APIClient():

    def fetch_users(self, url: str) -> list[User]:
        with urllib.request.urlopen(url) as response:
            request_bytes = response.read()

        request_text = request_bytes.decode('utf-8')

        payload_list = json.loads(request_text)


        users = parse_users(payload_list)


        return users
            


