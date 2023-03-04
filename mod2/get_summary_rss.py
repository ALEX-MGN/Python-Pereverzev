import sys


def translation_correct_format(byte):
    values = ["B", "KiB", "MiB", "GiB"]
    countTranslation = 0
    while (byte / 1024 > 1):
        byte = byte / 1024
        countTranslation += 1
    return f'{round(byte, 3)} {values[countTranslation]}'

def get_name_file(way):
    with open(way) as file:
        return file.readlines()[1:]

def get_summary_rss(way):
    sum = 0
    way_file = get_name_file(way)
    for lines in way_file:
        sum += int(lines.split()[5])
    return translation_correct_format(sum)

if __name__ == "__main__":
    print(get_summary_rss(sys.stdin))