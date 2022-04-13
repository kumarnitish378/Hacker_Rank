# program to convert 12 hr time format to 24 hr time format
# by Nitish kumar sharma [ECE], nitish.ns377@gmail.com

time = input("enter time in 12hr format : ")
if "am" in time or "AM" in time or "pm" in time or "PM" in time:
    hour = int(time[0:2:])
    if "pm" in time or "PM" in time:
        hour = int(time[0:2:])
        if hour <= 11:
            hr = str(hour+12)
            min = time[2:8:]
            time = hr+min
            print(time)
        else:
            hr = str(hour)
            min = time[2:8:]
            time = hr + min
            print(time)
    elif hour >11 and hour <=12 :
        hour = int(time[0:2:])
        if hour >11 and  hour <= 12:
            hr = "00"
            min = time[2:8:]
            time = hr+min
            print(time)
    else:
        hour = int(time[0:2:])
        if hour <= 11:
            hr = str(hour)
            if len(hr) < 2:
                hr = "0"+hr
            min = time[2:8:]
            time = hr + min
            print(time)

else:
    print(time)
