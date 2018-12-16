import datetime

def sun_angle(time):
    try:
        a = datetime.datetime.strptime(time, "%H:%M")
        b = datetime.datetime.strptime("06:00", "%H:%M")
        c = datetime.datetime.strptime("18:00", "%H:%M")
        if a >= b and a <= c:
            time = time.split(':')
            u = int(time[0]) - 6
            v = u * 60
            v += int(time[1])
            x = v * 0.25
            return x
        else:
            return "I don't see the sun!"
    except ValueError:
        pass
