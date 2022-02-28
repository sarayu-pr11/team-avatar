import random

number = random.randint(1,100)
if (number % 2) == 0:
    print("{0} is even".format(number))
else:
    print("{0} is odd".format(number))


if number > 1:
    for i in range(2, int(number/2)+1):
        if (number % 1) == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")
else:
    print(number, "is not a prime number")