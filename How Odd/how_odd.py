import re

def how_odd(text):
    result = []

    for byte in text.split():
        pattern = re.search(r'1$', byte)
        if pattern:
            result.append(str(byte))

    return(' '.join(result))


def main():
    with open('input.txt', 'r', encoding="utf-8") as infile:
        input_text = infile.read()

    output_text = how_odd(input_text)

    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(output_text)


if __name__ == "__main__":
    main()