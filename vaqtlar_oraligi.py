from datetime import timedelta

a = input().split(' ')
b = input().split(' ')
time1 = timedelta(hours=int(a[0]), minutes=int(a[1]), seconds=int(a[2]))
time2 = timedelta(hours=int(b[0]), minutes=int(b[1]), seconds=int(b[2]))
time3 = time1 - time2
print(int(abs(time3.total_seconds())))
