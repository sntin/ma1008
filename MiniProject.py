import time, math
import turtle as t

def get_choice():
    # Get user choice
    while True: 
        choice = input("Key in the number you want:\n   1: Manual Input\n   2: File Input\n   3: Point and Click\nYour Choice: ")
        try: 
            if choice in ["1", "2", "3"]:
                choice = int(choice)
                break 
            else: 
                print("Please choose 1, 2 or 3 only\n")
        except: 
            print("Please choose 1, 2 or 3 only\n")
    return choice


def get_inputs_manual(coordinates):
    coordinates = []
    while True: 
        try: 
            sides = int(input(f"Key in the number of sides of the polygon: "))
            if 3 <= sides <= 10: 
                break
            else: 
                print("We only accept 3 to 10. Try again")
        except: 
            print("Please key in integer only. Try again")

    print()
    N = 1
    while N <= sides: 
        # check if want straight or curved
        while True: 
            SorC = input(f"Enter S for straight lines and C for curved lines for line/curves {N}: ").upper()
            if SorC in ["S", "C"]:
                break
            else: 
                print("Please only enter S or C. Try again.")
                print()
 
        # get coordinates
        while True: 
            try: 
                print(f"Input the coordinates for line/curve {N}")
                if N == 1: 
                        print("Enter coordinate of starting point")
                        x0 = float(input("x: "))
                        y0 = float(input("y: "))
                        mousedot(x0,y0)

                        print("Enter coordinate of ending point")
                        x1 = float(input("x: "))
                        y1 = float(input("y: "))
                        mousedot(x1,y1)

                elif N == sides: 
                        x0 = coordinates[N-2][-2]
                        y0 = coordinates[N-2][-1]
                        x1 = coordinates[0][0]
                        y1 = coordinates[0][1]
                        print(f"Coordinate of starting point: ({x0},{y0})")
                        print(f"Coordinate of ending point: ({x1},{y1})")
                else: 
                        x0 = coordinates[N-2][-2]
                        y0 = coordinates[N-2][-1]
                        print(f"Coordinate of starting point: ({x0},{y0})")

                        print("Enter coordinate of ending point")
                        x1 = float(input("x: "))
                        y1 = float(input("y: "))
                        mousedot(x1,y1)
            except: 
                print("Key in numbers only please. Try again.")
                continue

            if SorC == "S": 
                coordinate = (x0,y0,x1,y1)
                coordinates.append(coordinate)
                draw_straight(coordinate)
                break    
            else: 
                try: 
                    print("Enter coordinate of control point 1")
                    x2 = float(input(f"x: "))
                    y2 = float(input(f"y: "))
                    mousedot(x2,y2)

                    print("Enter coordinate of control point 2")
                    x3 = float(input(f"x: "))
                    y3 = float(input(f"y: "))
                    mousedot(x3,y3)

                    coordinate = (x0,y0,x2,y2,x3,y3,x1,y1)
                    coordinates.append(coordinate)
                    draw_curve(coordinate)
                    break
                except: 
                    print("Key in numbers only please. Try again.")
                 
        N += 1
        print()
    return coordinates


def get_inputs_file():
    while True: 
        coordinates = []
        while True: 
            try: 
                infile_name = input("Key in input file name: ")
                infile = open(infile_name, "r")
                break
            except:
                print("File not found. Try again.")
        
        infile_lines = infile.readlines()
        t.color(infile_lines[0].strip())
        try:
            space_index = infile_lines.index("\n")
            for i in range(1, space_index):
                line = [float(x) for x in infile_lines[i].strip().split(" ")]
                coordinates.append(tuple(line))
            break
        except: 
            print("Wrong file format.")

    return coordinates


click = False
def waitforclick():
    print("Waiting for click")
    global click

    t.update()
    click = False
    while not click: 
        t.update()
        time.sleep(.1)
    
    click = False


def mousedot(x,y):
    t.penup()
    t.goto(x,y)
    t.dot(5, "red")


def func(x,y):
    global templist, click

    t.onscreenclick(None)
    templist.extend([x,y])
    mousedot(x,y)
    click = True


def get_inputs_click(coordinates):
    global templist
    templist = []
    while True: 
        try: 
            sides = int(input(f"Key in the number of sides of the polygon: "))
            if 3 <= sides <= 10: 
                break
            else: 
                print("We only accept 3 to 10. Try again")
        except: 
            print("Please key in integer only. Try again")


    N = 1
    while N <= sides: 
        # check if want straight or curved
        while True: 
            SorC = input(f"Enter S for straight lines and C for curved lines for line/curves {N}: ").upper()
            if SorC in ["S", "C"]:
                break
            else: 
                print("Please only enter S or C. Try again.")
 
        # get coordinates
        while True: 
            try: 
                print(f"Click the coordinates for line/curve {N}")
                if N == 1: 
                        print("Click starting point")
                        t.onscreenclick(func)
                        waitforclick()

                        print("Click end point")
                        t.onscreenclick(func)
                        waitforclick()
                elif N == sides: 
                        x0 = coordinates[N-2][-2]
                        y0 = coordinates[N-2][-1]
                        x1 = coordinates[0][0]
                        y1 = coordinates[0][1]
                        print(f"x-coordinate of start point: {x0}")
                        print(f"y-coordinate of start point: {y0}")
                        print(f"x-coordinate of end point: {x1}")
                        print(f"y-coordinate of end point: {y1}")
                        templist.extend([x0,y0,x1,y1])
                else: 
                        x0 = coordinates[N-2][-2]
                        y0 = coordinates[N-2][-1]
                        print(f"x-coordinate of start point: {x0}")
                        print(f"y-coordinate of start point: {y0}")
                        templist.extend([x0,y0])

                        print("Click end point")
                        t.onscreenclick(func)
                        waitforclick()
            except: 
                print("Error, dont know why")
                break

            if SorC == "S": 
                coordinates.append(tuple(templist))
                draw_straight(tuple(templist))
                templist = []
                break    
            else: 
                try:          
                    temp = [templist[2], templist[3]]
                    templist.pop()
                    templist.pop()

                    print("Click control point 1")
                    t.onscreenclick(func)
                    waitforclick()

                    print("CLick control point 2")
                    t.onscreenclick(func)
                    waitforclick()

                    templist.extend(temp)
                    
                    coordinates.append(tuple(templist))
                    draw_curve(tuple(templist))

                    templist = []
                    break
                except: 
                    print("Key in numbers only please. Try again.")
        
        N += 1
    return coordinates


def draw_straight(coordinate):
    x0,y0,x1,y1 = coordinate
    t.up()
    t.goto(x0,y0)
    t.down()
    t.goto(x1,y1)
    t.up()


def draw_curve(coordinate):
    p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y = coordinate    
    t.up()
    t.goto(p0x, p0y)
    t.down()

    N = 101
    for i in range(N): 
        m = i / (N-1)
        px = (1-m)**3 *p0x + 3*m*(1-m)**2 *p1x + 3*m**2*(1-m)*p2x + m**3*p3x
        py = (1-m)**3 *p0y + 3*m*(1-m)**2 *p1y + 3*m**2*(1-m)*p2y + m**3*p3y

        t.goto(px,py)
    t.up()


def draw(coordinates):
    try: 
        for coordinate in coordinates: 
            if len(coordinate) == 4: 
                draw_straight(coordinate)
            else: 
                draw_curve(coordinate)
    except: 
        print("Wrong input format.")


def save_input(coord):
    output_name = input("Key in output file name: ")
    outfile = open(output_name, "w")
    
    while True: 
        try: 
            color = input("Key in color of the outline, left blank if want black: ").strip()
            if color == "":
                color = "black"
            t.color(color)
            break
        except: 
            print("Invalid color.")
    
    print(color, file=outfile)

    for cord in coord: 
        for num in cord: 
            print(f"{num} ", end="", file=outfile)
        print("", file=outfile)

    print("", file=outfile)
    outfile.close()


def centroid(coordinates):
    sumx = 0
    sumy = 0
    sides = len(coordinates)
    for side in coordinates: 
        sumx += side[0]
        sumy += side[1]
    return sumx/sides, sumy/sides


def translation(coordinates, xt, yt):
    new_coordinates = coordinates.copy()
    for i in range(len(new_coordinates)): 
        coordinate = new_coordinates[i]
        for j in range(len(coordinate)):
            coordinate = new_coordinates[i]
            if j % 2 == 0:
                new_coordinates[i] = coordinate[0:j] + (coordinate[j] + xt,) + coordinate[j+1:]
            else:
                new_coordinates[i] = coordinate[0:j] + (coordinate[j] + yt,) + coordinate[j+1:]
    return new_coordinates

def rotation(coordinates, angle):
    angle *= math.pi / 180
    new_coordinates = coordinates.copy()
    for i in range(len(new_coordinates)):
        coordinate = new_coordinates[i]
        for j in range(0,len(coordinate),2):
            coordinate = new_coordinates[i]
            new_coordinates[i] = coordinate[0:j] + (coordinate[j]*math.cos(angle) - coordinate[j+1]*math.sin(angle), coordinate[j]*math.sin(angle) + coordinate[j+1]*math.cos(angle)) + coordinate[j+2:]
    return new_coordinates


def shear(coordinates, shearx=0, sheary=0):
    new_coordinates = coordinates.copy()
    for i in range(len(new_coordinates)):
        coordinate = new_coordinates[i]
        for j in range(0,len(coordinate),2):
            coordinate = new_coordinates[i]
            new_coordinates[i] = coordinate[0:j] + (coordinate[j] + shearx*coordinate[j+1], coordinate[j]*sheary + coordinate[j+1])+ coordinate[j+2:]
    return new_coordinates


def scale(coordinates, scale):
    new_coordinates = coordinates.copy()
    xc, yc = centroid(new_coordinates)
    for i in range(len(new_coordinates)):
        coordinate = new_coordinates[i]
        for j in range(0,len(coordinate),2):
            coordinate = new_coordinates[i]
            new_coordinates[i] = coordinate[0:j] + ((coordinate[j]-xc)*scale + xc, (coordinate[j+1]-yc)*scale + yc)+ coordinate[j+2:]
    return new_coordinates


def reflect(coordinates, types="x"):
    if types != "y": 
        types = "x"

    new_coordinates = coordinates.copy()
    for i in range(len(new_coordinates)):
        coordinate = new_coordinates[i]
        for j in range(0,len(coordinate),2):
            coordinate = new_coordinates[i]
            if types == "y":
                new_coordinates[i] = coordinate[0:j] + (-1*coordinate[j], coordinate[j+1])+ coordinate[j+2:]
            else:
                new_coordinates[i] = coordinate[0:j] + (coordinate[j], -1*coordinate[j+1])+ coordinate[j+2:]
    return new_coordinates


def transform1(coordinates): 
    global randomnum
    # get n
    while True: 
        try: 
            n = int(input("Key in n: "))
            break
        except: 
            print("Key in integer only please.")
    
    if randomnum == 1: 
        t.clear()

    # translate into an n by n "table"
    offset = 100
    x = -(n-1)/2
    while x < (n+1)//2: 
        y = -(n-1)/2
        while y < (n+1)//2: 
            tempcoordinates = translation(coordinates, x*offset, y*offset)
            draw(tempcoordinates)
            y += 1
        x += 1


def transform2(coordinates): 
    global randomnum
    # get n
    while True: 
        try: 
            n = int(input("Key in n: "))
            break
        except: 
            print("Key in integer only please.")
    
    if randomnum == 1: 
        t.clear()

    # rotate around origin
    offset = 100
    angle = 360/n
    tempcoordinates = translation(coordinates, 0, offset)
    for i in range(n): 
        tempcoordinates = rotation(tempcoordinates, angle)
        draw(tempcoordinates)


def transform3(coordinates): 
    global randomnum
    # get n
    while True: 
        try: 
            n = int(input("Key in n: "))
            break
        except: 
            print("Key in integer only please.")

    if randomnum == 1: 
        t.clear()

    # scale with pivot in origin
    k = 3
    for i in range(1, n+1): 
        tempcoordinates = scale(coordinates, 1 + (i-1)/k)
        draw(tempcoordinates)


def transform4(coordinates): 
    global randomnum
    if randomnum == 1: 
        t.clear()

    # shear
    tempcoordinates = shear(coordinates, 1, 0)
    tempcoordinates = shear(tempcoordinates, 0, 0.5)

    # draw in four "quadrants" reflected with axises
    draw(tempcoordinates)
    draw(reflect(tempcoordinates, "x"))
    draw(reflect(tempcoordinates, "y"))
    draw(reflect(reflect(tempcoordinates, "x"), "y"))
 


# MAIN PROGRAM
t.tracer(0)
t.hideturtle()
print("Welcome to this Polygon Program")

# COORDINATES INPUT
while True: 
        # Get user choice: 1, 2 or 3
        choice = get_choice()
        coordinates = []

        # Assign choice with appropriate functions
        if choice == 1: 
            coordinates = get_inputs_manual(coordinates)
        elif choice == 2: 
            coordinates = get_inputs_file()
            break
        else: 
            coordinates = get_inputs_click(coordinates)
        
        # Check if want to save
        while True: 
            save = input("Do you want to save your inputs? [Y/N]: ").upper()
            if save in ["Y", "N"]:
                break
            else: 
                print("Only Type Y or N please. Try again.")

        # Retry if they want
        if save == "Y":
            save_input(coordinates)
            break
        else: 
            print("Retry. Here we go again.")

# SHOW POLYGON CENTRED AT ORIGIN
t.clear()
coordinates = translation(coordinates, -centroid(coordinates)[0], -centroid(coordinates)[1])
draw(coordinates)

# TRANSFORMATION
print("\nNow let's draw the polygon!")
randomnum = 1
while True: 
    # Get choice
    while True: 
        try:          
            print("Choose from the following.")
            print("Pattern 1: The polygon is drawn n^2 times in a n by n format")
            print("Pattern 2: The polygon is drawn n times forming a circle around the origin")
            print("Pattern 3: The polygon is enlarged n - 1 multiple times, around the origin")
            print("Pattern 4: The polygon is sheared x and y, then reflected around x-axis, and y-axis, drawn 4 times")
            print("Pattern 0: Exit program")
            transformationChoice = int(input("Key in the pattern you want [1/2/3/4/0]: "))
            if 0 <= transformationChoice <= 4: 
                break
            else: 
                print("Please input integer from 0 to 4 only.\n")
        except: 
            print("Please input 0,1,2,3,4 only.\n")

    if transformationChoice == 0: 
        break
    elif transformationChoice == 1: 
        transform1(coordinates)
    elif transformationChoice == 2: 
        transform2(coordinates)
    elif transformationChoice == 3: 
        transform3(coordinates)
    else: 
        transform4(coordinates)

    randomnum += 1
    print()

print("CLick on the canvas to exit the program. Bye!")
t.exitonclick()
