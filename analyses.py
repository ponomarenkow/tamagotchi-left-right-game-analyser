from scipy.stats import binomtest, chisquare
from encoding import encode, decode

left_wins = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20, 24]

#calculating in what percentage of games left was chosen three or more times
def left_winning(combinations):
    if len(combinations) == 0:
        print("Not enough data.")
        return
    left = 0
    for com in combinations:
        if com in left_wins:
            left += 1;
    print("Left would win in " + str(left) + " out of " + str(len(combinations)) + " (" + str(round(left/len(combinations)*100)) + "%) games.")
    p =  binomtest(left, len(combinations), 0.5, alternative="two-sided").pvalue
    if p < 0.05:
        print("Result statistically significant, p = " + str(round(p, 3)))
    else:
        print("Result not statistically significant, p = " + str(round(p, 3)))

def ever_appeared(combinations, appearances, symbol_mode):
    if len(combinations) == 0:
        print("Not enough data.")
        return
    for i in range(0, len(appearances)):
        if appearances[i] != 0:
            print(str(i + 1) + ". " + decode(i, symbol_mode))

def never_appeared(appearances, symbol_mode):
    anything = False
    for i in range(0, len(appearances)):
        if appearances[i] == 0:
            print(str(i + 1) + ". " + decode(i, symbol_mode))
            anything = True
    if not anything:
        print("Nothing to show here.")

def most_frequent(combinations, appearances, symbol_mode):
    if len(combinations) == 0:
        print("Not enough data.")
        return
    results = []
    mx = 0
    for i in range(0, len(appearances)):
        if appearances[i] > mx:
            mx = appearances[i]
            results = []
            results.append(i)
        elif appearances[i] == mx:
            results.append(i)
    for r in results:
        print(decode(r, symbol_mode))
            
#displaying total number of times each combination appeared and comparing it to uniform distribution using chi square test
def statistics(combinations, appearances, symbol_mode):
    for i in range(0, 32):
        print(str(i + 1) + ". " + decode(i, symbol_mode) + " - " + str(appearances[i])) # + "  p = " + str(round(binomtest(appearances[i], len(combinations), 1/32, alternative="two-sided").pvalue, 3)
    print("Total number of games: " + str(len(combinations)))
    if len(combinations) == 0:
        print("Not enough data to test for uniform distribution.")
    else:
        p = chisquare(appearances).pvalue
        if p < 0.05:
            print("Result statistically significant, p = " + str(round(p, 3)))
        else:
            print("Result not statistically significant, p = " + str(round(p, 3)))
