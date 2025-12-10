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
    # read all rows so we can process columns
    max_row_length = 0
    rows: list[str] = []
    with open(input_path, "r") as f:
        for line in f:
            rows.append(line)
            max_row_length = max(max_row_length, len(line))

    # read columns to get operands & operator, preserving right- or left-padding spaces
    grand_total = 0
    operation = ["" for _ in range(len(rows))]
    for col_idx in range(max_row_length):
        # read down the column
        column = ["" for _ in range(len(rows))]
        for row_idx in range(len(rows)):
            # if the last row is shorter than the current col_idx,
            # pad with spaces
            if col_idx < len(rows[row_idx]):
                column[row_idx] = rows[row_idx][col_idx]
            else:
                column[row_idx] = "\n"

        # append to col until we hit a space-only column,
        # then store col as an operand and reset col
        if any(c != " " for c in column) and any(c != "\n" for c in column):
            for idx in range(len(operation)):
                operation[idx] += column[idx]

        # when we hit a space-only column, process the current col
        elif all(c == " " for c in column) or all(c == "\n" for c in column):
            operator = operation.pop().strip()
            operands = []
            # read operands from right to left, top to bottom
            for op_idx in range(len(operation[0]) - 1, -1, -1):
                operand = ""
                for row_idx in range(len(operation)):
                    operand += operation[row_idx][op_idx]
                operands.append(int(operand.strip()))

            total = operands[0]
            for operand in operands[1:]:
                if operator == "+":
                    total += operand
                elif operator == "*":
                    total *= operand
                else:
                    raise ValueError(f"Unknown operator: {operator}")
            grand_total += total

            # reset operation
            operation = ["" for _ in range(len(rows))]

    return grand_total


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    result = solve(input_path)
    print(f"Result: {result}")
