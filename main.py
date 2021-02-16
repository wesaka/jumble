import json
from itertools import permutations

word_dict = json.load(open('words_dictionary.json'))


def find_word(letters):
    letters.lower()
    num_letters = len(letters)

    possible_words = list()

    for word in word_dict:
        if len(word) == num_letters:
            if sorted(word.lower()) == sorted(letters):
                possible_words.append(word)

    return possible_words


def bonus_answer(letters, quantity, lengths):
    letters = letters.lower()
    tainted = list()

    combination_possibilities = list()

    for perm in permutations(letters):
        usable_perm = ''.join(perm)

        possibilities = list()

        start = 0
        end = lengths[0]

        for j in range(0, len(lengths)):
            if usable_perm[start:end] in tainted:
                break

            else:
                pos = find_word(usable_perm[start:end])

            if len(pos) == 0:
                tainted.append(usable_perm[start:end])
                break

            possibilities.append(pos)

            if j == len(lengths) - 1:
                if len(possibilities) != len(lengths):
                    possibilities = list()

                elif possibilities in combination_possibilities:
                    break

                else:
                    combination_possibilities.append(possibilities)
                    print(possibilities)
                    print('\n')

                continue

            else:
                start = start + lengths[j]
                end = end + lengths[j+1]


if __name__ == '__main__':
    isStop = 'y'
    while isStop == 'y':
        print(find_word(input('Write the letters you wanna check against:')))

        isStop = input('Do you want to search another word? (y/n/bonus)')
        isStop.lower()

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