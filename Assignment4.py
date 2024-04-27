from jes4py import *

# This Is Lab Assignment 4


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


# HTML page
def designHtml():
    with open("assignment4.html", "wt") as file:
        # Write The Doctype decleration and the head
        file.write(
            """<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                        <title>Muhannad Mojalled</title>
                    </head>
                <body>"""
        )

        # Write the image tag
        file.write(
            """<!-- This is the Image -->
            <img
            src="https://upload.wikimedia.org/wikipedia/ar/archive/d/d9/20231125191228%21Kaau_logo.jpg"
            ,
            height="100"
            ,
            width="100"
            ,
            />"""
        )

        # write the Description and the links
        file.write(
            """ <!-- This is Description about me-->
            <h2>
                My name is Muhannad Mojalled<br />
                I am a Information Technology student <br />
                at king abdulaziz university
            </h2>
            <!-- This is Hyper Link -->
            <a href="https://www.kau.edu.sa/Home.aspx?lng=arl">Kau Website</a>
            <h3>Kau Collages</h3>"""
        )

        # write the lists
        file.write(
            """<ol>
                <!-- This is Ordered list-->
                    <li>Faculty of Computing and Information Technology</li>
                        <ul>
                        <!-- This is unordered list -->
                            <li>CS</li>
                            <li>IT</li>
                            <li>IS</li>
                        </ul>
                    <li>Faculty of Economics and Administration.</li>
                    <li>Islamic Economics Institute</li>
                </ol>"""
        )

        # write the table and close the hmtl tag
        file.write(
            """
            <!-- this is the table -->
            <table border="1" cellpadding="5">
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>Country</th>
                <th>City</th>
            </tr>
            <tr>
                <td>Muhannad</td>
                <td>22</td>
                <td>Saudi Arabia</td>
                <td>Jeddah</tr>
            </tr>
            <tr>
                <td>Ziyad</td>
                <td>22</td>
                <td>Saudi arabia</td>
                <td>Jeddah</td>
            </tr>
            </table>
        </body>
        </html>
"""
        )


designHtml()
