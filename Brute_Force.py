from itertools import combinations

item_list = ["A", "B", "C"]
print(item_list)

def get_combinations(item_list):
    data = list()
    for i in combinations(data, 20):
        data.append(item_list[i])
    return data


print(get_combinations("20"))
# [["A"], ["B"], ["C"], ["A", "B"], ["A", "C"], ["B", "C"], ["A", "B", "C"]]

COMBINATIONS = {
    "action-1":
        {"Price": 20, "Interest": 5},
    "action-2":
        {"Price": 30, "Interest": 10},
    "action-3":
        {"Price": 50, "Interest": 15},
    "action-4":
        {"Price": 70, "Interest": 20},
    "action-5":
        {"Price": 60, "Interest": 17},
    "action-6":
        {"Price": 80, "Interest": 25},
    "action-7":
        {"Price": 22, "Interest": 7},
    "action-8":
        {"Price": 26, "Interest": 11},
    "action-9":
        {"Price": 48, "Interest": 13},
    "action-10":
        {"Price": 34, "Interest": 27},
    "action-11":
        {"Price": 42, "Interest": 17},
    "action-12":
        {"Price": 110, "Interest": 9},
    "action-13":
        {"Price": 38, "Interest": 23},
    "action-14":
        {"Price": 14, "Interest": 1},
    "action-15":
        {"Price": 18, "Interest": 3},
    "action-16":
        {"Price": float(0.8), "Interest": 8},
    "action-17":
        {"Price": float(0.4), "Interest": 12},
    "action-18":
        {"Price": 10, "Interest": 14},
    "action-19":
        {"Price": 24, "Interest": 21},
    "action-20":
        {"Price": 114, "Interest": 18},
                }
WALLET = 500


#Boucler sur le dictionnaire pour en sortie les 2 valeurs correspondant à chaques actions


#def all_combinations(action, price, interest)0:
#
#    combi = COMBINATIONS
#    for i in combinations(combi, 500):
#        print(i)
