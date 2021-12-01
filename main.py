from StatBlock import StatBlock

import requests


def statblock_gen(challenge_rating: int, name: str, size: str, monster_type: str) -> StatBlock:
    if challenge_rating > 30 or challenge_rating < 0:
        raise ValueError('CR can\'t be higher than 30 or lower than 0')
    work_statblock = StatBlock(challenge_rating, name, size, monster_type)
    # NLP generated flavor text goes here
    work_statblock.flavor_text = "The Chungus is a True Neutral Large Beast, the size of a fully grown bull,\
with a coat of black and brown.\nThe Chungus is a kind, peace-loving creature who seeks to be left alone to live\
in its forest.\nHowever, when the Chungus is threatened, it will fight with ferocity and cunning."
    # TODO step 7 adjust armor class

    # TODO step 8 adjust hit points
    # TODO step 9 figure out vulnerabilities, immunities and such
    # do things
    return work_statblock


if __name__ == '__main__':
    CR_test = int(input("cr: "))
    name_test = "Chungus"
    size_test = "Large"
    type_test = "Beast"
    try:
        Statblock_test = statblock_gen(CR_test, name_test, size_test, type_test)
    except ValueError as err:
        print(err)

    Statblock_test.print()
