# Project title 
  Building my first own API! 

# A brief description of what this project does and who it's for
  The API makes it possible for the gym to register the instructors and the athletes. It also provides the instructors with an personal accesscode. Further relevant information of the athlete can be stored: contact information, the contactperson, grouplesson, level, etc. 

# API Reference
  MODELS 
  - Create a FK to Operator in the Garage model 
  - Create in the Tariff model two FK's: to the Operator and the Garage model 
  - Arguments: default=None, null=True, on_delete=CASCADE

  SERIALIZERS
  - Create two PrimaryKeyRelatedFields in the Operator class: to the Garage class and to Tariff class

  VIEWS
  - Import filters from django restframework
  - Use filters: SearchFilter and OrderingFilter 

  URLS(ROOT)

  URLS
  - Import DefaultRouter from restframework
  - Register the viewsets with the router

    ADMIN
  - Create a superuser via the terminal to use the admin
  - Register models to display & customize your models in the Django admin panel

  SETTINGS
  - Add a part of the "staticDataUrl" from the garages.json file: STATIC_RDW_DATA_URL = 'https://npropendata.rdw.nl/parkingdata/v2/static/'

  EXTRA
  - Add the garages.json file to your app: JSON-file with RDW_data: name, identifier, staticDataUrl, limitedAccess
  - Build a json_parser: python code to retrieve data from the file garages.json (a Command class that inherits from Basecommand)
  - Build a RDW_parser: python code to retrieve data from the staticDataUrls (a Command class that inherits from Basecommand)
