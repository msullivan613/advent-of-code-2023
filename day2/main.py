import re
from pathlib import Path

GAME_REGEX = re.compile(r"^Game (?P<game_id>\d+):.*$")
RED_REGEX = re.compile(r"(?P<count>\d+) red")
GREEN_REGEX = re.compile(r"(?P<count>\d+) green")
BLUE_REGEX = re.compile(r"(?P<count>\d+) blue")
CUBES = {"red": 12, "green": 13, "blue": 14}


input_text = Path("day2/input.txt").read_text(encoding="utf-8")

part_one_total = 0
part_two_total = 0

for game in input_text.splitlines():
    print(f"\n{game}")
    minimum_required = {"red": 0, "green": 0, "blue": 0}
    game_id = int(GAME_REGEX.match(game).group("game_id"))
    valid_game = True
    for pull in game.split(":")[1].split(";"):
        print(f"\nPull: {pull}")
        red_match = RED_REGEX.search(pull)
        green_match = GREEN_REGEX.search(pull)
        blue_match = BLUE_REGEX.search(pull)
        red_count = int(red_match.group("count")) if red_match else 0
        green_count = int(green_match.group("count")) if green_match else 0
        blue_count = int(blue_match.group("count")) if blue_match else 0
        print(
            f"Red count: {red_count} - Green count: {green_count} - Blue count: {blue_count}"
        )
        if minimum_required["red"] < red_count:
            minimum_required["red"] = red_count
        if minimum_required["blue"] < blue_count:
            minimum_required["blue"] = blue_count
        if minimum_required["green"] < green_count:
            minimum_required["green"] = green_count
        if (
            red_count > CUBES["red"]
            or blue_count > CUBES["blue"]
            or green_count > CUBES["green"]
        ) and valid_game:
            print("Impossible game!")
            valid_game = False
    if valid_game:
        part_one_total += game_id
    print(
        f"Minimum required - Red: {minimum_required['red']} Green: {minimum_required['green']} Blue: {minimum_required['blue']}"
    )
    game_power = (
        minimum_required["red"] * minimum_required["green"] * minimum_required["blue"]
    )
    part_two_total += game_power

print(f"\nPart One Total: {part_one_total}")
print(f"Part Two Total: {part_two_total}")
