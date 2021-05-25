
def equation(x1,x2,y1,y2,x):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - x1*a
    y = a * x + b
    return y

with open("valeurs_short_waves.txt","w") as file:
    file.write("x1,x2,y1,y2,x,y\n")
    while True:
        x1 = float(input("x1 : "))
        x2 = float(input("x2 : "))
        y1 = float(input("y1 : "))
        y2 = float(input("y2 : "))
        x = float(input("x : "))
        y = equation(x1,x2,y1,y2,x)
        print("y = ",y)
        print()
        file.write(str(x1)+","+str(x2)+","+str(y1)+","+str(y2)+","+str(x)+","+str(y))
        file.write("\n")
