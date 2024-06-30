# Write your solution here
while True:
    editor = input("editor: ")
    if editor.lower() == "visual studio code":
        break
    if editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
print("an excellent choice!")