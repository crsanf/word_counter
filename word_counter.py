import sys

#Set the full file path here or leave blank and be prompted for it
source = r''''''

def main():
    word_count = 0
    with open(source) as f:
        for line in f:
            stripped_line = line.strip()
            words = stripped_line.split(' ')
            word_count += len(words)

    print(f'Total words in file: {word_count}')

if __name__ == '__main__':
    if source == '':
        source = sys.argv[1]

    print(sys.argv)
    main()