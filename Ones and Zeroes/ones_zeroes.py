import re

def ones_zeroes(text):
    replace_ones = re.sub(r'[iIl|!/]', '1', text)
    result = re.sub(r'[oO@Θθ]', '0', replace_ones)
    return result

def main():
    with open('input.txt', 'r', encoding="utf-8") as infile:
        input_text = infile.read()

    output_text = ones_zeroes(input_text)

    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(output_text)

if __name__ == "__main__":
    main()