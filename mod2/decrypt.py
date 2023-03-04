import sys

def descrypt(string):
    new_string = ""
    index = 0
    while(index < len(string) - 1):
        if(string[index] != "."):
            new_string += string[index]
        elif(string[index] == "." and string[index + 1] == "."):
            new_string = new_string[:-1]
            index += 1
        index += 1
    return new_string + string[-1] if string[-1] != "." else ""

if __name__ == "__main__":
    print(descrypt(sys.stdin.read()))
