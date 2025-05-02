import re

def lsb(text):
    result = []

    for byte in text.split():
        matches = re.finditer(r'1', byte)
        if matches:
            match = list(matches)[-1].start() + 1
            result.append(str(match))
        else:
            result.append('-1')

    return(' '.join(result))


def main():
    with open('input.txt', 'r', encoding="utf-8") as infile:
        input_text = infile.read()

    output_text = lsb(input_text)

    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(output_text)


if __name__ == "__main__":
    main()