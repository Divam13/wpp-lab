import pandas as pd
import datetime

dt_jan_15_2012 = pd.to_datetime('2012-01-15')
print("a) DateTime for Jan 15 2012:", dt_jan_15_2012)

dt_specific_time = pd.to_datetime('2012-01-15 21:20')
print("b) Specific date and time of 9:20 PM:", dt_specific_time)

local_datetime = pd.Timestamp.now()
print("c) Local date and time:", local_datetime)

date_only = pd.to_datetime('2025-04-14').date()
print("d) Date without time:", date_only)

current_date = pd.Timestamp.today().date()
print("e) Current date:", current_date)

time_from_datetime = pd.Timestamp.now().time()
print("t) Time from a datetime:", time_from_datetime)

current_local_time = datetime.datetime.now().time()
print("g) Current local time:", current_local_time)
