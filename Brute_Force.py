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


def get_gain(actions_list, wallet=500):
    get_combinations = all_combinations(actions_list)
    best_yield = 0
    for combination in get_combinations:
        for action_price in combination:
            rendement = (wallet / action_price[1]) * action_price[2] / 100
            best_yield = rendement
            best_combination = combination
            # calcule temps de processus:
            process_time = time.process_time()
            # Utilisation en ressource
            progress = psutil.Process()
            cpu_percent = progress.cpu_percent()
            memory_usage = progress.memory_percent()
    return best_combination, best_yield, process_time, cpu_percent, memory_usage


best_combination, best_yield, process_time, cpu_percent, memory_usage = get_gain(NEW_COMBINATIONS, 500)
print(f"Meilleur combinaison: {best_combination}\n"
      f"Meilleur rendement: {best_yield} € \n"
      f"Temps d'execution: {process_time} secondes \n"
      f"cpu usage: {cpu_percent} % \n"
      f"Usage de la Ram: {memory_usage} %")