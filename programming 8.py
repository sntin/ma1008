'''1
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

v1 = (x1, y1)
v2 = (x2, y2)

def vecSum(v1, v2):
        return (v1[0] + v2[0], v1[1] + v2[1])
'''

'''2
import math

g = 9.81
def calcD(v, y, ang):
    d = v**2 / (2 * g) * (1 + math.sqrt(1 + 2*g*y / (v**2 * (math.sin(ang))**2))) * math.sin(2 * ang)
    return d

print(d)
'''

''' 3
import random
def rollDice():
    return random.randint(1,6)

def samensum(d1, d2, d3):
    if d1 == d2 == d3:
        return "same"
    else:
        return d1 + d2 + d3
    
d1 = rollDice()
d2 = rollDice()
d3 = rollDice()

status = samensum(d1, d2, d3)
if status == "same":
    print("Jackpot")
elif status >= 11:
    print("Big")
else:
    print("Small")

'''

''' 4
def days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30
    
day = int(input("Enter the day of the month: "))
month = int(input("Enter the month: "))

totaldaysofmonthsbeforethemonth = 0
for i in range(1, month):
    totaldaysofmonthsbeforethemonth += days(i)

totaldays = totaldaysofmonthsbeforethemonth + day
print(f"The number of days from 1/1/2023 to {day}/{month}/2023 is {totaldays}")

'''


'''5
def add_income(revenue, shop, income):
    if shop in revenue: 
        revenue[shop] += income
    else:
        revenue[shop] = income

revenue = {"Jurong":1620.55, "Bedok":2598.60, "Sengkang":1886.40}
for key in revenue: 
    print(f"{key}: {revenue[key]}")
'''



