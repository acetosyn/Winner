from random import choice, seed
from pandas import read_csv as pd

df = pd("allnames.csv")
# print (df)
names = df.names.tolist()
print (names)

def pick_at_random(number):
    seed(number)
    winner = choice(names)
    return winner
