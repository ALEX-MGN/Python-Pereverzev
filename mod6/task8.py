import re

file_with_all_words = "\n" + open("words.txt").read().lower() + "\n"
dictionary = {"2":"[a|b|c]",
              "3":"[d|e|f]",
              "4":"[g|h|i]",
              "5":"[j|k|l]",
              "6":"[m|n|o]",
              "7":"[p|q|r|s]",
              "8":"[t|u|v]",
              "9":"[w|x|y|z]"}

def my_t9(combination):
    pattern = "[\n]"
    for number in combination:
        pattern += dictionary[number]
    pattern += "[\n]"
    return re.findall(pattern, file_with_all_words)

combination = "22736368"
print(*my_t9(combination))
