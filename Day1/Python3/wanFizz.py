'''
 * @author: SyahirahWanMin
 * @date: 05/10/2020
'''

n = int(input("Please enter the limit : "))
for x in range(1, n+1):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
