filename = 'pi_million_digits.txt'

with open(filename) as fo:
    lines = fo.readlines()
    
pi_string = ""
for l in lines:
    pi_string += l.strip()

def get_date_position(date, pi):
    target = pi 
    input = date 
    for i, c in enumerate(target):
        if c == input[0] and i + len(input) <= len(target):
            target_snippet = target[i:i+len(input)] 
            if target_snippet == input:
                return f"It's found at position {i-1} in the decimals of pi"
    return "Not found"

birthday = input("Enter your birthday: ")

if birthday in pi_string:
    print("FOUND: Your birthday is in the first million digits of pi")
    print(get_date_position(birthday, pi_string))
else:
    print("It's not in the first 1 million")

