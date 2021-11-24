from random import randint, shuffle
import requests

def generate_ability_scores(challenge_rating: int) -> list[int]:
    ability_array = []
    for i in range(0, 6):
        ability_array.append(randint(3 + i, 20 + int(challenge_rating / 3)))
    shuffle(ability_array)
    return ability_array


class StatBlock:
    name = str
    armor_class = int
    hit_points = int
    attack_bonus = int
    damage_output = int
    proficiency_bonus = int
    save_dc = int
    size = str
    type = str
    alignment = str
    challenge = int
    flavor_text = str
    strength = int
    dexterity = int
    constitution = int
    wisdom = int
    intelligence = int
    charisma = int

    def __init__(self, challenge_rating: int, name: str, size: str, type: str):
        self.name = name
        self.size = size
        self.type = type
        self.alignment = "True Neutral"  # placeholder
        self.challenge = challenge_rating

        # values per CR are as specified in the "Monster Statistics by Challenge Rating" table on page 274 of the DMG
        # list index corresponds to target CR, as in CR 0 has 10 AC and so on
        ac_list = [10, 13, 13, 13, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18]  # 17 or higher = 19
        hp_list = [6, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 250, 265, 280, 295, 310, 325,
                   340, 355, 400, 445, 490, 535, 580, 625, 670, 715, 760, 805, 850]
        atk_list = [3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 9, 10, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13,
                    13, 14]
        dmg_list = [1, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, 104, 110, 116, 122, 140, 158, 176,
                    194, 212, 230, 248, 266, 284, 302, 320]
        prof_list = [2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9]
        dc_list = [10, 13, 13, 13, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 21,
                   21, 21, 22, 22, 22, 23]

        if challenge_rating >= 17:
            self.armor_class: int = 19
        else:
            self.armor_class: int = ac_list[challenge_rating]
        self.hit_points: int = hp_list[challenge_rating]
        self.attack_bonus: int = atk_list[challenge_rating]
        self.damage_output: int = dmg_list[challenge_rating]
        self.proficiency_bonus: int = prof_list[challenge_rating]
        self.save_dc: int = dc_list[challenge_rating]

        # generate ability scores
        ability_array = generate_ability_scores(challenge_rating)
        self.strength = ability_array[0]
        self.dexterity = ability_array[1]
        self.constitution = ability_array[2]
        self.wisdom = ability_array[3]
        self.intelligence = ability_array[4]
        self.charisma = ability_array[5]

    def return_ability_bonus(self, ability: str):
        ability_score = int
        if ability == "str":
            ability_score = self.strength
        elif ability == "dex":
            ability_score = self.dexterity
        elif ability == "con":
            ability_score = self.constitution
        elif ability == "wis":
            ability_score = self.wisdom
        elif ability == "int":
            ability_score = self.intelligence
        elif ability == "cha":
            ability_score = self.charisma
        else:
            raise ValueError("ability must be str, dex, con, wis, int, or cha")
        ability_score = ability_score - 10
        ability_score = int(ability_score / 2)
        return ability_score

    def print(self):
        print(self.name)
        print(f'{self.size} {self.type}, {self.alignment}')
        print(f'Armor Class {self.armor_class}')
        print(f'Hit Points {self.hit_points}')
        print(f'STR {self.strength}(+{self.return_ability_bonus("str")}) \
DEX {self.dexterity}(+{self.return_ability_bonus("dex")}) \
CON {self.constitution}(+{self.return_ability_bonus("con")}) \
INT {self.intelligence}(+{self.return_ability_bonus("int")}) \
WIS {self.wisdom}(+{self.return_ability_bonus("wis")}) \
CHA {self.charisma}(+{self.return_ability_bonus("cha")})')
        print(f'Challenge {self.challenge}')

        print(self.flavor_text)


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
