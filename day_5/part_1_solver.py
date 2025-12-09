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

fresh_ingredient_ranges: list[tuple[int, int]] = []
fresh_ingredient_count = 0

with open(os.environ.get("INPUT_FILE"), "r") as f:
    is_reading_ingredient_ranges = True
    line = f.readline()
    while line:
        # check for blank line separating sections
        if line.strip() == "":
            is_reading_ingredient_ranges = False

        # reading fresh ingredient ranges
        if is_reading_ingredient_ranges:
            range_parts = line.strip().split("-")
            fresh_ingredient_ranges.append((int(range_parts[0]), int(range_parts[1])))

        # reading ingredient IDs
        elif id := line.strip():
            ingredient_id = int(id)
            for start, end in fresh_ingredient_ranges:
                if start <= ingredient_id <= end:
                    print(f"Ingredient ID {ingredient_id} is fresh.")
                    fresh_ingredient_count += 1
                    break

        line = f.readline()

print(f"Total fresh ingredients: {fresh_ingredient_count}")
