class Travel_Methods():
    def __init__(self):
        pass
    def convert_to_minutes(time_array):
        minutes_array=[]
        for x in time_array:
            hour = int(str(x).split(".")[0])
            minutes = int(float("%.2f" % (x-hour))*100)
            if hour in [0,1,2,3]:
                hour = hour+24
            minutes_array.append(hour*60+minutes)
        return sum(minutes_array)/len(time_array)

    def convert_to_hours(minutes_average):
        hour = int(minutes_average/60)
        minute = ((minutes_average / 60 - hour) * 60) / 100
        minute = float("%.2f" % minute)

        if hour==24:
            hour =12
        elif hour>24:
            hour=hour-24
        elif hour>12:
            hour=hour-12

        hour_minute = float("%.2f" % (hour + minute))
        hour_minute = str(hour_minute).replace(".",":")
        if len(hour_minute.split(":")[1])==1:
            hour_minute = hour_minute+"0"
        return hour_minute