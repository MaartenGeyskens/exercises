# Write your code here
def cakes(eggs, butter, flour):
    eggsc = eggs//5
    butterc = butter//250
    flourc = flour//250
    return min(eggsc, butterc, flourc)