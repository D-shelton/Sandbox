import os
import requests
import pyodbc
import json
import base64
from dotenv import load_dotenv

######################################
#           USED LIBRARIES           #
######################################
# 1. Requests - used for API calls   #
# python -m pip install requests     #
#                                    #
# 2. pyodbc - Used to connect to SQL #
# pip install pyodbc                 #
#                                    #
# 3. dotenv - used to load API data  #
# pip install python-dotenv          #  
######################################
#        ADDITIONAL INSTALLS         #
######################################
# 1. ODBC library                    #
# sudo apt install unixodbc-dev      #
#                                    #
# sudo apt-get update                #
######################################


#############
# dattoinfo #
#############

# loads API key info from .env
load_dotenv()
username = os.getenv('DATTO_PUBLIC_KEY')
password = os.getenv('DATTO_PRIVATE_KEY')

# Build headers to log in and encode
auth_string = f"{username}:{password}"
encoded_auth_string = base64.b64encode(auth_string.encode()).decode('utf-8')

# url to access and header to use
url = "https://api.datto.com/v1/bcdr/agent?_page=1&_perPage=100" 
headers = {'Authorization': f'Basic {encoded_auth_string}'} 


############
# SQL info #
############

server = '8bitserver'
database = 'Datto'
username = 'data'
password = 'password'
connectionString = f'Driver={{SQL Server Native Client 11.0}};SERVER={server};DATABASE={database};UID={username};PWD={password};'

def formatResponse(raw_data):
    # iterate over clients in raw_data
        print("starting iteration over clients")
        for client in raw_data["clients"]:
            # sets client's name in variable and prints it
            client_name = client.get("clientName")
            print(f"Client Name: {client_name}")

            # iterate over each agent under client
            print("starting iteration over agents")
            for agent in client.get("agents", []):
                # gets hostname for agent
                hostname = agent.get("hostname")
                # gets boolean value representing success
                screenshot_success = agent.get("screenshotSuccess")

                # prints agent name and screenshot success
                if screenshot_success != True:
                    print("Screenshot Failed")

def tableCheck(cursor):
    table_name = 'datto'
    cursor.execute(f"""
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}')
        BEGIN
            CREATE TABLE backups (
                id INT PRIMARY KEY IDENTITY(1,1),
                client_id INT NOT NULL,
                client_name NVARCHAR(100),
                backup_status NVARCHAR(50),
                backup_date DATETIME NOT NULL,
                CONSTRAINT FK_Client FOREIGN KEY(client_id) REFERENCES clients(client_id)
            );
        END;
                """)
    

def main():
    # Make GET call from datto info above
    response = requests.get(url, headers=headers)

    # Check response - if not valid return error
    if response.status_code != 200:
        print(f"Error with GET from datto: {response.status_code}, {response.text}")
        exit(1) 
    # Else call success, put json data into dict - print to test
    else:
        print("Call successful, report being prepared")
        raw_data = response.json()
        print(json.dumps(raw_data, indent=4))


    # conn = pyodbc.connect(connectionString)
    # cursor = conn.cursor()
    # tableCheck(cursor)

        


if __name__ == '__main__':
    main()


