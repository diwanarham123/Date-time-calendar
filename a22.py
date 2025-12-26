import datetime
from datetime import date
import time

today = date.today()
now = datetime.datetime.now()

print("Today's date is",today)
print("\nCurrent Date and time is",now)
print("\nDate components", today.year, today.month, today.day)