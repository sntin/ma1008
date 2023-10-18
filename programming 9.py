# Programming 9

'''1
def check_digit(string, num):
    if num < len(string):
        return string[num].isdigit()    
    return False
'''

'''2
import math
def area(float1, float2, string = "cir"):
    if string == "cir":
        A = math.pi * float1 ** 2
    elif string == "rect":
        A = float1 * float2
    elif string == "tri":
        A = float1 * float2 / 2
    else:
        return -1

    return A
'''

'''3
def insert(Birthday, ic, btuple):
    if ic not in Birthday:
        Birthday[ic] = btuple
'''

'''4 
def check_birthday(Birthday, ic, btuple):
    if ic not in Birthday:
        return 2
    elif Birthday[ic] == btuple:
        return 1
    else:
        return 3
'''

'''5
def exchangeAmount(amount, rate, mode = "T"):
    if mode == "T":
        return amount / rate
    elif mode == "F":
        return amount * rate

rate = 3.05
mode = input("To or from Singapore dollar (T/F): ")
if mode == "T":
    amount = float(input("Amount in Ringgit Malaysia: "))
    exchangeAmount = exchangeAmount(amount, rate, mode)
    print(f"RM{amount:.2f} = S${exchangeAmount:.2f}")
elif mode == "F":
    amount = float(input("Amount in Singapore dollar: "))
    exchangeAmount = exchangeAmount(amount, rate, mode)
    print(f"S${amount:.2f} = RM{exchangeAmount:.2f}")
'''

        


    




