import re

def is_strong_password(password, file):
    password = password.lower()
    words = re.findall(r'[a-z]*[a-z]{4,}', password)
    if any(word in file for word in words):
        return False
    return True

if __name__ == "__main__":
    file_with_all_words = open("words.txt").read().lower().split("\n")
    print(is_strong_password("hello.sister asdsadasd2qwerty", file_with_all_words))