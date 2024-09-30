# level url: http://www.pythonchallenge.com/pc/return/bull.html
# Page text: "len(a[30]) = ?"

# Clicking the image takes to: http://www.pythonchallenge.com/pc/return/sequence.txt
# Text: "a = [1, 11, 21, 1211, 111221, "

# The pattern starts with 1 and then each iteration describes the previous, e.g.
# when n is 1, there is one number 1, which is written like "11"
# if n is 111221, the next will be 312211 as there are 3 1s, 2 2s, and 1 1

# How to solve?

# To find the next item, convert to string
# Loop over string
# Count the amount of repeated characters there are
# Append the number of times the character is repeated to output string
# Followed by appending the character
# Move to the next character


def sequencer():
    num = 1
    num_str = str(num)
    sequence_list = [1]
    for i in range(30):

        next_num_str = ""

        char_counter = 1
        for j in range(len(num_str)):
            if j + 1 == len(num_str):
                next_num_str += str(char_counter) + num_str[j]
                char_counter = 1
            elif num_str[j] == num_str[j + 1]:
                char_counter += 1
            else:
                next_num_str += str(char_counter) + num_str[j]
                char_counter = 1

        num_str = next_num_str
        sequence_list.append(num_str)

    # print(f"{sequence_list=}")
    print(f"{len(sequence_list[30])=}")


def main():
    sequencer()


if __name__ == "__main__":
    main()
