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


def solve(input_path: str) -> int:
    operands: list[list[int]] = []
    operators: list[str] = []
    grand_total = 0

    with open(input_path, "r") as f:
        for line in f:
            items = line.strip().split()
            if items and items[0].isdigit():
                operand_row = [int(item) for item in items]
                operands.append(operand_row)
            else:
                operators = items

    for col_idx in range(len(operands[0])):
        col_operands = [operands[row_idx][col_idx] for row_idx in range(len(operands))]
        total = col_operands[0]
        for row_idx in range(1, len(col_operands)):
            operator = operators[col_idx]
            if operator == "+":
                total += col_operands[row_idx]
            elif operator == "*":
                total *= col_operands[row_idx]
            else:
                raise ValueError(f"Unknown operator: {operator}")
        grand_total += total

    return grand_total


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    result = solve(input_path)
    print(f"Result: {result}")
