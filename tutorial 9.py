# Tutorial 9

'''1
i. Before the function is called
ii. yes
iii. it is a parameter where if you dont use it, it will have a default value.
You can create it by (name = default value) and it must be after the non optional
parameter
iv. as many as you want
v. Yes, but you need to specify the non optional parameters first before the optional
'''

'''2
def func(p1, p2 = 0.0, p3 = "z", p4 = 100):
i. c = func(12, 7.2) correct
ii. func(0, p3 = "abc") correct
iii. func(10) correct
iv. func("xyz", "12.3", p4 = 5) correct
v. func(10, p4 = 2, p3 = "alpha", p2 = 1.0) correct
vi. func(p4 = 2, p3 = "alpha", p2 = 1.0, 10) incorrect
'''

'''3
def total(num):
    sum += num
    
sum = 0
for i in range(1, 5):
    total(i)
print(sum)

0 because changes is not reflected in the main program
'''

'''4
def output(message, times = 1):
    print(message*times)
    
output("Computational Thinking")
output("Very easy", 3)

Computional Thinking
Very easyVery easyVery easy
'''

'''5
a = 1
b = 2
c = 3
d = 123.4 

def add(a, b, c=4):
    global d
    a += b
    b += 1
    d += a
    print(a, b, c)
    return a+b+c

for i in range(1, 4):
    a = add(i, b)
    print(a, b, c)
print(d)

3 3 4
10 2 3
4 3 4
11 2 3
5 3 4
12 2 3
135.4

if global d is removed then d will still be 123.4
'''

'''6
def checkmarks(marks, passes):
    for i in range(len(marks)):
        if 47 <= marks[i] < 50:
            marks[i] = 50
            passes += 1
            
marklist = [44, 68, 56, 98, 47, 28, 88, 75, 49, 66]

passes = 6
checkmarks(marklist, passes)

print("New mark list: ", marklist)
print("The new number of passes: ", passes)

New mark list: [44, 68, 56, 98, 50, 28, 88, 75, 50, 66]
The new number of passes: 6

marklist changes because list is mutable and mutable changes will be reflected in main function
passes is an integer so it is immutable and must be returned if it wants to be used in
main function
'''




































