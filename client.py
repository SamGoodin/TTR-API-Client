import time
from api import API
from pprint import pprint
import tkinter as tk


class Client:

    def __init__(self) -> None:
        self.api = API()
        self.api_calls = [
            self.api.get_invasions,
            self.api.get_field_offices,
            self.api.get_population,
            self.api.get_silly_meter
        ]

        #self.setup_inv()

    def setup_inv(self):
        self.inv_win = tk()


    def create_inv_table(self, data):
        keys = list(data.keys())
        keys.sort()
        for key in keys:
            inv_data = data[key]
            progress = inv_data['progress']
            type = inv_data['type']
        

    def run_client(self):
        while True:
            for call in self.api_calls:
                data, name = call()
                if data:
                    if call == self.api.get_invasions:
                        print(f"---------Start of {name}-------")
                        pprint(data)
                        print(f"---------End of {name}---------")
                        self.create_inv_table(data)
                    elif call == self.api.get_field_offices:
                        pass
                    elif call == self.api.get_population:
                        pass
                    elif call == self.api.get_silly_meter:
                        pass
                    else:
                        print("Unknown call made to the API.")
                    


if __name__ == '__main__':
    client = Client()
    client.run_client()