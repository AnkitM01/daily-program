     

text = input("Enter a text\n ")

spam = False

if "make a lots of money" in text:
    spam = True
elif "buy this" in text:
    spam = True
elif "watch this" in text:
    spam = True
elif "subscribe this" in text:  
    spam = True

if spam:
    print("This text is spam")
else:
    print("This is not spam")