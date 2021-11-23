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

    def print(self):
        print(
            f'{self.name}\n{self.size} {self.type}, {self.alignment}\nArmor Class {self.armor_class}\nHit Points {self.hit_points}\nChallenge {self.challenge}')
        print(self.flavor_text)


def statblock_gen(challenge_rating: int, name: str, size: str, monster_type: str) -> StatBlock:
    if challenge_rating > 30 or challenge_rating < 0:
        raise ValueError('CR can\'t be higher than 30 or lower than 0')
    work_statblock = StatBlock(challenge_rating, name, size, monster_type)
    # NLP generated flavor text goes here
    work_statblock.flavor_text = """The Chungus is a True Neutral Large Beast, the size of a fully grown bull,
     with a coat of black and brown.\n
     The Chungus is a kind, peace-loving creature who seeks to be left alone to live in its forest.\n
     However, when the Chungus is threatened, it will fight with ferocity and cunning."""
    # TODO step 1 get name
    # TODO step 2 figure out size
    # TODO step 3 adjust statistics
    # TODO step 4 alignment
    # TODO step 5 ability scores
    # TODO step 7 adjust armor class
    # TODO step 8 adjust hit points
    # TODO step 9 figure out vulnerabilities, immunities and such
    # do things
    return work_statblock


if __name__ == '__main__':
    CR_test = 10
    name_test = "Chungus"
    size_test = "Large"
    type_test = "Beast"
    try:
        Statblock_test = statblock_gen(CR_test, name_test, size_test, type_test)
    except ValueError as err:
        print(err)

    Statblock_test.print()
