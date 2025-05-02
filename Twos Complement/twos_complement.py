import re

def twos_complement(text):
    result = []

    for byte in text.split():
        if re.match(r'^1', byte):
            ls_one_idx = re.search(r'1[0]*$', byte).start()
            flipped = []
            for i in range(len(byte)):
                if i < ls_one_idx:
                    flipped.append('1' if byte[i] == '0' else '0')
                else:
                    flipped.append(byte[i])
            processed_byte = ''.join(flipped)
            result.append(processed_byte)
        else:
            result.append(byte)

    return(' '.join(result))


def main():
    with open('input.txt', 'r', encoding="utf-8") as infile:
        input_text = infile.read()

    output_text = twos_complement(input_text)

    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(output_text)


if __name__ == "__main__":
    main()