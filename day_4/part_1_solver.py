# Advent of Code 2025
# Copyright (C) 2025 Khai Nguyen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os

from rich import print

ROLL = "@"
EMPTY = "."
MAX_SURROUNDING_ROLLS = 3


def count_surrounding_rolls(rolls: list[str], row: int, col: int) -> int:
    count = 0
    for r in range(max(0, row - 1), min(len(rolls), row + 2)):
        for c in range(max(0, col - 1), min(len(rolls[0]), col + 2)):
            # Skip the current roll itself
            if (r, c) == (row, col):
                continue

            # Count if there's a roll in the position being checked
            if rolls[r][c] == ROLL:
                count += 1

    return count


rolls = []
with open(os.environ.get("INPUT_FILE"), "r") as f:
    line = f.readline()
    while line:
        rolls.append(line.strip())
        line = f.readline()

accessible_rolls = 0
for row in range(len(rolls)):
    for col in range(len(rolls[0])):
        # Skip if it's not a roll
        if rolls[row][col] != ROLL:
            continue

        surrounding_rolls = count_surrounding_rolls(rolls, row, col)
        if surrounding_rolls <= MAX_SURROUNDING_ROLLS:
            accessible_rolls += 1

print(f"Accessible rolls: {accessible_rolls}")
