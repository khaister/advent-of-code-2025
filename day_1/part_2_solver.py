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

"""
--- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while
you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the
snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of
times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So,
in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times
before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?
"""

import os

INPUT_FILE = os.environ.get("INPUT_FILE", "day_1/input.txt")
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
