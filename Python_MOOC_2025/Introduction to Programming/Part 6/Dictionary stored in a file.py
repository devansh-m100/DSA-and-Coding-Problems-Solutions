# Write your solution here
try:
    with open("dictionary.txt") as dictionary:
        entries = dictionary.readlines()

except FileNotFoundError:
    entries = []

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        entry = f"{finnish_word} - {english_word}\n"
        entries.append(entry)
        with open("dictionary.txt", "a") as dictionary:
            dictionary.write(entry)
        print("Dictionary entry added")
    elif function == "2":
        search_term = input("Search term: ")
        for entry in entries:
            if search_term in entry:
                print(entry.strip())
    elif function == "3":
        print("Bye!")
        break
