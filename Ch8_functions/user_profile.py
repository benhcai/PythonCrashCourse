def build_profile(first, last, **user_info):
    """Build a dictonary containing first and last name, as well as,
    a variety of user information
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, val in user_info.items():
        profile[key] = val
    return profile

user1 = build_profile('jen', 'wonder', power='flying', universe='dc', color='red')

print(f"Our person {user1['first_name']} {user1['last_name']} is good at:")
for key, val in user1.items():
    if key != 'first_name' and key != 'last_name':
        print(f"And has {key} to be {val}")

