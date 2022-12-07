vowels="aeiouAEIOU"
while True:
    char1=input("vowel, or 9 to quit: ")
    if char1.isalpha() or char1=="9":
        if char1=="9":
            break
        if char1 in vowels:
            print("vowel")
        else:
            print("not vowel")
    else:
        print("wrong input")