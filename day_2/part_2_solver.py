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

INPUT_FILE = os.environ.get("INPUT_FILE")
f = open(INPUT_FILE, "r")

line = f.readline()
product_id_ranges = line.split(",")

invalid_product_ids = []
for product_id_range in product_id_ranges:
    # Find the start and end of the product ID range
    start_end = product_id_range.split("-")
    start = int(start_end[0])
    end = int(start_end[1])
    print(f"Product ID Range: {start} - {end}")

    # Check each product ID in the range
    for id in range(start, end + 1):
        product_id = str(id)

        # Look at all possible partitions, starting from 2 parts
        # to full length (i.e. all digits in the product ID are the same)
        for part_count in range(2, len(product_id) + 1):
            if len(product_id) % part_count != 0:
                # skip if not divisible
                continue

            # Collect all parts and add to a set
            parts = set()
            part_size = len(product_id) // part_count
            for i in range(part_count):
                part = product_id[i * part_size : (i + 1) * part_size]
                parts.add(part)

            # If there's only one unique part, then all parts are the same
            if len(parts) == 1:
                invalid_product_ids.append(id)
                print(f"    Found invalid product ID: {id}")
                break

print(f"Sum of invalid product IDs: {sum(invalid_product_ids)}")

f.close()
