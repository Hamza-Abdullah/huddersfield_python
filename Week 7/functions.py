import random


def random_string():
    answers = ["Yes", "No", "Maybe", "Ni!"]
    selection = random.sample(answers, 1)[0]
    print(selection)


random_string()


def check_email(email):
    domain = email[email.find("@") + 1:]
    if email.count("@") != 1 or email[0] == "@" or "." not in domain or domain[0] == ".":
        print(email + " isn't valid at " + domain)
    else:
        print(email + " is valid at " + domain)


def get_email_name(email):
    print(email[:email.find("@")])


def word_in_question(question, word):
    if word in question:
        return True
    else:
        return False


get_email_name("hello@mail.com")
print(word_in_question("How are you?", "you"))