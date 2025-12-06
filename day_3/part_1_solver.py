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


def find_bank_with_max_joltage(
    banks: list[int], starting_index: int, positional_index: int
) -> tuple[int, int]:
    max_bank = -1
    max_bank_index = -1
    for i in range(starting_index, len(banks)):
        if len(banks) - 1 - i < positional_index:
            continue
        if banks[i] > max_bank:
            max_bank = banks[i]
            max_bank_index = i
    return max_bank, max_bank_index


def solve():
    INPUT_FILE = os.environ.get("INPUT_FILE")
    f = open(INPUT_FILE, "r")

    _NUMBER_OF_BANKS = 2
    total_joltage = 0

    line = f.readline()
    while line:
        max_banks = []
        banks = [int(x) for x in line.strip()]
        starting_index = 0
        for positional_index in range(_NUMBER_OF_BANKS - 1, -1, -1):
            max_bank, max_bank_index = find_bank_with_max_joltage(
                banks, starting_index, positional_index
            )
            max_banks.append(max_bank)
            starting_index = max_bank_index + 1

        max_joltage = 0
        for i in range(len(max_banks)):
            max_joltage += max_banks[i] * (10 ** (len(max_banks) - i - 1))
        print(f"Max joltage for banks {banks}: {max_banks} -> {max_joltage}")
        total_joltage += max_joltage

        line = f.readline()

    print(f"Total joltage: {total_joltage}")

    f.close()


if __name__ == "__main__":
    solve()
