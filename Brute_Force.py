import itertools
import csv
from itertools import combinations
import time
import psutil

# calcule temps de processus:
PROCESS_TIME = time.process_time()
# Utilisation en ressource
PROGRESS = psutil.Process()
PATH = "dataset1_Python+P7.csv"
PATH_2 = "dataset2_Python+P7.csv"


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
        for combination in itertools.combinations(NEW_COMBINATIONS, all_combinations):
            combinations.append(combination)
    return combinations


def get_price_for_combination(combination):
    total_price = 0
    for action in combination:
        total_price += action[1]
    return total_price


def get_gain(action):
    return (action[1] * action[2]) / 100


def get_gain_for_combination(combination):
    total = 0
    for action in combination:
        total += get_gain(action)
    return total


def get_best(actions_list, wallet=500):
    combinations = all_combinations(actions_list)
    best_combination = None
    best_yield = 0
    for combination in combinations:
        # check action price
        total_price = get_price_for_combination(combination)
        if total_price > wallet:
            continue

        # check gain
        rendement = get_gain_for_combination(combination)
        if rendement > best_yield:
            best_combination = combination
            best_yield = rendement
            # calcule temps de processus:
            process_time = PROCESS_TIME
            # Utilisation en ressource
            cpu_percent = PROGRESS.cpu_percent()
            memory_usage = PROGRESS.memory_percent()
            if memory_usage >= 99 and process_time > 300:
                break
    return best_combination, best_yield, process_time, cpu_percent, memory_usage


best_combination, best_yield, process_time, cpu_percent, memory_usage = get_best(NEW_COMBINATIONS)


print(f"Meilleur combinaison: {best_combination}\n"
      f"Meilleur rendement: {best_yield} € \n"
      f"Meilleur prix: {get_price_for_combination(best_combination)} \n"
      f"Temps d'execution: {process_time} secondes \n"
      f"cpu usage: {cpu_percent} % \n"
      f"Usage de la Ram: {memory_usage} %")
