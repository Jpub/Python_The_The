import random

class Dice:
    def __init__(self, val=6):
        if val not in [4, 6, 8, 12, 20]:
            raise Exception('그런 정다면체는 존재하지 않습니다.') 
        self.face_num = val

    def shoot(self):
        return random.randint(1, self.face_num)