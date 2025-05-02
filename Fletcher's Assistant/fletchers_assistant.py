import re

def fletchers_assistant(line, line_number):
    line = line.strip()
    if (len(line) > 8 or len(line) < 6):
        return str(line_number)
    if not re.search(r'^>>', line):
        return str(line_number)
    if not re.search(r'>$', line):
        return str(line_number)
    line = line[2:-1]
    if not re.fullmatch(r'-+', line):
        return str(line_number)
    return None


def main():
    bad_arrows = []
    with open('input.txt', 'r', encoding="utf-8") as infile:
        for line_number, line in enumerate(infile):
            result = fletchers_assistant(line, line_number+1)
            if result is not None:
                bad_arrows.append(result)
    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(' '.join(bad_arrows))


if __name__ == "__main__":
    main()