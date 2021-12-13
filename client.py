import time
from api import API
from pprint import pprint


class Client:

    def __init__(self) -> None:
        self.api = API()
        self.api_calls = [
            self.api.get_invasions,
            self.api.get_field_offices
        ]

    def run_client(self):
        while True:
            for call in self.api_calls:
                data, name = call()
                if data:
                    print(f"---------Start of {name}-------")
                    pprint(data)
                    print(f"---------End of {name}---------")


if __name__ == '__main__':
    client = Client()
    client.run_client()