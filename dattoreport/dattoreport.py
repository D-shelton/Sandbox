import os
import requests
import pyodbc
import json
import base64
from dotenv import load_dotenv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

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
#                                    #
# 4. openpyxl - used for excel work  #
# pip install openpyxl               #  
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
# libs - dotenv
load_dotenv()
username = os.getenv('DATTO_PUBLIC_KEY')
password = os.getenv('DATTO_PRIVATE_KEY')

# Build headers to log in and encode
# libs - base64
auth_string = f"{username}:{password}"
encoded_auth_string = base64.b64encode(auth_string.encode()).decode('utf-8')

# url to access and header to use
url = "https://api.datto.com/v1/bcdr" 
headers = {'Authorization': f'Basic {encoded_auth_string}'} 


# call to get list of active devices
# libs - requests, json
def get_active():
    # set url to get device list
    device_url = f"{url}/device"

    try:
        # sets response to get device list in response
        response = requests.get(device_url, headers=headers)

        # check return status code
        if response.status_code == 200:
            return response.json()
        # if failed print error code and message
        else:   
            print(f"Error: Failed Device retrieval -  Code:{response.status_code}, Text:{response.text}")
            return None
        
    except Exception as e:
        print(f"Exception while retrieving devices: {e}")
        return None
    
# call to get device backup info
# libs - requests, json
def get_backups(serialNumber):
    # set url to get device info
    backup_url = f"{url}/{serialNumber}/asset"

    try:
        # sets response to get device status
        response = requests.get(backup_url, headers=headers)

        # Check return code
        if response.status_code == 200:
            # if success - return json
            return response.json()
        
        else:
            print(f"Error: Could not retrieve info for {serialNumber} Error {response.status_code}, {response.text}")
            return None
        
    except Exception as e:
        print(f"Exception during retrieval for {serialNumber}: {e}")
        return None
    
# writes data to excel workbook
# libs -  openpyxl
def write_xlsx(device_backup_data, filename="datto_report.xlsx"):
    # Create and activate a workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Datto Report"

    # define headers for columns
    headers = [
        "serialNumber", "name", "agentVersion", "isPaused", "isArchived", 
        "latestOffsite", "lastSnapshot", "lastScreenshotAttempt", 
        "lastScreenshotAttemptStatus", "lastScreenshotUrl", 
        "localStorageUsed", "localStorageAvailable"
    ]

    # Write headers to first row
    for col_num, header in enumerate(headers, 1):
        col_letter = get_column_letter(col_num)
        ws[f"{col_letter}1"] = header

    # Write each device's backup data to following rows
    for row_num, data in enumerate(device_backup_data, 2):  # Start from row 2
        ws[f"A{row_num}"] = data["serialNumber"]
        ws[f"B{row_num}"] = data["name"]
        ws[f"C{row_num}"] = data["agentVersion"]
        ws[f"D{row_num}"] = data["isPaused"]
        ws[f"E{row_num}"] = data["isArchived"]
        ws[f"F{row_num}"] = data["latestOffsite"]
        ws[f"G{row_num}"] = data["lastSnapshot"]
        ws[f"H{row_num}"] = data["lastScreenshotAttempt"]
        ws[f"I{row_num}"] = data["lastScreenshotAttemptStatus"]
        ws[f"J{row_num}"] = data["lastScreenshotUrl"]
        ws[f"K{row_num}"] = data["localStorageUsed"]
        ws[f"L{row_num}"] = data["localStorageAvailable"]

    # Save workbook
    wb.save(filename)
    print(f"Data written to {filename}")
    

# main func to pull and report data
def datto_report():
    # get list of active devices
    devices = get_active()

    # Check for return of None to report error
    if devices is None or not devices:
        print("No devices found/retrieved")
        return

    full_backup_data = []
    
    # Iterate over devices
    for device in devices:
        # Get serialNumber for device
        serialNumber = device.get("serialNumber")
        # if serial is found check for backups
        if serialNumber:
            backup_info = get_backups(serialNumber)
            # if backups are found
            if backup_info:
                # import 
                device_data = {
                    "serialNumber": serialNumber,
                    "name": device.get("name", ""),
                    "agentVersion": backup_info.get("agentVersion", ""),
                    "isPaused": backup_info.get("isPaused", ""),
                    "isArchived": backup_info.get("isArchived", ""),
                    "latestOffsite": backup_info.get("latestOffsite", ""),
                    "lastSnapshot": backup_info.get("lastSnapshot", ""),
                    "lastScreenshotAttempt": backup_info.get("lastScreenshotAttempt", ""),
                    "lastScreenshotAttemptStatus": backup_info.get("lastScreenshotAttemptStatus", ""),
                    "lastScreenshotUrl": backup_info.get("lastScreenshotUrl", ""),
                    "localStorageUsed": device.get("localStorageUsed", ""),
                    "localStorageAvailable": device.get("localStorageAvailable", ""),
                }
                
                # Append the device's data to the list
                full_backup_data.append(device_data)
            else: 
                print(f"No backup info found for {serialNumber}")
        else:
            print(f"Device serial not found")

    write_xlsx(full_backup_data)


if __name__ == "__main__":
    print("Running report directly")
    datto_report()
            