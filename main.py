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



def get_gain(actions_list, wallet):
    get_combinations = all_combinations(actions_list)
    best_yield = 0
    wallet = 500
    for combination in get_combinations:
        total_amount = wallet
        rendement_total = 0
        for action_price in combination:
            invest = total_amount / 3
            total_amount -= invest
            print(action_price[1])
            print(total_amount)
            rendement = (total_amount / action_price[1]) * action_price[2]
            print(rendement)
            rendement_total += rendement
            if rendement_total > best_yield:
                best_yield = rendement_total
                best_combination = combination
    return best_combination, best_yield


start_process = time.time()
processing = psutil.Process()
idle_ram = processing.memory_info().rss
best_combination, best_yield = get_gain(NEW_COMBINATIONS, 500)
after_ram = processing.memory_info().rss
end_process = time.time()
print("Meilleur combinaison", best_combination, "cpu usage: ", end_process - start_process, "en secondes"
      , "Usage de la ram: "
      , after_ram - idle_ram, "Byte")
print("Meilleur rendement", best_yield, "cpu usage: ", end_process - start_process, "en secondes"
      , "Usage de la ram: "
      , after_ram - idle_ram, "Byte")
