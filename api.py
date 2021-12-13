import requests
import pprint

class API:

    def __init__(self) -> None:
        self.inv_url = "https://www.toontownrewritten.com/api/invasions"
        self.last_inv_time = None

        self.fo_url = "https://www.toontownrewritten.com/api/fieldoffices"
        self.last_fo_time = None

        self.login_url = "https://www.toontownrewritten.com/api/login"
        self.last_login_time = None

        self.sm_url = "https://www.toontownrewritten.com/api/sillymeter"
        self.last_sm_time = None

        self.pop_url = "https://www.toontownrewritten.com/api/population"
        self.last_pop_time = None

    def __send_request(self, url, params):
        r = requests.get(url=url, params=params)
        return r.json()

    def get_invasions(self):
        """
        Response: {
            'error': None or string,
            'invasions': invasion data,
            'lastUpdated': timestamp of last queried data
        }

        Invasion Data: {
            'district invasion is in': {
                'asOf': timestamp of when district last reported status,
                'progress': '200/4000',
                'type': string
            }
        }
        """
        data = self.__send_request(self.inv_url, {'User-Agent': 'SamGoodin-MasterMax | Independent Dev'})
        if data['error']:
            print(f"Invasion Error: {data['error']}")
        if data['lastUpdated'] != self.last_inv_time:
            self.last_inv_time = data['lastUpdated']
            return data['invasions']
        else:
            return None

    def get_field_offices(self):
        """
        Response: {
            'fieldOffices': FO data,
            'lastUpdated': timestamp of last queried data
        }

        Field Office Data: {
            Zone ID: {
                'department': string,
                'difficulty': number of stars,
                'annexes': number of annexes,
                'open': boolean meaning open for toons to enter,
                'expiring': how long until remaining groups get kicked
            }
        }
        """
        data = self.__send_request(self.fo_url, {'User-Agent': 'SamGoodin-MasterMax | Independent Dev'})
        if data['lastUpdated'] != self.last_fo_time:
            self.last_fo_time = data['lastUpdated']
            return data['fieldOffices']
        else:
            return None

    def get_population(self):
        """
        Response: {
            'error': None or string,
            'totalPopulation': number,
            'populationByDistrict': dict of district names to population values,
            'lastUpdated': timestamp of last queried data
        }
        """
        data = self.__send_request(self.pop_url, {'User-Agent': 'SamGoodin-MasterMax | Independent Dev'}) 
        if data['error']:
            print(f"Invasion Error: {data['error']}")
        if data['lastUpdated'] != self.last_pop_time:
            self.last_pop_time = data['lastUpdated']
            return data
        else:
            return None

if __name__ == '__main__':
    api = API()
    api.get_invasions()