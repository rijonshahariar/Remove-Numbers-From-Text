text = input("Enter Text: ")
result = ''.join([i for i in text if not i.isdigit() and i.isalnum()])
print(result)
