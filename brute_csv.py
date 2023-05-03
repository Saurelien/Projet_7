import time
import psutil
import csv


# calcule temps de processus:
PROCESS_TIME = time.process_time()
# Utilisation en ressource
PROGRESS = psutil.Process()
PATH = "dataset1_Python+P7.csv"
PATH_2 = "dataset2_Python+P7.csv"


def get_actions_from_csv(file_path_1):
    """TEST, Cette fonction prend en entrée deux chemins de fichier type csv et renvoie une liste
    contenant les données du fichier."""

    # Récupération et convertion de " dataset1_Python+P7.csv "
    print("Lecture de dataset1_Python+P7.csv...")
    with open(file_path_1, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # ignorer l'entête

        # Cette liste contient pour chaque action, les informations suivantes : nom, prix, bénéfice et rendement
        # (calculé en multipliant le prix par le bénéfice, le tout divisé par 100).
        # Ainsi qu'une condition eliminant les données à zero ou inférieur du prix et profit de la liste
        action_list1 = [
            (name, float(price), float(profit), float(price) * float(profit) / 100)
            for name, price, profit in reader
            if float(price) > 0 and float(profit) > 0
        ]

    # Utilisation de la fonction "max" pour déterminer l'action la plus rentable.
    # Cette action est déterminée en utilisant le rendement comme clé de tri.
    best_action_yield = max(action_list1, key=lambda best_yield: best_yield[3])
    print(best_action_yield)

    return action_list1

def get_price_for_combination(combination):
    total_price = 0
    for action in combination:
        total_price += action[1]
    return total_price


def get_gain_for_combination(combination1):
    total = 0
    for action in combination1:
        total += get_gain(action)
    return total


def get_best(actions_list, wallet=500):
    # Utilisation actuelle du CPU:
    start_cpu_percent = psutil.cpu_percent()

    # Utilisation actuelle de la mémoire:
    process = psutil.Process()
    start_mem = process.memory_info().rss / 1024 / 1024

    # Début de la mesure du temps d'exécution
    start_time = time.time()

    combinations = get_actions_from_csv(PATH)
    best_combination = None
    best_yield = 0
    for combination in combinations:
        # check action price
        total_price = get_price_for_combination(combination)
        if float(total_price) > float(wallet):
            continue

        # check gain
        rendement = get_gain_for_combination(combination)
        if rendement > best_yield:
            best_combination = combination
            best_yield = rendement

            # Fin de la mesure du temps d'execution:
            end_time = time.time()

            # Consommation de la mémoire à la fin
            end_mem = process.memory_info().rss / 1024 / 1024

            # % de cpu consommé:
            end_cpu_percent = psutil.cpu_percent()

            # Calculer le temps de lecture
            elapsed_time = end_time - start_time

            # Calculer la consommation de mémoire
            mem_usage = end_mem - start_mem

            # Afficher les informations sur les performances :
            print(f"Temps de lecture : {elapsed_time:.2f} secondes")
            print(f"Consommation de mémoire : {mem_usage:.2f} MB")
            print(f"Utilisation CPU : {end_cpu_percent - start_cpu_percent:.2f} %")
            if memory_usage >= 99 and process_time > 300:
                break
    return best_combination, best_yield, process_time, cpu_percent, memory_usage


action_list1 = get_actions_from_csv(PATH)
best_combination, best_yield, process_time, cpu_percent, memory_usage = get_best(action_list1)


print(f"Meilleur combinaison: {best_combination}\n"
      f"Meilleur rendement: {best_yield} € \n"
      f"Meilleur prix: {get_price_for_combination(best_combination)} \n"
      f"Temps d'execution: {process_time} secondes \n"
      f"cpu usage: {cpu_percent} % \n"
      f"Usage de la Ram: {memory_usage} %")