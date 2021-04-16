speed = int(input("enter speed: "))
average_speed = int(input("average of road: "))

points = (speed - average_speed)/5

if speed  < 60:
    print("ok")
elif speed == 60:
    print("OK")

if points < 12:
    print("demerit: " + str(points))

else:
    print("time to go to jail")



