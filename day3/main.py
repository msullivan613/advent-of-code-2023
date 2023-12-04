import re
from pathlib import Path


input_text = Path("day3/input.txt").read_text(encoding="utf-8")
lines = input_text.splitlines()


class PartNumber:
    numbers: list[str]
    line_index: int
    start_index: int
    stop_index: int

    def __init__(
        self, numbers: list[str], line_index: int, start_index: int, stop_index: int
    ):
        self.numbers = numbers
        self.line_index = line_index
        self.start_index = start_index
        self.stop_index = stop_index

    def __str__(self):
        return f"Part number: {self.as_int()} - Line: {self.line_index+1} Position: {self.start_index+1}"

    def as_int(self):
        return int("".join(self.numbers))

    def is_real_number(self):
        return any(
            symbol_is_adjacent_to_part_number(symbol, self) for symbol in symbols
        )


class Symbol:
    character: str
    line_index: int
    character_index: int

    def __init__(self, character: str, line_index: int, character_index: int):
        self.character = character
        self.line_index = line_index
        self.character_index = character_index

    def __str__(self):
        return f"Character: {self.character} - Line: {self.line_index+1} Position: {self.character_index+1}"

    def could_be_gear(self):
        return self.character == "*"


def symbol_is_adjacent_to_part_number(symbol: Symbol, part_number: PartNumber):
    return symbol.line_index in [
        part_number.line_index - 1,
        part_number.line_index,
        part_number.line_index + 1,
    ] and symbol.character_index in list(
        range(part_number.start_index - 1, part_number.stop_index + 2)
    )


SYMBOL_REGEX = re.compile(r"[^.\d]")
symbols: list[Symbol] = []
for line_index, line in enumerate(lines):
    for character_index, character in enumerate(line):
        if SYMBOL_REGEX.match(character):
            symbols.append(Symbol(character, line_index, character_index))

print()
for symbol in symbols:
    print(symbol)

NUMBER_REGEX = re.compile(r"\d")
part_numbers: list[PartNumber] = []
for line_index, line in enumerate(lines):
    numbers = []
    start_index = None
    end_index = None
    for character_index, character in enumerate(line):
        if NUMBER_REGEX.match(character):
            numbers.append(character)
            if start_index is None:
                start_index = character_index
            end_index = character_index
        else:
            if numbers:
                part_numbers.append(
                    PartNumber(numbers, line_index, start_index, end_index)
                )
                numbers = []
                start_index = end_index = None
    if numbers:
        part_numbers.append(PartNumber(numbers, line_index, start_index, end_index))
        numbers = []
        start_index = end_index = None

real_part_numbers = [
    part_number for part_number in part_numbers if part_number.is_real_number()
]

print()
for part_number in part_numbers:
    print(f"{part_number} - Real: {part_number in real_part_numbers}")

part_one_total = sum(part_number.as_int() for part_number in real_part_numbers)


def get_adjacent_part_numbers(symbol: Symbol):
    return [
        part_number
        for part_number in part_numbers
        if symbol_is_adjacent_to_part_number(symbol, part_number)
    ]


class Gear:
    symbol: Symbol
    adjacent_part_numbers: list[PartNumber]

    def __init__(self, symbol: Symbol, adjacent_part_numbers: list[PartNumber]):
        if len(adjacent_part_numbers) != 2:
            raise ValueError("Gears only have two adjacent part numbers!")
        self.symbol = symbol
        self.adjacent_part_numbers = adjacent_part_numbers

    def __str__(self):
        return f"Gear - {str(self.symbol)}"

    def get_gear_ratio(self):
        return (
            self.adjacent_part_numbers[0].as_int()
            * self.adjacent_part_numbers[1].as_int()
        )


gears: list[Gear] = []
for symbol in symbols:
    if symbol.could_be_gear():
        try:
            gears.append(Gear(symbol, get_adjacent_part_numbers(symbol)))
        except ValueError:
            pass

print()
for gear in gears:
    print(gear)

part_two_total = sum(gear.get_gear_ratio() for gear in gears)

print(f"\nPart one total: {part_one_total}")
print(f"Part two total: {part_two_total}")
