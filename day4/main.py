import re
from pathlib import Path

input_text = Path("day4/input.txt").read_text(encoding="utf-8")
part_one_total = 0

CARD_NUMBER_REGEX = re.compile(r"^Card\s+(?P<card_number>\d+):")
num_of_matches_per_card_number: dict[int, int] = {}


def get_numbers_in_string(string: str):
    return {number.strip() for number in string.split()}


for line in input_text.splitlines():
    print(f"\n{line}")
    card_number = int(CARD_NUMBER_REGEX.search(line).group("card_number"))
    line = line.split(":")[1]
    winning_numbers, drawn_numbers = line.split("|")
    winning_numbers = get_numbers_in_string(winning_numbers)
    drawn_numbers = get_numbers_in_string(drawn_numbers)
    print(f"Winning numbers: {winning_numbers}")
    print(f"Drawn numbers: {drawn_numbers}")
    matches = winning_numbers.intersection(drawn_numbers)
    print(f"Matches: {matches}")
    num_of_matches_per_card_number[card_number] = len(matches)
    if matches:
        points = pow(2, len(matches) - 1)
        print(f"Points from this card: {points}")
        part_one_total += points


print(f"\nPart one total: {part_one_total}\n")

num_of_each_card_number = {
    card_number: 1 for card_number in num_of_matches_per_card_number
}
for card_number, num_of_matches in num_of_matches_per_card_number.items():
    copies_of_card = num_of_each_card_number[card_number]
    created_card_numbers = list(
        range(card_number + 1, card_number + num_of_matches + 1)
    )
    print(
        f"{copies_of_card} copies of card #{card_number} - {num_of_matches} matches - Creates {copies_of_card} copies of {created_card_numbers}"
    )
    for created_card_number in created_card_numbers:
        num_of_each_card_number[created_card_number] += copies_of_card

total_cards = sum(num_of_each_card_number.values())
print(f"\nPart two total: {total_cards}")
