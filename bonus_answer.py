from itertools import permutations


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
