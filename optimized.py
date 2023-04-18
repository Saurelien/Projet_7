import itertools
import psutil
import time

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


def get_gain_optimized(actions_list, budget_wallet=500):
    best_yield = 0
    # Appel de la fonction " all_combination " dans la boucle des combinaisons possible de la liste en dur
    for combination in itertools.combinations(actions_list, + 1):
        for action in combination:
            # calcule temps de processus:
            process_time = time.process_time()
            # calcule du rendement " action[1] correspond a l'élément 2 = prix de l'action
            action_price = action[1]
            action_yield = action[2]
            capital = int(budget_wallet / action_price)
            rendement = (capital * action_yield) / 100
            print(rendement)
        if rendement > best_yield:
            best_yield = rendement
            best_combination = combination
        # Utilisation en ressource
        progress = psutil.Process()
        cpu_percent = progress.cpu_percent()
        memory_usage = progress.memory_percent()
    return best_combination, best_yield, cpu_percent, memory_usage, process_time


best_combination, best_yield, process_time, cpu_percent, memory_usage = get_gain_optimized(NEW_COMBINATIONS, 500)
print(f"Meilleur combinaison: {best_combination}\n"
      f"Meilleur rendement: {best_yield} € \n"
      f"Temps d'execution: {process_time} secondes \n"
      f"cpu usage: {cpu_percent} % \n"
      f"Usage de la Ram: {memory_usage} %")


