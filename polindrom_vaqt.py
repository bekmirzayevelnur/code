time = input()
hours = int(time[:2])
minutes = int(time[3:])
while True:
    minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
        if hours == 24:
            hours = 0
    time_str = f"{hours:02d}:{minutes:02d}"
    if time_str == time_str[::-1]:
        print(time_str)
        break
