import time
import psutil
import csv

PATH = "dataset1_Python+P7.csv"
PATH_2 = "dataset2_Python+P7.csv"


def get_actions_from_csv(file_path_1, budget=500):
    """TEST, Cette fonction prend en entrée deux chemins de fichier type csv et renvoie une liste
    contenant les données du fichier."""

    # Décompte du temps
    start_time = time.monotonic()
    # Objet pour traquer l'utilisation du cpu
    process = psutil.Process()
    # Objet pour traquer l'utilisation de la mémoire
    mem_before = process.memory_info().rss

    # Récupération et convertion du fichier csv
    with open(file_path_1, 'r') as file:
        reader = csv.reader(file)
        # Ignorer l'en-tête
        next(reader)
        actions = [(name, float(price), float(profit), (int(budget) / float(price)) * float(profit) / 100)
                   for name, price, profit in reader
                   if float(price) > 0 and float(profit) > 0]

    # Trier les actions en fonction de leur rendement, du plus élevé au plus faible
    actions = sorted(actions, key=lambda action: action[3], reverse=True)

    # Sélectionner les actions ayant le rendement le plus élevé, jusqu'à atteindre le budget maximal de 500$
    best_actions = []
    for action in actions:
        if action[1] <= budget:
            # tant que le prix de l'action est inferieur au 500$, j'ajoute:
            # Le nom, Le prix, Le profit, Le rendement dans la liste best_actions
            best_actions.append({
                "name": action[0],
                "price": action[1],
                "profit": action[2],
                "yield": action[3],
            })
            budget -= action[1]
        if budget <= 0:
            break

    # Utilisation de la ram pendant l'execution de la fonction
    mem_after = process.memory_info().rss
    # Utilisation du cpu pendant le processus en %
    cpu_usage = process.cpu_percent()
    # Calcule du temps écoulé
    elapsed_time = time.monotonic() - start_time

    # Print elapsed time, CPU usage, and memory usage
    print(f"Temps écoulé: {elapsed_time:.3f} seconds")
    print(f"Utilisation du cpu: {cpu_usage}%")
    print(f"utilisation de la mémoire: {(mem_after - mem_before) / 1024 / 1024:.2f} MB")

    return best_actions


action_list1 = get_actions_from_csv(PATH)
print(action_list1)
action_list2 = get_actions_from_csv(PATH_2)
print(action_list2)
