import secrets
import argparse


def word_to_dict(wordlist):
    word_dict = {}
    with open(wordlist) as f:
        for line in f:
            line = line.rsplit()
            word_dict[line[0]] = line[1]
    return word_dict


def dice_roll(rolls):
    thrown = ''
    for i in range(0, rolls):
        dice = secrets.choice(range(1, 7))
        throw = str(dice)
        thrown += throw
        i += 1
    return thrown


def throw_list(pass_length, rolls):
    throw_list = []
    for i in range(0, pass_length):
        roll = dice_roll(rolls)
        throw_list.append(roll)
    return throw_list


def passphrase_with_reference_nums(wordlist, rolls, pass_length):
    passphrase = ''
    all_words = word_to_dict(wordlist)
    rolls = throw_list(pass_length, rolls)
    for numbers in rolls:
        word = all_words.get(numbers)
        passphrase = passphrase + word + ' '
    return passphrase


def main():
    parser = argparse.ArgumentParser(description='Generate passphrases of your own length. Default is 6 words'
                                                 'from the "Eff large wordlist"')
    parser.parse_args()

    # list_prompt = input('What list do you want to use?: ')
    # if list_prompt.lower() == 'exit':
    #     print('Okay goodbye')
    #     quit()
    # elif list_prompt.lower() == 'l':
    #     wordlist = 'eff_large_wordlist.txt'
    #     rolls = 5
    # elif list_prompt.lower() == 's':
    #     wordlist = 'eff_short_wordlist_1.txt'
    #     rolls = 4
    # elif list_prompt != 'l' or list_prompt != 's':
    #     print('Wrong input.')
    #     quit()
    # try:
    #     length_prompt = input('How long of a passphrase do you want?: ')
    #     if length_prompt == 'exit':
    #         quit()
    #     pass_length = int(length_prompt)
    # except ValueError:
    #     print('Only numbers or "exit" are accepted')
    #     quit()


   # generate_passphrase = passphrase_with_reference_nums(wordlist, rolls, pass_length)
   # print(generate_passphrase)

if __name__ == "__main__":
    main()