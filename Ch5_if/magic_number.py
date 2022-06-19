try_limit = 5
current_try = 0
while current_try < try_limit:
    try:
        user_input = input("choose number 10: ")
        print(user_input, user_input.isnumeric(), int(user_input) == 10, user_input.isnumeric() and int(user_input) == 10)
        if (user_input.isnumeric() == True and int(user_input) == 10):
            print('you have chosen 10')
            break
        else:
            print('not 10')
    except:
        pass
    current_try += 1
    print("error", current_try, "/", try_limit)
