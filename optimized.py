import time
import psutil
import csv

PATH = "dataset1_Python+P7.csv"
PATH_2 = "dataset2_Python+P7.csv"


def get_actions_from_csv(file_path_1, budget=500):
    """TEST, Cette fonction prend en entrée un chemins de fichier type csv et renvoie une liste
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

        # Structuration de la liste en intention ou liste de compréhension
        action_list = [
            (
                name,
                float(price),
                float(profit),
                float(price) * float(profit) / 100
            )
            for name, price, profit in reader
            if float(price) > 0 and float(profit) > 0
            and float(price) * float(profit) / 100 > 0
        ]

    # Trier les actions en fonction de leur rendement, du plus élevé au plus faible
    action_list = sorted(action_list, key=lambda action: (action[3], action[1]), reverse=True)

    # Sélectionner les actions ayant le rendement le plus élevé, jusqu'à atteindre le budget maximal de 500$
    best_actions = []
    for action in action_list:
        if action[1] <= budget:
            # Si le prix de l'action est inferieur a 500$, j'ajoutes:
            # Le nom, Le prix, Le profit, Le rendement dans le dictionnaire best_actions
            best_actions.append({
                "name": action[0],
                "price": action[1],
                "profit": action[2],
                "rendement réelle": action[3]
            })
            budget -= action[1]
        if budget <= 0:
            break

    # Afficher les résultats ligne par ligne pour une meilleurs visibilité
    rows_array = []
    for row in best_actions:
        rows = f"Sienna bought: \n {row['name']} \n total cost: {row['price']}\n" \
               f" Total return: {row['rendement réelle']}"
        print(rows)
        rows_array.append(rows)
    #max_yield = max(rows_array, key=lambda best_yield: best_yield[3])
    #print(max_yield)

    # Utilisation de la ram pendant l'execution de la fonction
    mem_after = process.memory_info().rss
    # Utilisation du cpu pendant le processus en %
    cpu_usage = process.cpu_percent()
    # Calcule du temps écoulé
    elapsed_time = time.monotonic() - start_time

    print(f"Temps écoulé: {elapsed_time:.3f} seconds")
    print(f"Utilisation du cpu: {cpu_usage}%")
    print(f"utilisation de la mémoire: {(mem_after - mem_before) / 1024 / 1024:.2f} MB")

    return rows_array


action_list1 = get_actions_from_csv(PATH)
action_list2 = get_actions_from_csv(PATH_2)
