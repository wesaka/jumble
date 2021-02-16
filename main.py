import json
from itertools import permutations

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


def solve_inexact(letters, current_len):
    # The next step is to find all the permutations with the length equal to the word, inside the letters given
    perms = permutations(letters, current_len)

    # Lets also create a "blacklist" for all the possibilities discarded, so the program doesn't waste our time
    blacklist = list()

    for perm in perms:
        current_perm = ''.join(perm)
        possibilities = solve(current_perm)

        for possibility in possibilities:
            if possibility in blacklist:
                continue

            answer = input('Is ' + possibility + ' the correct word? (y/N)')
            if answer == 'y':
                # The next step is to remove the characters that form the accepted word
                for c in perm:
                    letters = letters.replace(c, '', 1)

                return possibility, letters

            else:
                blacklist.append(possibility)


if __name__ == '__main__':
    isStop = 'y'
    while isStop == 'y':
        print(solve(input('Write the letters you wanna check against:').lower()))

        isStop = input('Do you want to search another word? (y/N/bonus)').lower()

        if isStop != 'n' and isStop != 'y' and isStop != 'bonus':
            print('Option not recognized. Exiting')
            exit(0)

    if isStop == 'bonus':
        bonus_letters = input('Enter the letters of the bonus answer: ').lower()
        number_of_words = int(input('And now, tell me how many words there are to solve: '))
        for i in range(0, number_of_words):
            current_len = int(input('Now, what is the length of the word #' + str(i + 1) + "? "))
            answer, bonus_letters = solve_inexact(bonus_letters, current_len)

            print('The word #' + str(i + 1) + ' is: ' + answer + '\n')