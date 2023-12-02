import re

part_one_total = 0
part_two_total = 0
with open("day1/input.txt", "r", encoding="utf-8") as input_file:
    input_text = input_file.read()

NUMBERS_AS_STRINGS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_first_number(line: str, strings_as_numbers: bool) -> int:
    characters = ""
    for character in line:
        if re.match(r"\d", character):
            return int(character)
        if strings_as_numbers:
            characters += character
            for number_as_string, number in NUMBERS_AS_STRINGS.items():
                if number_as_string in characters:
                    return number

def get_last_number(line: str, strings_as_numbers: bool) -> int:
    characters = ""
    for character in reversed(line):
        if re.match(r"\d", character):
            return int(character)
        if strings_as_numbers:
            characters = character + characters
            for number_as_string, number in NUMBERS_AS_STRINGS.items():
                if number_as_string in characters:
                    return number

def get_line_value(line: str, strings_as_numbers: bool):
    first = get_first_number(line, strings_as_numbers)
    last = get_last_number(line, strings_as_numbers)
    print(f"First number: {first}\nLast number: {last}")
    return int(f"{first}{last}")

for line in input_text.splitlines():
    print()
    print(f"Line: {line}")
    part_one_total += get_line_value(line, False)

print(f"\nPart one total: {part_one_total}")

for line in input_text.splitlines():
    print()
    print(f"Line: {line}")
    part_two_total += get_line_value(line, True)
print(f"\nPart two total: {part_two_total}")
    
    
