import requests
import pyodbc
import json

######################################
#           USED LIBRARIES           #
######################################
# 1. Requests - used for API calls   #
# python -m pip install requests     #
#                                    #
# 2. pyodbc - Used to connect to SQL #
# pip install pyodbc                 #  
######################################


#############
# dattoinfo #
#############

username = "PUBLIC_KEY"
password = "SECRET_KEY"

auth_string = f"{username}:{password}"

url = "https://api.datto.com/v3/" # find aptek url
headers = {'Authorization': f'Basic {auth_string}' } #change to match datto standard

############
# SQL info #
############

server = '8bitserver'
database = 'Datto'
username = 'data'
password = 'password'
connectionString = f'Driver={{SQL Server Native Client 11.0}};SERVER={server};DATABASE={database};UID={username};PWD={password};'


# Make GET call from datto info above
response = requests.get(url, headers=headers)

# Check response - if not valid return error
if response.status_code != 200:
    print(f"Error with GET from datto: {response.status_code}, {response.text}")
    exit(1) 

# Put returned data into dict 
raw_data = response.json()

conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

    





