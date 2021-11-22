class StatBlock:
    name = str
    def __init__(self):
        self.name = 'todo' #TODO

    def print(self):
        print(self.name)

def statblock_gen(challenge_rating: int) -> StatBlock:
    work_statblock = StatBlock()
    #do things
    return work_statblock


if __name__ == '__main__':
    CR_test = 10
    Statblock_test = statblock_gen(CR_test)

