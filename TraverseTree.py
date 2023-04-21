from colors import *


###### FIND HIGHT OF TREE ######
def height(node):
    # Wenn der Knoten None ist, gibt die Funktion 0 zurück, da es keine Hoehe gibt.
    if node is None:
        return 0

    # Die Funktion wird rekursiv aufgerufen, um die Hoehe der linken und rechten Unterbaeume zu berechnen.
    # Dabei wird die groessere Hoehe der beiden Unterbaeume ausgewaehlt (max-Funktion) und dann um 1 erhoeht,
    # um den aktuellen Knoten selbst in der Hoehenberechnung zu beruecksichtigen.
    return 1 + max(height(node.left), height(node.right))


##### TRAVERSE TREE ######
def traverse_and_check_avl(node, stats):
    #Abbruchbedingung
    if node is None:
        return True

    # Gehe ganz nach unten links (Traversierung von unten)
    left_avl = traverse_and_check_avl(node.left, stats)

    # Gehe ganz nach unten rechts (Traversierung von unten)
    right_avl = traverse_and_check_avl(node.right, stats)

    # Besuche den aktuellen Knoten
    left_height = height(node.left)
    right_height = height(node.right)
    balance_factor = abs(left_height - right_height)
    is_avl = True

    if balance_factor > 1:
        print(bcolors.FAIL + f"bal({node.val}) = {balance_factor} (AVL violation!)" + bcolors.RESET)
        is_avl = False
    else:
        print(bcolors.GREEN + f"bal({node.val}) = {balance_factor}" + bcolors.RESET)

    stats['min'] = min(stats['min'], node.val)
    stats['max'] = max(stats['max'], node.val)
    stats['sum'] += node.val
    stats['count'] += 1

    # AVL ist nur TRUE, wenn alle 3 Werte True sind
    return is_avl and left_avl and right_avl


###### PRINT TREE STATS ######
def check_avl_and_print_stats(root):
    #Leerer Baum ist auch ein AVL-Baum
    if root.val is None:
        print(bcolors.UNDERLINE + "AVL: " + bcolors.RESET + bcolors.GREEN + " yes" + bcolors.RESET + "\nThis AVL-Tree is empty!")
        return

    # Dictionary mit Min, Max, Avg, Sum und Count wird erstellt
    # inf = unendlich
    # min wird mit +inf initialisiert, damit der erste Vergleich IMMER anschlaegt
    # max wird mit -inf initialisiert, damit der erste Vergleich IMMER anschlaegt
    stats = {'min': float('inf'), 'max': float('-inf'), 'sum': 0, 'count': 0}

    # AVL- Eigenschaft wird geprueft
    is_avl = traverse_and_check_avl(root, stats)

    print(
        bcolors.UNDERLINE + "AVL: " + bcolors.RESET + bcolors.GREEN + " yes" + bcolors.RESET if is_avl else bcolors.UNDERLINE + "AVL:" + bcolors.RESET + bcolors.FAIL + " no" + bcolors.RESET)
    print(
        f"{bcolors.UNDERLINE}min:{bcolors.RESET} {stats['min']}, {bcolors.UNDERLINE}max:{bcolors.RESET} {stats['max']}, {bcolors.UNDERLINE}avg:{bcolors.RESET} {round(stats['sum'] / stats['count'], 2)}")
