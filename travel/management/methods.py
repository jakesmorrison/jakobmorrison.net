class Travel_Methods():
    def __init__(self):
        pass
    def convert_to_minutes(time_array):
        minutes_array=[]
        for x in time_array:
            hour = int(str(x).split(".")[0])
            minutes = int(float("%.2f" % (x-hour))*100)
            minutes_array.append(hour*60+minutes)
        return sum(minutes_array)/len(time_array)

    def convert_to_hours(minutes_average):
        hour = int(minutes_average/60)
        if hour>12:
            hour=hour-12
        minute = ((minutes_average / 60 - hour) * 60) / 100
        minute = float("%.2f" % minute)
        print(minute)
        hour_minute = float("%.2f" % (hour + minute))
        return str(hour_minute).replace(".",":")