# Find the start of packet sequence (four characters that are all different)
# This is an example of a text searching algorithm, where each character within a four interval has to be unique.
# To optimize this algorithm, I can move the search area up to the character after the duplicate one.
# For example, if we have abcbrs, then I can jump from abcb to cbrs, instead of checking bcbr.

# Optimize later ^^^

from tqdm import tqdm

letter_occurrence_map = {}
for i in range(26):
    letter_occurrence_map[chr(ord('a') + i)] = [0, 0]
    # The second element could be used to record the latest index of a given character


def find_start_of_packet():
    num_unique = 0
    code_index = 0
    while num_unique != 4 and code_index < len(letters_of_code):
        current_letter = letters_of_code[code_index]
        letter_occurrence_map.get(current_letter)[0] += 1
        if letter_occurrence_map.get(current_letter)[0] == 1:
            num_unique += 1

        code_index += 1
        if code_index >= 5:
            if letter_occurrence_map.get(letters_of_code[code_index - 5])[0] == 1:
                num_unique -= 1
            letter_occurrence_map.get(letters_of_code[code_index - 5])[0] -= 1

    print("The start-of-packet marker starts at index: " + str(code_index - 3)
          + " and ends at index " + str(code_index))


def find_start_of_message():
    num_unique = 0
    code_index = 0
    while num_unique != 14 and code_index < len(letters_of_code):
        current_letter = letters_of_code[code_index]
        letter_occurrence_map.get(current_letter)[0] += 1
        print(current_letter)
        if letter_occurrence_map.get(current_letter)[0] == 1:
            num_unique += 1

        code_index += 1
        if code_index >= 15:
            if letter_occurrence_map.get(letters_of_code[code_index - 15])[0] == 1:
                num_unique -= 1
            letter_occurrence_map.get(letters_of_code[code_index - 15])[0] -= 1
        print(num_unique)
    print("The start-of-message maker starts at index: " + str(code_index - 13)
          + " and ends at index " + str(code_index))


with open("input.txt") as datastream:
    letters_of_code = [char for char in datastream.readline()]
    # find_start_of_packet() # Part 1.
    find_start_of_message()  # Part 2.

if __name__ == "__main__":
    print()
