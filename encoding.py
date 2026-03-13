
increments = [16, 8, 4, 2, 1]

#returning the number assigned to a given combination of left and right
def encode(combination: str) -> int:
    if len(combination) != 5:
        print("Combinations must have length of 5 characters.")
        return -1

    result = 0

    for i in range(0, 5):
        symbol = combination[i]
        if not (symbol == 'l' or symbol == 'r' or symbol == '<' or symbol == '>' or symbol == ',' or symbol == '.'):
            print("You may only use characters 'l', 'r', '<' or '>'.")
            return -1
        elif symbol == 'r' or symbol == '>' or symbol == '.':
            result += increments[i]

    return result


#returning a combination of left and right that is associated with given number
def decode(number: int, symbol_mode: bool) -> str:
    if number > 31 or number < 0:
        return False

    l = '<'
    r = '>'
    if not symbol_mode:
        l = 'l'
        r = 'r'

    result = ""
    for i in increments:
        if number >= i:
            result += r
            number -= i
        else:
            result += l

    return result
