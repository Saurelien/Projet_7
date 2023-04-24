import csv
from itertools import combinations
import time
import psutil

# calcule temps de processus:
PROCESS_TIME = time.process_time()
# Utilisation en ressource
PROGRESS = psutil.Process()
PATH = "dataset1_Python+P7.csv"

def get_csv_file(path):
    action_list = []
    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Ne pas inclure l'entête du fichier
        next(csv_reader)
        for row in csv_reader:
            action_list.append([row[0], float(row[1]), float(row[2])])
    return action_list


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


def get_csv_combinations(action_list):
    all_combinations = []
    for action_data in range(1, len(action_list) + 1):
        for combination in combinations(action_list, action_data):
            all_combinations.append(combination)
    return all_combinations


def get_best_csv_combinations(actions_list, wallet=500):
    actions_list = get_csv_file(PATH)
    combinations = get_csv_combinations(actions_list)
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
    return best_combination, best_yield, process_time, cpu_percent, memory_usage


best_combination, best_yield, process_time, cpu_percent, memory_usage = get_best_csv_combinations(PATH)

print(f"Meilleur combinaison: {best_combination}\n"
      f"Meilleur rendement: {best_yield} € \n"
      f"Meilleur prix: {get_price_for_combination(best_combination)} \n"
      f"Temps d'execution: {process_time} secondes \n"
      f"cpu usage: {cpu_percent} % \n"
      f"Usage de la Ram: {memory_usage} %")