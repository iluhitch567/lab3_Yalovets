def ex2():
    john = 3
    mary = 5
    adam = 6

    print(f"{john}, {mary}, {adam}")

    total_apple = john + mary + adam

    print("Total apple:", total_apple)
    print("________________________________")


def ex3():
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
    print("________________________________")

def ex4():
    x = int(input("input X: "))
    x = float(x)

    y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
    print("y =", y)
    print("________________________________")

def ex5():
    # this program computes the number of seconds in a given number of hours

    a = 2  # number of hours
    seconds = 3600

    print("Hours: ", a)
    print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
    # this is the end of the program that computes the number of seconds in 3 hour
    print("________________________________")

def ex6():
    # input a float value for variable a here
    a = float(input("Input float 'a': "))

    # input a float value for variable b here
    b = float(input("Input float 'b': "))

    # output the result of addition here
    print(a + b)

    # output the result of subtraction here
    print(a - b)

    # output the result of multiplication here
    print(a * b)

    # output the result of division here
    print(a / b)
    print("\nThat's all, folks!")

    print("________________________________")

def ex7():
    x = float(input("X: "))

    sum = x + 1 / x

    for i in range(0, 3, 1):
        sum = 1 / sum
        print(sum)
    print("Y =", sum)
    print("________________________________")

def ex8():
    h = int(input("Start hours: "))
    m = int(input("Start minutes: "))
    d = int(input("Event duration minutes: "))

    sum = (h * 60) + m + d

    print(f"{sum // 60}:{sum % 60}")
    print("________________________________")

ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()
