import json
from bonus_answer import bonus_answer

word_dict = json.load(open('words_dictionary.json'))


def solve(letters):
    letters.lower()
    num_letters = len(letters)

    possible_words = list()

    for word in word_dict:
        if len(word) == num_letters:
            if sorted(word.lower()) == sorted(letters):
                possible_words.append(word)

    return possible_words


if __name__ == '__main__':
    isStop = 'y'
    while isStop == 'y':
        print(solve(input('Write the letters you wanna check against:').lower()))

        isStop = input('Do you want to search another word? (y/n)').lower()

        if isStop != 'n' and isStop != 'y' and isStop != 'bonus':
            print('Option not recognized. Exiting')
            exit(0)

    if isStop == 'bonus':
        bonus_letters = input('Enter the bonus letters:')
        number_of_words = int(input('Enter the number of words:'))
        word_length = list()

        for i in range(0, number_of_words):
            word_length.append(int(input('Insert the length of the word number ' + str(i + 1))))

        bonus_answer(bonus_letters, number_of_words, word_length)