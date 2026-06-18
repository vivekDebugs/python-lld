from random import random

class IdGenService:
    @staticmethod
    def generate() -> str:
        factor = 10**12
        randNumber = random() * factor // 10
        return str(int(randNumber))