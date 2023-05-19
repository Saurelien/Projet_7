import time
import psutil
import csv
import matplotlib.pyplot as plt

PATH = "CSV/dataset1_Python+P7.csv"
PATH_2 = "CSV/dataset2_Python+P7.csv"
INITIAL_BUDGET = 500
# Décompte du temps
START_TIME = time.monotonic()
# Objet pour traquer l'utilisation du cpu
PROCESS = psutil.Process()
# Objet pour traquer l'utilisation de la mémoire
MEM_BEFORE = PROCESS.memory_info().rss


class Colors:

    HEADER = '\033[35m'
    OKBLUE = '\033[34m'
    OKCYAN = '\033[36m'
    OKGREEN = '\033[32m'
    STR_YELLOW = '\033[33m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GREEN = OKGREEN + BOLD
    DESIGN = f"{STR_YELLOW + BOLD} |----------| {ENDC}"


def get_actions_from_csv(file_path_1):
    """TEST, Cette fonction prend en entrée un chemins de fichier type csv et renvoie une liste
    contenant les données du fichier."""

    # Récupération et convertion du fichier csv
    with open(file_path_1, 'r') as file:
        reader = csv.reader(file)
        # Ignorer l'en-tête
        next(reader)

        # Structuration de la liste
        action_list = []
        for name, price, profit in reader:
            price = float(price)
            profit = float(profit)
            if price > 0 and profit > 0:
                action_list.append((name, price, profit, price * profit / 100))

    # Trier les actions en fonction de leur rendement, du plus élevé au plus faible
    action_list = sorted(action_list, key=lambda action: action[3], reverse=True)
    return action_list


def display_best_action(action):
    return print(f"\n {Colors.HEADER+ Colors.BOLD}name: {Colors.GREEN}{action[0]}"
                 f"\n {Colors.HEADER}prix: {Colors.OKCYAN}{action[1]:2f}"
                 f"\n {Colors.HEADER}profit: {Colors.OKBLUE}{action[2]:2f}"
                 f"\n {Colors.HEADER}rendement réelle: {Colors.DESIGN}{Colors.GREEN}{action[3]:2f}\n")


def get_action_best_yield(action_list, budget):
    # Calcule du nombre d'actions du program:
    action_counts = 0

    # Sélectionner les actions ayant le rendement le plus élevé, jusqu'à atteindre le budget maximal de 500$
    best_actions = []
    total_gain = 0
    for action in action_list:
        if action[1] <= budget:
            # Si le prix de l'action est inferieur a 500$, j'ajoutes:
            # Le nom, Le prix, Le profit, Le rendement dans le dictionnaire best_actions
            best_actions.append({
                "name": action[0],
                "price": action[1],
                "profit": action[2],
                "yield": action[3]
            })
            budget -= action[1]
            display_best_action(action)
            action_counts += 1
            total_gain += action[3]
            # Utilisation de la ram pendant l'execution de la fonction
            mem_after = PROCESS.memory_info().rss
            # Utilisation du cpu pendant le processus en %
            cpu_usage = PROCESS.cpu_percent()
            # Calcule du temps écoulé
            elapsed_time = time.monotonic() - START_TIME
            if budget <= 0:
                break

    return print(f"\n {Colors.HEADER + Colors.BOLD}Temps écoulé: {Colors.GREEN}{elapsed_time:.3f} seconds "
                 f"\n {Colors.HEADER}Utilisation du cpu: {Colors.GREEN}{cpu_usage}%"
                 f"\n {Colors.HEADER}utilisation de la mémoire: "
                 f"{Colors.GREEN}{(mem_after - MEM_BEFORE) / 1024 / 1024:.2f} MB"
                 f"\n {Colors.HEADER}Number of actions: {Colors.GREEN}{action_counts}"
                 f"\n {Colors.HEADER}Budget final restant: {Colors.GREEN}{budget:.2f}$ "
                 f"\n {Colors.HEADER}Rendement réelle : {Colors.GREEN}{total_gain}")


action_list1 = get_actions_from_csv(PATH)
action_list2 = get_actions_from_csv(PATH_2)
get_action_best_yield(action_list1, INITIAL_BUDGET)
get_action_best_yield(action_list2, INITIAL_BUDGET)
