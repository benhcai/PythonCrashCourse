print("Divide two numbers. q to quit")

while True:
    first_num = input("First num: ")
    if first_num == "q":
        break
    second_num = input("Second num: ")
    if second_num == "q":
        break
    try:
        ans = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("Can't divide by 0!")
    else:
        print(ans)
