import time
import psutil
import csv
import matplotlib.pyplot as plt

PATH = "dataset1_Python+P7.csv"
PATH_2 = "dataset2_Python+P7.csv"


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


def calculate_total_return(actions):
    total_cost = sum(action["price"] for action in actions)
    total_profit = sum(action["profit"] for action in actions)
    return total_cost * total_profit / 100


def get_action_best_yield(action_list, budget=500):

    # Décompte du temps
    start_time = time.monotonic()
    # Objet pour traquer l'utilisation du cpu
    process = psutil.Process()
    # Objet pour traquer l'utilisation de la mémoire
    mem_before = process.memory_info().rss

    # Sélectionner les actions ayant le rendement le plus élevé, jusqu'à atteindre le budget maximal de 500$
    best_actions = []
    best_action_pair = None
    best_yield = 0
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
            print(f"\n name: {action[0]}, prix: {action[1]:2f}, profit: {action[2]:2f}"
                  f"\n rendement réelle: {action[3]:2f}, budget restant: {budget:.2f}$ \n")
            for i in range(len(best_actions)):
                for j in range(i + 1, len(best_actions)):
                    total_yield = calculate_total_return(best_actions)
                    if total_yield > best_yield:
                        best_action_pair = (best_actions[i], best_actions[j])
                        best_yield = total_yield
                    if budget <= 0:
                        break

    # Utilisation de la ram pendant l'execution de la fonction
    mem_after = process.memory_info().rss
    # Utilisation du cpu pendant le processus en %
    cpu_usage = process.cpu_percent()
    # Calcule du temps écoulé
    elapsed_time = time.monotonic() - start_time

    print(f"\n Budget final restant: {budget:.2f}$ \n Rendement réelle total sur deux ans: {best_yield}")
    print(f"\n Temps écoulé: {elapsed_time:.3f} seconds")
    print(f"\n Utilisation du cpu: {cpu_usage}%")
    print(f"\n utilisation de la mémoire: {(mem_after - mem_before) / 1024 / 1024:.2f} MB")

    return best_actions, best_action_pair


action_list1 = get_actions_from_csv(PATH)
action_list2 = get_actions_from_csv(PATH_2)
get_action_best_yield(action_list1)
get_action_best_yield(action_list2)
