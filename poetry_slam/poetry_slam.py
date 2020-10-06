import random

# read porm from .txt file
def get_file_lines(filename):
    infile = open(filename, "r")
    poem = infile.readlines()
    infile.close()
    return (poem)

# reverses the poem
def lines_printed_backwards(lines_list):
    line_count = len(lines_list)

    for line in reversed(lines_list):
        print(line_count, line)
        line_count -= 1
    
# randomly selects which line to print
def lines_printed_random(lines_list):
    line_count = 0

    while line_count <= len(lines_list):
        index = random.randint(0,22)
        print(lines_list[index])
        line_count += 1

# prints lines that are either multiples of 3 or 5
def lines_printed_custom(lines_list):
    line_count = 0

    for line in lines_list:
        if line_count % 3 == 0 or line_count % 5 == 0:
            print(line)

        line_count += 1


lines = get_file_lines("poem.txt")

print("---------- Poem Printed Backwards: ----------\n")
backwards = lines_printed_backwards(lines)

print("---------- Poem Printed Randomly: ----------\n")
random = lines_printed_random(lines)

print("----------Poem Printed in Multiples of 3 and 5: ----------\n")
custom = lines_printed_custom(lines)