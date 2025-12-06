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
    for product_id in range(start, end + 1):
        product_id_length = len(str(product_id))
        # Product ID must have an even number of digits
        if product_id_length % 2 != 0:
            continue

        # Find the middle point to split the product ID into two halves
        divider_index = product_id_length // 2
        left_half = str(product_id)[:divider_index]
        right_half = str(product_id)[divider_index:]

        # If the left half is equal to the right half, it's an invalid product ID
        if left_half == right_half:
            invalid_product_ids.append(product_id)
            print(f"    Found invalid product ID: {product_id}")

print(f"Sum of invalid product IDs: {sum(invalid_product_ids)}")

f.close()
