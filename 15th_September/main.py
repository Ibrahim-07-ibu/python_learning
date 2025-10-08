x = int(input("enter the coordinates of x"))
y = int(input("enter the coordinates of y"))

if x > 0 and y > 0 :
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0 :
    print("Quadrant IV")
else :
    print("Invalid")
