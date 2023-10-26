'''1
try:
    f = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/ATextFile.txt", "r")
    lines = f.readlines()

    output = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/output.txt", "w")

    for line in lines: 
        for char in line: 
            output.write(char.upper())

    output.close()
    f.close()

except: 
    print("Errorrr")
'''

'''2
f = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/ATextFile.txt", "r")
lines = f.readlines()

output = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/output.txt", "w")
for i in range(len(lines)):
    output.write(f"{i+1} ")
    output.write(lines[i])
'''


'''3
for i in range(-10, 11):
    if i !=0:
        print(f"{1/i:.3f}")
    else: 
        print("DivisionByZero")

for i in range(-10, 11):
    try: 
        print(f"{1/i:.3f}")
    except:
        print("DivisionByZero")
'''

'''4
import math 

f = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/asciioutput.txt", "w")
col = 4
rows = math.ceil(128 / col)



for i in range(rows):
    for j in range(i, 128, rows):
        f.write(f"{j:>3d}:{str(chr(j)):<5s} ")
    f.write("\n")
'''

'''5
f = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/CarTest.txt", "r")
output = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/CarOutput.txt", "w")

lines = f.readlines()
output.write(f"no. fuel(l) distance(km) rate(km/l)\n")

for line in lines: 
    line = line.split()
    if len(line) > 0:
        num = int(line[0])
        liters = float(line[1])
        km = float(line[2])
        rate = km/liters

        output.write(f"{num:^3d} {liters:^7.2f} {km:^12.2f} {rate:^10.2f}\n")
'''

'''6
def convert(i):
    result = ""
    dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",\
            "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    if i.isdigit():
        if len(i) == 1: 
            result = dict[i]
        elif len(i) == 2:
            fdigit = i[0]
            sdigit = i[1]
            if fdigit == "0":
                result = dict[sdigit]
            elif i == "10":
                result = "ten"
            elif i == "11":
                result = "eleven"
            elif i == "12":
                result = "twelve"
            elif i == "13":
                result = "thirteen"
            elif i == "14": 
                result = "fourteen"
            elif i == "15":
                result = "fifteen"
            elif i == "16":
                result = "sixteen"
            elif i == "17":
                result = "seventeen"
            elif i == "18":
                result = "eighteen"
            elif i == "19":
                result = "nineteen"
            elif fdigit == "2":
                result += "twenty"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "3":
                result += "thirty"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "4":
                result += "fourty"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "5":
                result += "fifty"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "6":
                result += "sixty"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "7":
                result += "seventy"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "8":
                result += "eighty"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            elif fdigit == "9":
                result += "ninety"
                if sdigit != "0": 
                    result += " " + dict[sdigit]
            
        else: 
            result = i + " is out of range"
            
    else: 
        result = i + " is not a valid number"

    return result

f = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/Integers.txt", "r")
output = open("C:/Users/ASUS/Desktop/NTU Y1S1/MA1008 Tutorials/outputIntegers.txt", "w")
lines = f.readlines()

for line in lines: 
    line = line.strip()
    output.write(f"{line} = {convert(line)} \n")


'''
