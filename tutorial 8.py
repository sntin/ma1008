# Tutorial
# 1. def name(param): block return
# 2. make codes easier to read, can reuse it, divide and conquer

'''3. 
def Func(num):
    total = 0
    while num > 0:
        total = total + num*(num-1)
        num = num - 1
    return total

n(n-1) + ... + 3x2 + 2x1 + 1x0
''' 

'''4
x = Func(5) --> x = 40
x = Func(5.5) --> x = 53.5
x = Func('5') --> x = error
x = Func() --> x = error
'''

'''5
number = 50
def Func(number):
    print(number)
    number = 2
    print(number)

Func(number) # 50 2
print(number) # 50
'''
'''6
confusing = 0
def do_work(num):
   confusing = -50
   confusing += num
   print("confusing in do_work is ", confusing)
   return confusing

confusing = 100
print("confusing in main is ", confusing)
confusing += do_work(confusing) 
print("confusing in main is ", confusing)
confusing += do_work(confusing)
print("confusing in main is ", confusing)
confusing += do_work(confusing)

# confusing in main is 100
# confusing in do_work is 50
# confusing in main is 150
# confusing in do_work is 100
# confusing in main is 250
# confusing in do work is 200
'''

'''7
def isLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False
'''

'''8
    def vecSum(v1, v2):
        return (v1[0] + v2[0], v1[1] + v2[1])
'''



