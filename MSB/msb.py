import re

def msb(text):
    result = []

    for byte in text.split():
        match = re.search(r'1', byte)
        if match:
            result.append(str(match.start() + 1))
        else:
            result.append('-1')

    return(' '.join(result))


def main():
    with open('input.txt', 'r', encoding="utf-8") as infile:
        input_text = infile.read()

    output_text = msb(input_text)

    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(output_text)


if __name__ == "__main__":
    main()