import sys

def translation_correct_format(byte):
    values = ["B", "KiB", "MiB", "GiB"]
    countTranslation = 0
    while (byte / 1024 > 1):
        byte = byte / 1024
        countTranslation += 1
    return f'{round(byte, 3)} {values[countTranslation]}'

def get_mean_size(data):
    count_file = 0
    sum_value_file = 0
    for lines in data:
        count_file += 1
        sum_value_file += int(lines.split()[4])
    if(count_file == 0):
        return "Файлы не найдены"
    else:
        return translation_correct_format(sum_value_file / count_file)

if __name__ == "__main__":
    print(get_mean_size(sys.stdin.readlines()[1:]))