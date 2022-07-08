import secrets
import argparse


def word_to_dict(wordlist):  # Convert wordlist to dictionary that can be read by passphrase function
    word_dict = {}
    with open(wordlist) as f:
        for line in f:
            line = line.rsplit()
            word_dict[line[0]] = line[1]
    return word_dict


def dice_roll(rolls):  # Roll the dice n number of times to produce number sequence
    thrown = ''
    for i in range(0, rolls):
        dice = secrets.choice(range(1, 7))
        throw = str(dice)
        thrown += throw
        i += 1
    return thrown


def list_of_throws(pass_length, rolls):  # Combine number sequences into a list to be read by passphrase function
    throw_list = []
    for i in range(0, pass_length):
        roll = dice_roll(rolls)
        throw_list.append(roll)
    return throw_list


def passphrase_with_reference_nums(wordlist, rolls, pass_length):  # Generate passphrase based on number sequences
    # provided
    passphrase = ''
    all_words = word_to_dict(wordlist)
    rolls = list_of_throws(pass_length, rolls)
    for numbers in rolls:
        word = all_words.get(numbers)
        passphrase = passphrase + word + ' '
    return passphrase


def main():
    # Set default values for generator
    wordlist = 'eff_large_wordlist.txt'
    pass_length = 6
    rolls = 5

    # Add parsing options for command line interface
    parser = argparse.ArgumentParser(description='Generate passphrases of your own length. Default is 6 words'
                                                 'from the "Eff large wordlist"')
    parser.add_argument('-w', '--wordlist', default='large', choices=['large', 'short'], help='Set wordlist to be used')
    parser.add_argument('-l', '--length', default=6, type=int, help='Set length of phrase')
    # parser.add_argument('-c', '--custom', type=str, help='Specify filepath to your own wordlist')
    args = parser.parse_args()
    if args.wordlist == 'large':
        wordlist = 'eff_large_wordlist.txt'
        rolls = 5
    elif args.wordlist == 'short':
        wordlist = 'eff_short_wordlist_1.txt'
        rolls = 4
    if args.length:
        pass_length = args.length

    generate_passphrase = passphrase_with_reference_nums(wordlist, rolls, pass_length)
    print(generate_passphrase)


if __name__ == "__main__":
    main()
