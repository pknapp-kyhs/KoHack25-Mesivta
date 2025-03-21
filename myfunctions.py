import os
from datetime import datetime
import pytz

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_time():
    """
    Formatters: (all have '%' before them)

    a - weekday
    b - month name
    d - day of month
    Y - year

    I - hour
    M - minute
    S - second
    p - AM/PM

    """

    timezone = pytz.timezone('America/New_York')
    now = datetime.now(timezone)
    
    f_date = now.strftime("%a, %b %d %Y\n%I:%M:%S %p")
    
    print(f_date)