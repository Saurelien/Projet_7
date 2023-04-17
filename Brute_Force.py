import itertools
from itertools import combinations
import time
import psutil

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


def all_combinations(actions_list):
    combinations = []
    for all_combinations in range(1, len(actions_list) + 1):
        for combination in itertools.combinations(actions_list, all_combinations):
            combinations.append(combination)
    return combinations


def get_gain(actions_list, budget_wallet=500):
    best_yield = 0
    best_combination = []
    #Appel de la fonction " all_combination " dans la boucle des combinaisons possible de la liste en dur
    for combination in all_combinations(actions_list):
        for action in combination:
            #calcule du rendement " action[1] correspond a l'élément 2 = prix de l'action
            capital = int(budget_wallet / action[1])
            rendement = capital * action[2] / 100
        if rendement > best_yield:
            best_yield = rendement
            best_combination = combination
        # calcule temps de processus:
        process_time = time.process_time()
        progress = psutil.Process()
        cpu_percent = progress.cpu_percent()
        memory_usage = progress.memory_percent()
    return best_combination, best_yield, cpu_percent, memory_usage, process_time


best_combination, best_yield, cpu_percent, memory_usage, process_time = get_gain(NEW_COMBINATIONS, 500)
print(f"Temps d'execution: {process_time}")
print(f"Meilleur combinaison: {best_combination}")
print(f"Meilleur rendement: {best_yield}")
print(f"Utilisation du processeur: {cpu_percent} %")
print(f"Utilisation de la RAM: {memory_usage} %")

