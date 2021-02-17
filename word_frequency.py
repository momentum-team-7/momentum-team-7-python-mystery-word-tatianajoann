stop_words = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', ''
]
stop_characters = [";", ":", "?", "!", ",", ".", '"', "'"]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, "r") as open_file:
        read_file = open_file.read()
        for i in stop_characters:
            read_file = read_file.replace(i, '')
        read_file = read_file.replace("\n", ' ')
        read_file = read_file.replace("—", ' ')
        read_file = read_file.replace("-", ' ')
        read_file = read_file.lower()
        read_file = read_file.split(" ")
        copy_list = []
        for word in read_file:
            # print(word)
            # print(read_file)
            if word not in stop_words:
                copy_list.append(word)
        # print(read_file)
        # print(copy_list)
        another_list = []
        for word in copy_list:
            if word not in another_list:
                print(word, "|", copy_list.count(word),
                      "*" * copy_list.count(word))
                another_list.append(word)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

# read in file and print out the frequency of words in that file
# open file and save it to a variable - jupyter 09
# remove punctuation
# normalize all words to lowercase
# remove stop words, words used so frequently theyre ignored
# check each word and see if its equal to a stop word , if it is
# conditional with if
# go through file word by word and keep a count of how often each word is ued.
# probably use a dictionary to store this key => words, values => occurences
