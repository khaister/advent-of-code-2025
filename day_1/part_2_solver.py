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

INPUT_FILE = os.environ.get("INPUT_FILE")
f = open(INPUT_FILE, "r")

DIAL_START = 50
DIAL_MIN = 0
DIAL_MAX = 99

previous_dial_position = DIAL_START  # Previous position of the dial
current_dial_position = DIAL_START  # Current position of the dial
dial_at_zero_count = 0  # Total count of times the dial points at 0
dial_passed_zero_count = 0  # Count of times the dial passes 0 during rotation

line = f.readline()
while line:
    # Parse the rotation instruction
    direction = line[0]
    distance = int(line[1:])

    # Save the previous dial position
    previous_dial_position = current_dial_position

    # Update the current dial position
    if direction == "L":
        current_dial_position -= distance
    elif direction == "R":
        current_dial_position += distance
    current_dial_position %= DIAL_MAX + 1
    print(f"Moved {direction}{distance} to {current_dial_position}")

    # Check if the dial is at 0 after the rotation
    if current_dial_position == 0:
        print("DIAL AT 0!")
        dial_at_zero_count += 1

    # Calculate how many times the dial passed 0 during a full rotation
    num_rotations = distance // (DIAL_MAX + 1)
    dial_passed_zero_count += num_rotations
    if num_rotations > 0:
        print(f"Passed 0 {num_rotations} times during a full rotation.")

    # If previous dial position was not at zero and current is not at zero,
    # check if it passed 0 during the last partial rotation
    if previous_dial_position != 0 and current_dial_position != 0:
        # If moving left and new position is greater than previous, it passed 0 once more
        if direction == "L" and current_dial_position > previous_dial_position:
            dial_passed_zero_count += 1
            print("Passed 0 once more during left rotation.")
        # If moving right and new position is less than previous, it passed 0 once more
        elif direction == "R" and current_dial_position < previous_dial_position:
            dial_passed_zero_count += 1
            print("Passed 0 once more during right rotation.")

    line = f.readline()

print("--- FINAL RESULTS ---")
print(f"Dial was at 0 a total of {dial_at_zero_count} times.")
print(f"Dial passed 0 a total of {dial_passed_zero_count} times.")
print(f"Total count (at 0 + passed 0): {dial_at_zero_count + dial_passed_zero_count}")

f.close()
