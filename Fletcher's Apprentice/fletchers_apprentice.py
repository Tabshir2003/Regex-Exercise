import re

def fletchers_apprentice(arrow):
    arrow = arrow.strip()
    if re.fullmatch(r'^>>-{3,5}>$', arrow):
        return str(arrow)
    
    arrow = re.sub(r'>>>+', '>>', str(arrow))

    thick_shaft = re.fullmatch(r'^(>>)(=+)(>)$', arrow)
    if thick_shaft:
        arrow = thick_shaft.group(1) + thick_shaft.group(2).replace('=', '-') + thick_shaft.group(3)

    if re.fullmatch(r'^>>-{3,5}>$', arrow):
        return str(arrow)
    return None


def main():
    good_arrows = []
    with open('input.txt', 'r', encoding="utf-8") as infile:
        for line in infile:
            result = fletchers_apprentice(line)
            if result is not None:
                good_arrows.append(result)
    with open('output.txt', 'w', encoding="utf-8") as outfile:
        outfile.write(' '.join(good_arrows))


if __name__ == "__main__":
    main()