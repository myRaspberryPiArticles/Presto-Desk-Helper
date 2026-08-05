# Source - https://stackoverflow.com/a/35016037
# Posted by TyCharm, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-05, License - CC BY-SA 4.0

def time_conversion(time):   
    days = 0
    hours = 0
    mins = 0

    days = time // 1440 # minutes in a day = 1440
    leftover_minutes = time % 1440 # % is remainder
    hours = leftover_minutes // 60 # if the leftover minutes are more than 60, it will out it into hours
    mins = leftover_minutes % 60 # % is remainder
    
    converted_string = f"{str(round(days))}d {str(round(hours))}h {str(round(mins))}m"
    
    return converted_string
    