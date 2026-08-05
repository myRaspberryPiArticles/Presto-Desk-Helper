import network
import requests
import time
from presto import Presto
import json

presto = Presto()

presto.connect()   
# Make GET request


def fetch_time():
    try:
        response = requests.get("https://gateway.timeapi.world/timezone/Europe/London", headers={"x-rapidapi-key": "1fa031b1ddmsh6269abb2d931465p130deejsn5c1cda14dd16"})
        # Get response content
        response_content = json.loads(response.content)
        
        # Print results
        print('Response content:', response_content)
        print(f'time: {response_content["datetime"]}')
        
        return response_content["datetime"]
        
    except Exception as e:
        print('An error occurred during the request:', str(e))
                
def timedata_to_date(datetime_string):
    year = int(datetime_string[0:4])
    month = int(datetime_string[5:7])
    day = int(datetime_string[8:10])
    hour = int(datetime_string[11:13])
    minute = int(datetime_string[14:16])
    second = int(datetime_string[17:19])
    
    datetime_object = time.mktime((year, month, day, hour, minute, second, 0, 0))
    localtime = time.localtime(datetime_object)
    
    day = localtime[6]
    day_number = localtime[2]
    month = localtime[1]

    DAYS = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun"]
    
    MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"]

    day_name = DAYS[day]
    month_name = MONTHS[month-1]
    
    date_string = f"{day_name} {day_number} {month_name}"

    return date_string

def timedata_to_seconds(datetime_string):
    second = datetime_string[17:19]
    return second

if __name__ == "__main__":
    #get_time()
    #get_date()
    pass