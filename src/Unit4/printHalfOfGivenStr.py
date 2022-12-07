text='python'
length=len(text)
if length%2==0:
    print(text[ : length//2])
else:
    print(text[length//2 : -1])
