from random import random

class IDGenService:
    @staticmethod
    def generate():
        rand = random() * 10**12 // 10
        return str(int(rand))