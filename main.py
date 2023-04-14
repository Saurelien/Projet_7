import itertools
import psutil
import time
from itertools import combinations

################################################################################################
################################################################################################
###       1. Retranscrire les actions dans le code: dans une liste                           ###
###       2. Écrire une fonction qui prend des paramètres et qui renvoie le rendement réel   ###
###            20€   100%                                                                    ###
###            X     5%                                                                      ###
###       3. Définir toutes les combinaisons possible d’actions.                             ###
###       4 Trouver pour 500€, quelle combinaison à le meilleur rendement.                   ###
################################################################################################
################################################################################################
NEW_COMBINATIONS = [
    ("#1", 20, 5),
    ("#2", 30, 10),
    ("#3", 50, 15),
    ("#4", 70, 20),
    ("#5", 60, 17),
    ("#6", 80, 25),
    ("#7", 22, 7),
    ("#8", 26, 11),
    ("#9", 48, 13),
    ("#10", 34, 27),
    ("#11", 42, 17),
    ("#12", 110, 9),
    ("#13", 38, 23),
    ("#14", 14, 1),
    ("#15", 18, 3),
    ("#16", float(0.8), 8),
    ("#17", float(0.4), 12),
    ("#18", 10, 14),
    ("#19", 24, 21),
    ("#20", 114, 18)
                   ]


def all_combinations(NEW_COMBINATIONS):
    new_combinations = list(itertools.combinations(NEW_COMBINATIONS, 3))
    return new_combinations


#start_process = time.time()
#processing = psutil.Process()
#idle_ram = processing.memory_info().rss
#all_combinations(NEW_COMBINATIONS)
#after_ram = processing.memory_info().rss
#end_process = time.time()

#print(all_combinations(NEW_COMBINATIONS), "cpu usage: ", end_process - start_process, "en secondes", "Usage de la ram: "
#      , after_ram - idle_ram, "Byte")



#def get_best_yield(price, wallet):


def get_combinations(item_list):
    data = list()
    for i in range(1, len(item_list) + 1):
        data += list(combinations(item_list, i))
    return data


start_process = time.time()
processing = psutil.Process()
idle_ram = processing.memory_info().rss
all_combinations(NEW_COMBINATIONS)
after_ram = processing.memory_info().rss
end_process = time.time()
print(get_combinations(NEW_COMBINATIONS), "cpu usage: ", end_process - start_process, "en secondes", "Usage de la ram: "
      , after_ram - idle_ram, "Byte")


def get_gain(param1, param2):

    return get_gain()


def find_best_yield(combinations):
    best_yield = 0
    best_combination = None

    for combination in combinations:
        name, initial_price, current_price = combination
        yield_percent = get_combinations(initial_price, current_price)

        if yield_percent > best_yield:
            best_yield = yield_percent
            best_combination = combination

    return best_combination, best_yield


#calcule du rendement:
# nombre d'action * le prix / par 100 == le rendemant * 365 jours * pour deux ans ==  rendement *2

#wallet = 500
#rendement = nb_action * price / 100

#def get_all_combinations(ALL_COMBINATIONS):
#
#    new_data = list()
#    for i in range(len(ALL_COMBINATIONS) + 1):
#        print(i)
#        for j in range(i):
#            new_data += list(combinations(ALL_COMBINATIONS, j))
#            print(new_data)
#    return new_data


#print(get_all_combinations(ALL_COMBINATIONS))

#print(get_combinations(ALL_COMBINATIONS))