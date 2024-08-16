import datetime
import pytz
# utc_date = datetime.datetime.now()
# eet_date = str(utc_date + datetime.timedelta(hours = 3))[0:10]
# current_time = int(str(utc_date + datetime.timedelta(hours = 3))[11:16].replace(":",""))
# eet_date_format = eet_date.split('-')
# # logfilename = eet_date_format[0]+eet_date_format[1] +eet_date_format[2]
# print(eet_date_format)


eet_zone = pytz.timezone('Europe/Helsinki')  # EET: UTC+2, EEST (daylight saving): UTC+3
utc_now = datetime.datetime.now(pytz.utc)
eet_time = utc_now.astimezone(eet_zone)
date_list = [eet_time.strftime('%Y'), eet_time.strftime('%m'), eet_time.strftime('%d')]
logfilename = date_list[0]+date_list[1] +date_list[2]
current_time = int(str(eet_time )[11:16].replace(":",""))
print(utc_now)



# eet_zone = pytz.timezone('Europe/Helsinki')  # EET: UTC+2, EEST (daylight saving): UTC+3
# utc_now = datetime.datetime.now(pytz.utc)
# eet_time = utc_now.astimezone(eet_zone)
# current_timer = int(str(eet_time )[11:16].replace(":",""))