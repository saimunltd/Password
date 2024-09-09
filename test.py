import random


def password_generate():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "1234567890"
    symboles = "~!@#$%^&*()_-=/*-+.></?}{[]}"

    all_chars = lower + upper + number + symboles

    lengeth = int(input("Enter your password length\n: "))

    password = "".join(random.sample(all_chars,lengeth))
    print("Generated password:",password)
if __name__ == "__main__":
    password_generate() 