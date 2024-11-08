import time
import math
import turtle as t

def get_choice():
    # Get user choice
    while True: 
        choice = input("Key in the number you want:\n   0: Exit\n   1: Manual Input\n   2: File Input\n   3: Point and Click\nYour Choice: ")
        try: 
            if choice in ["0", "1", "2", "3"]:
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
    global exited
    while True: 
        coordinates = []
        while True: 
            print("Enter nothing to exit")
            try: 
                infile_name = input("Key in input file name: ") + ".txt"

                if infile_name == ".txt":
                    exited = True
                    break

                infile = open(infile_name, "r")
                break
            except:
                print("File not found. Try again.")
        
        if exited: 
            break

        infile_lines = infile.readlines()
        t.color(infile_lines[0].strip())
        try:
            for i in range(1, len(infile_lines)):
                if infile_lines[i] != "" and infile_lines[i] != "\n":
                    line = [float(x) for x in infile_lines[i].strip().split(" ")]
                    coordinates.append(tuple(line))
            break
        except: 
            print("Wrong file format.")

    return coordinates


def xmat(mat1, mat2):
    row_mat1, column_mat1, row_mat2, column_mat2 = len(mat1), len(mat1[0]), len(mat2), len(mat2[0])
    res = []
    if column_mat1 == row_mat2: 
        for i in range(row_mat1) :
            temp = []
            for j in range(column_mat2):
                sum = 0
                l = 0
                for k in range(column_mat1):
                    sum += mat1[i][k]*mat2[l][j]
                    l += 1
                temp.append(sum)
            res.append(temp)
    return res

    
click = False
def waitforclick():
    print("Waiting for click\n")
    global click

    t.update()
    click = False
    while not click: 
        t.update()
        time.sleep(.05)
    
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
            print(f"Line/curve {N}")
            try: 
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
    output_name = input("Key in output file name: ") + ".txt"
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


def transform(name, coordinates, xt=0, yt=0, angle=0, scale=0, shearx=0, sheary=0, types="x"):
    new_coordinates = coordinates.copy()
    if name == "translation":
        transformationmat = [[1,0,xt], [0,1,yt], [0,0,1]]
    elif name == "rotation":
        angle *= math.pi / 180
        transformationmat = [[math.cos(angle),-math.sin(angle),0], [math.sin(angle),math.cos(angle),1], [0,0,1]]
    elif name == "shear":
        transformationmat = [[1,shearx,0], [sheary,1,0], [0,0,1]]
    elif name == "scale":
        transformationmat = [[scale,0,0], [0,scale,0], [0,0,1]]
    elif name == "reflection":
        if types != "y": 
            types = "x"
        if types == "x": 
            transformationmat = [[1,0,0], [0,-1,0], [0,0,1]]
        else: 
            transformationmat = [[-1,0,0], [0,1,0], [0,0,1]]
    elif name == "origined":
        xc, yc = centroid(new_coordinates)
        transformationmat = [[1,0,-xc], [0,1,-yc], [0,0,1]]
    else: 
        transformationmat = [[1,0,0], [0,1,0], [0,0,1]]

    for i in range(len(new_coordinates)): 
        coordinate = new_coordinates[i] = list(new_coordinates[i])
        for j in range(0, len(coordinate), 2):
            res = xmat(transformationmat, [[coordinate[j]], [coordinate[j+1]], [1]])
            coordinate[j], coordinate[j+1] = res[0][0], res[1][0]  
        new_coordinates[i] = coordinate
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
            tempcoordinates = transform("translation", coordinates, xt=x*offset, yt=y*offset)
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
    tempcoordinates = transform("translation", coordinates, xt=0, yt=offset)
    for i in range(n): 
        tempcoordinates = transform("rotation", tempcoordinates, angle=angle)
        draw(tempcoordinates)


def transform3(coordinates): 
    global randomnum
    # get n
    while True: 
        try: 
            n = int(input("Key in n: "))
            angle = int(input("Key in angle: "))
            break
        except: 
            print("Key in integer only please.")

    if randomnum == 1: 
        t.clear()

    # scale with pivot in origin
    k = 3
    tempcoordinates = coordinates
    for i in range(1, n+1): 
        tempcoordinates = transform("scale", tempcoordinates, scale = 1 + (i-1)/k)
        draw(tempcoordinates)
        tempcoordinates = transform("rotation", tempcoordinates, angle=angle)
        draw(tempcoordinates)


def transform4(coordinates): 
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

    # shear
    tempcoordinates = transform("translation", coordinates, xt=-coordinates[0][0], yt=-coordinates[0][1])
    tempcoordinates = transform("shear", tempcoordinates, shearx=1, sheary=0)
    tempcoordinates = transform("shear", tempcoordinates, shearx=0, sheary=0.5)
    tempcoordinates = transform("translation", coordinates, xt=coordinates[0][0], yt=coordinates[0][1])
    
    k = 3
    for i in range(1,n+1): 
        tempcoordinates = transform("scale", tempcoordinates, scale = 1 + (i-1)/k)
        draw(tempcoordinates)
        tempcoordinates = transform("reflection", tempcoordinates, types="x")
        draw(tempcoordinates)
        tempcoordinates = transform("reflection", tempcoordinates, types="y")
        draw(tempcoordinates)
        tempcoordinates = transform("reflection", tempcoordinates, types="x")
        draw(tempcoordinates)
    

def custom_transform(coordinates): 
    polygons = [coordinates]
    t.clear()
    draw(polygons[-1])

    customchoice = ""
    while True: 
        if customchoice == 0: 
            while True: 
                want_to_save = input("Do you want to save the last polygon [Y/N]:").upper()
                if want_to_save in ["Y", "N"]:
                    break
                print("Please only enter Y or N.")
            
            if want_to_save == "Y":
                save_input(polygons[-1])
                break
            else: 
                break

        print("\nChoose from the following.")
        print("[0]: Exit")
        print("[1]: translation")
        print("[2]: rotation")
        print("[3]: shear")
        print("[4]: scale")
        print("[5]: reflection")
        print("[6]: center in origin")
        print("[7]: show current polygon")
        print("[8]: reset to previous polygon")
        print("[9]: reset to original polygon")
        print("[10]: clear board")
        
        while True: 
            try: 
                customchoice = int(input("What's your choice: "))
                if 0 <= customchoice <= 10: 
                    break
                print("Please enter integer from 0 to 10 only.")
            except: 
                print("Please enter integer only.")
        
        # translation
        if customchoice == 1: 
            while True: 
                try: 
                    xt = float(input("x-translation: "))
                    yt = float(input("y-translation: "))
                    break
                except: 
                    print("Please enter a valid number")
            new_polygon = transform("translation",polygons[-1], xt=xt, yt=yt)
            polygons.append(new_polygon)    
        
        # rotation
        elif customchoice == 2: 
            while True: 
                try: 
                    angle = float(input("Key in the angle you want (rotate around origin): "))
                    break
                except:
                    print("Please enter a valid number.")
            new_polygon = transform("rotation", polygons[-1], angle=angle)
            polygons.append(new_polygon)
        
        # shear
        elif customchoice == 3: 
            while True: 
                try: 
                    shearx = float(input("Key in x-shear factor: "))
                    sheary = float(input("Key in y-shear factor: "))
                    break
                except: 
                    print("Please enter a valid number.")
            new_polygon = transform("shear", polygons[-1], shearx=shearx, sheary=sheary)
            polygons.append(new_polygon)

        # scale
        elif customchoice == 4: 
            while True: 
                try: 
                    scale = float(input("Key in scale factor: "))
                    break
                except: 
                    print("Please enter a valid number.")
            new_polygon = transform("scale", polygons[-1],scale=scale)
            polygons.append(new_polygon)

        # reflection
        elif customchoice == 5: 
            while True: 
                types = input("Key in axis of reflection [x/y]: ").lower()
                if types in ["x", "y"]:
                    break
                print("Key in x or y only.")
            new_polygon = transform("reflection", polygons[-1], types=types)
            polygons.append(new_polygon)
        
        # origined
        elif customchoice == 6: 
            new_polygon = transform("origined", polygons[-1])
            polygons.append(new_polygon)
        
        # show current
        elif customchoice == 7: 
            draw(polygons[-1])
        
        # reset to previous
        elif customchoice == 8: 
            if len(polygons) != 1: 
                polygons.pop()
                t.clear()
                draw(polygons[-1])

        # reset to initial
        elif customchoice == 9: 
            polygons = [polygons[0]]
            t.clear()
            draw(polygons[-1])
        
        # clear board
        elif customchoice == 10: 
            t.clear()
        


        
    


# MAIN PROGRAM
t.tracer(0)
t.hideturtle()
exited = False

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
        elif choice == 3: 
            coordinates = get_inputs_click(coordinates)
        else: 
            exited = True
            break
        
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
            t.clear()
            print("Retry. Here we go again.")

# SHOW POLYGON CENTRED AT ORIGIN
if exited: 
    print("BYEE")
else: 
    t.clear()
    coordinates = transform("origined", coordinates)
    draw(coordinates)

    
    # TRANSFORMATION
    print("\nNow let's draw the polygon!")
    randomnum = 1
    while True: 
        # Get choice
        while True: 
            try:          
                print("Choose from the following.")
                print("[0]: Exit program")
                print("[1]: The polygon is drawn n^2 times in a n by n format")
                print("[2]: The polygon is drawn n times forming a circle around the origin")
                print("[3]: The polygon is enlarged n-1 times around the origin while getting rotated")
                print("[4]: The polygon is sheared x and y from the first point, then enlarged n-1 times and reflected to all quadrants")
                print("[5]: Do my own transformation")
                transformationChoice = int(input("Key in the pattern you want [0/1/2/3/4/5]: "))
                if 0 <= transformationChoice <= 5: 
                    break
                else: 
                    print("Please input integer from 0 to 5 only.\n")
            except: 
                print("Please input integer only.\n")

        if transformationChoice == 0: 
            break
        elif transformationChoice == 1: 
            transform1(coordinates)
        elif transformationChoice == 2: 
            transform2(coordinates)
        elif transformationChoice == 3: 
            transform3(coordinates)
        elif transformationChoice == 4: 
            transform4(coordinates)
        else: 
            custom_transform(coordinates)
            break
        
        randomnum += 1
        print()

    print("CLick on the canvas to exit the program. Bye!")
    t.exitonclick()
