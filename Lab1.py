from jes4py import *


# Example 1
def example1():
    f = pickAFile()
    print(f)
    file = open(f, "rt")
    contents = file.read()
    print(contents)
    file.close()


# Example 2
def example2():
    f = pickAFile()
    print(f)
    file = open(f, "rt")
    contents = file.readlines()
    print(contents)


# Example 3
def example3():
    path = pickAFile()

    with open(path, "w") as fW:
        fW.write("My name is Muhannad. ")
        fW.write("I am an information tecnology student.\n")
        fW.write("And now we are done.\n\nThe End.")

    with open(path, "rt") as fR:
        print(fR.read())


# Exercise 1
def exercise1():
    with open("Lab2.py", "wt") as fW:
        fW.write(
            "print ('Welcome to Jython programing language! This is Lab 2*** Happy to be her')"
        )
    with open("Lab2.py", "rt") as fR:
        contents = fR.read()
        with open("Copy.txt", "wt") as fW:
            fW.write(contents)


# Exercise 2
def exercise2():
    ls = []
    with open("Copy.txt", "rt") as fW:
        text = fW.readline()
        index = text.find("This")
        sentence = "This is Lab 2***"
        length = len(sentence)
        if sentence in text:
            newText = text[index : index + length]
            print(f"Sentence was found: {newText}")
        else:
            print("Sentence was not found")


# Exercise 3
def exercise3():
    with open("Lab2.py", "wt") as fW:
        fW.write(
            "print (“Welcome to Jython programing language! This is Lab 2*** Happy to be here”)"
        )
    ls = []

    with open("Lab2.py", "rt") as fW:
        text = fW.readline()
        index = text.find("! This")
        sentence = "! This is Lab 2*** "
        length = len(sentence)
        if sentence in text:
            newText = text[index : index + length]
            print(f"Sentence was found: {newText}")
            with open("Copy.txt", "wt") as fW:
                fW.write(newText)
        else:
            print("Sentence was not found")


# Exercise 4
def exercise4():
    target_word = input("Please enter the word: ")
    with open("Ex4.txt", "rt") as file:
        contents = file.read()
        sentences = contents.split(".")
        for sentence in sentences:
            if target_word.lower() in sentence.lower():
                print(sentence.strip() + ".")


# Exercise 5
def exercise5():
    with open("Ex5.txt", "rt") as file:
        first_three_lines = file.readlines()[:3]
        print(first_three_lines)
