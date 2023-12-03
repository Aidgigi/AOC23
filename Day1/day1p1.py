import string

if __name__ == "__main__":
    # Get input
    with open("input.txt", 'r') as f:
        rawlines = f.readlines()

    # Fancy list comp (gotta show off)
    lines = [line.translate({ord(i): None for i in string.ascii_lowercase + '\n'}) for line in rawlines]

    # Now without list comp for readability's sake
    total = 0

    for line in lines:
        first_number  = line[0]
        second_number = line[-1]
        
        total += int(f"{first_number}{second_number}")

    print(total)
