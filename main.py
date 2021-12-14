from StatBlock import StatBlock

import requests


def statblock_gen(challenge_rating: int, name: str, size: str, monster_type: str) -> StatBlock:
    accepted_types = ["aberration", "beast", "construct", "elemental", "monstrosity", "plant"]
    accepted_sizes = ["tiny", "small", "medium", "large", "huge", "gargantuan"]
    if size not in accepted_sizes:
        raise ValueError('Size must be a DnD size')
    if monster_type not in accepted_types:
        raise ValueError('See supported types')
    if challenge_rating > 30 or challenge_rating < 0:
        raise ValueError('CR can\'t be higher than 30 or lower than 0')
    work_statblock = StatBlock(challenge_rating, name, size, monster_type)
    # NLP flavor text generation goes here
    work_statblock.flavor_text = "The Chungus is a True Neutral Large Beast, the size of a fully grown bull,\
with a coat of black and brown.\nThe Chungus is a kind, peace-loving creature who seeks to be left alone to live\
in its forest.\nHowever, when the Chungus is threatened, it will fight with ferocity and cunning."
    # TODO adjust based on monster type
    return work_statblock


if __name__ == '__main__':
    CR_test = int(input("CR: "))
    name_test = input("Name: ")
    size_test = input("Size: ").lower()
    type_test = input("Type: ").lower()
    try:
        Statblock_test = statblock_gen(CR_test, name_test, size_test, type_test)
        Statblock_test.print()
    except ValueError as err:
        print(err)
