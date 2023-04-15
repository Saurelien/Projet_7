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
    best_yield = 0
    wallet = 500
    for combination in all_combinations(actions_list):
        total_amount = wallet
        for action_price in combination:
            print(f"Prix par action: {action_price[1]}")
            print(f"Pourcent de l'action a deux ans: {action_price[2]}")
            print(f"Total du porte feuille: {total_amount}")
            print("formule du rendement: portefeuille / prix de l'action * par le rendement")
            rendement = (total_amount / action_price[1]) * action_price[2]
            print("Rendement: ", rendement)
            if rendement > best_yield:
                best_yield = rendement
                best_combination = combination
    return best_combination, best_yield


start_process = time.time()
processing = psutil.Process()
idle_ram = processing.memory_info().rss
best_combination, best_yield = get_gain(NEW_COMBINATIONS, 500)
after_ram = processing.memory_info().rss
end_process = time.time()
print("Meilleurs combinaisons", best_combination, "cpu usage: ", end_process - start_process, "en secondes"
      , "Usage de la ram: "
      , after_ram - idle_ram, "Byte")
print("Meilleur rendement", best_yield, "cpu usage: ", end_process - start_process, "en secondes"
      , "Usage de la ram: "
      , after_ram - idle_ram, "Byte")
