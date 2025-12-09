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
fresh_ingredient_ids: set[int] = set()

with open(os.environ.get("INPUT_FILE"), "r") as f:
    is_reading_ingredient_ranges = True

    for line in f:  # Better: iterate directly
        # check for blank line separating sections
        if line.strip() == "":
            is_reading_ingredient_ranges = False
            continue

        # reading fresh ingredient ranges
        if is_reading_ingredient_ranges:
            start, end = map(int, line.strip().split("-"))
            fresh_ingredient_ranges.append((start, end))
        # reading ingredient IDs
        else:
            ingredient_id = int(line.strip())
            for start, end in fresh_ingredient_ranges:
                if start <= ingredient_id <= end:
                    fresh_ingredient_ids.add(ingredient_id)
                    break  # Optional optimization


def merge_intervals(intervals):
    # Sort intervals by start
    intervals_copy = sorted(intervals, key=lambda x: x[0])
    merged = []

    for interval in intervals_copy:
        if not merged or interval[0] > merged[-1][1] + 1:  # +1 for contiguous
            # No overlap
            merged.append(list(interval))
        else:
            # Overlapping — merge
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Part 2: Use ALL ranges, not just "active" ones
all_ranges = merge_intervals(fresh_ingredient_ranges)

possible_fresh_ingredient_count = 0
for start, end in all_ranges:
    possible_fresh_ingredient_count += end - start + 1

print(f"Part 1 - Total confirmed fresh ingredients: {len(fresh_ingredient_ids)}")
print(f"Part 2 - Total possible fresh ingredients: {possible_fresh_ingredient_count}")
