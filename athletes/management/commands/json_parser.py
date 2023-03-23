import json 
from django.core.management.base import BaseCommand
from athletes.models import Garage
import requests
from json import JSONDecodeError


class Command(BaseCommand):
    help = 'Parses the JSON-file'

    def add_arguments(self, parser):
        parser.add_argument("filename", nargs='*', type=str)


    def handle(self, *args, **options):
        with open('athletes\garages.json') as f:
            data = json.load(f)
            print(end='')
        with open('json_data', 'w+') as file:
            file = json.dumps(data, indent=4)
            print(file)

            


    # def _get_parking_facilities(self, filename):
    #     with open(filename) as json_file:
    #         user_data = json.load(json_file)
        
    #     garage = user_data.get("ParkingFacilities")
    #     self._create_garages(garage)
    #     print(garage)

    # def handle(self, *args, **options):
    #     with open('athletes\garages.json') as f:
    #         data = json.load(f)
    #         for i in data:
    #             print(end='')
    #     print(data)
            
    
    # def handle(self, *args, **options):
    #     try:
    #         with open('athletes\garages.json', 'r', encoding='cp1252') as f:
    #             data = json.load(f)
    #             print(f)
    #     except json.decoder.JSONDecodeError:
	#             print("There was a problem accessing the equipment data.")






    # def handle(self, *args, **options):
    #     with open('athletes\garages.json', encoding='utf-8', errors='ignore') as f:
    #         f = json.load(f, strict=False)
    #         print(f)



    # def handle(self, *args, **options):
    #     try: 
    #         resp = requests.get("https://reqres.in/api/users")
    #         resp_dict = resp.json()
    #         pretty = json.dumps(resp_dict, indent=4)
    #         print(pretty)
    #     except JSONDecodeError:
    #         ('TEST')






# for item in response:
#     print(item['Message'])
#     print(item['Status'])
#     postalArray = item['PostOffice']
#     for k in postalArray:
#         print(k['Name'])
#         print(k['District'])



    # def _get_internal_garage(self,data):
    #     name = data.get("name")
    #     identifier = data.get("name")
    #     garage = Garage.objects.create(id=identifier, name=name)
    #     print(garage)


    # def _create_garages(self, garage):
    #     for i in garage:
    #        x = self._get_internal_garage(i)
    #        print(x)



    # def _get_parking_facilities(self, filename):
    #     with open(filename, "r") as json_file:
    #         user_data = json.load(json_file)

    #     garage = user_data.get("parkingFacilities")
    #     self._create_garages(garage) 
    #     print(garage)       
