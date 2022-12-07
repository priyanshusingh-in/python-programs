#input sequence from user convert sequence to dictionary and print in python?
s = set()
i = 0
while True:
    user_input = input("enter words: ")
    for words in user_input.strip().split():
        words_from_list = words.strip().split()
        for x in words_from_list:
            s.add(x)
    for i in s:
        print(i)
    