def matrix():
    keypad = [ [1,2,3,],[4,5,6,],[7,8,9],["*",0,"#"] ]

    for row in keypad:
        for col in row:
            print(col, end="")
        print()

matrix()