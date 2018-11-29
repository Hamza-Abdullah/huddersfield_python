import random
import sys


def random_name():
    names = ["Hamza", "Rowan", "Atkinson", "Jackie", "Chan", "Tom", "Hardy"]
    selection = random.sample(names, 1)[0]
    return selection


def random_phrase():
    phrases = ["Maybe", "Tell me more", "I'm pleased to hear that", "Possibly", "Good to know"]
    selection = random.sample(phrases, 1)[0]
    return selection


def check_email(email, domain):
    if email.count("@") != 1:
        return False

    if domain[0] == "." or domain[-1] == ".":
        return False

    if email[0] == "@":
        return False

    if email[(email.find('@') + 1):] != domain:
        return False

    return True


def get_email_name(email):
    return email[:email.find("@")]


def word_in_question(question, word):
    if word in question:
        return True
    else:
        return False


email = input("Please enter your University of Poppleton email address: " )
if check_email(email, "pop.ac.uk") is False:
    sys.exit("Invalid email.")
name = get_email_name(email)
operator = random_name()
print("Hi " + name + ", my name is " + operator + " and I'll be helping you today.")

while True:
    question = input("What is your question?: ")
    question = question.upper()
    disconnect = random.randint(0, 100)
    if question == "GOODBYE" or disconnect < 16:
        print("Disconnected")
        break
    elif word_in_question(question, "LIBRARY") is True:
        print("The library is closed today.")
    elif word_in_question(question, "WIFI") is True:
        print("Wifi is excellent across the campus.")
    elif word_in_question(question, "DEADLINE") is True:
        print("Your deadline has been extended by two working days.")
    else:
        print(random_phrase())
