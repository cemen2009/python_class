from random import randint


class Die:
    """Модель n-гранного ігрового кубика"""
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        """Симулює випадіння числа на 6-гранному кубику"""
        number = randint(1, self.sides)
        print(f"Вам випало число: {str(number)}")


cube = Die(6)
for i in range(0, 10):  # create 10 loop of cube dropping
    i += 1  # flag of loop
    cube.roll_die()     # cube drop
print()
side10 = Die(10)
for i in range(0, 10):  # create 10 loop of 10-sided figure dropping
    i += 1  # flag of loop
    side10.roll_die()     # figure drop
print()
side20 = Die(20)
for i in range(0, 10):  # create 10 loop of 20-sided figure dropping
    i += 1  # flag of loop
    side20.roll_die()     # figure drop
