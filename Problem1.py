def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    count = len(name1) + len(name2)

    if count == 0: return "Not compatible! Single forever </3"
    flames = {"F": "Friendship", "L": "Love", "A": "Affection", "M": "Marriage", "E": "Enemy", "S": "Sibling"}
    
    keys = list(flames.keys())
    while len(keys) > 1:
        index = (count % len(keys)) - 1
        if index >= 0:
            keys.pop(index)
            keys = keys[index:] + keys[:index]  # rotate list
        else: keys.pop() 
    return flames[keys[0]]

your_name = input("Enter your name: ")
partner_name = input("Enter partner's name: ")
print("Result:", flames_game(your_name, partner_name))