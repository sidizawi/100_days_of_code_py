with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as letters:
            with open(f"./Output/ReadyToSend/letter_for_{name[:len(name) - 1]}.txt", mode='w') as f:
                for line in letters:
                    if "[name]" in line:
                        f.write(f"Dear {name[:len(name) - 1]},\n")
                    else:
                        f.write(line)