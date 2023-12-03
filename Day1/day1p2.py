import string, re

number_dict = {
        "one": "1", "two": "2", "three": "3", 
        "four": "4", "five": "5", "six": "6", 
        "seven": "7", "eight": "8", "nine": "9"
    }

pattern = '|'.join([fr'(?<!\w){num}(?!\w)' for num in number_dict.keys()])

def match_replace(match):
    word = match.group(0)
    return number_dict.get(word, word)

if __name__ == "__main__":
    # Get input
    with open("input.txt", 'r') as f:
        rawlines = f.readlines()
        rawlines = ["twone", "nine"]

    # For part two, we'll replace spelled out numbers with their corresponding digits
    # Being based on order complicates things, attempting regex fuckery
    #converted_lines = [re.sub(pattern, match_replace, line) for line in rawlines]

    converted_lines = []
    for line in rawlines:
        replaced = re.sub(pattern, match_replace, line)
        print(replaced)
        converted_lines.append(replaced)

    # Fancy list comp (gotta show off)
    lines = [line.translate({ord(i): None for i in string.ascii_lowercase + '\n'}) for line in converted_lines]

    # Now without list comp for readability's sake
    total = 0

    for line in lines:
        first_number  = line[0]
        second_number = line[-1]
        
        print(line)
        print(f"{first_number}{second_number}")

        total += int(f"{first_number}{second_number}")

    print(total)
