fav_langs = {
        'ben': ['js', 'ruby'],
        'sarah': ['c', 'c++'],
        'ryan': ['java', 'rust'],
        'steve': ['python'],
        'albert': ['assembly', 'dog'],
        'phil': ['python']
        }

first_langs = {}

for name, langs in fav_langs.items():
    first_langs[name] = langs[0]

for name in set(sorted(first_langs.values())):
    print('Thanks ' + name.title())

print('-----')

for name, langs in fav_langs.items():
    for lang in langs:
        print(name + ' ' + lang)
