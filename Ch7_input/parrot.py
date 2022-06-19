count = 0
count_limit = 5
message = ""
# flag
active = count < count_limit
while active:
    count += 1
    message = input("Type message or quit() ")
    if message == "quit()":
        break
    print(message + ' - ' + str(count) + "/" + str(count_limit))
    
