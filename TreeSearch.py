###### Simple Search ######
def simple_search(node, key, path=None):  # Wenn der path nicht gesetzt ist, wird None initialisiert
    if path is None:
        path = []

    # Wenn der Knoten None ist, wird False und der path zurückgegeben
    if node is None:
        return False, path

    # Wenn der Knotenwert None ist, wird False und der path zurückgegeben
    if node.val is None:
        return False, path

    # Wenn der Knotenwert dem gesuchten Schlüssel entspricht, wird True und der path zurückgegeben
    if node.val == key:
        return True, path + [node.val]

    # Wenn der gesuchte Schlüssel kleiner als der Knotenwert ist, wird der linke Teilbaum durchsucht
    if key < node.val:
        return simple_search(node.left, key, path + [node.val])

    # Wenn der gesuchte Schlüssel größer als der Knotenwert ist, wird der rechte Teilbaum durchsucht
    return simple_search(node.right, key, path + [node.val])


###### SUBTREE SEARCH GENAU ######
def check_subtree_structure(tree_node, subtree_node):
    # Wenn der Subtree vollstaendig durchsucht wurde, ist er im Baum enthalten
    if subtree_node is None:
        return True
    # Wenn der Baum vollstaendig durchsucht wurde, aber der Subtree noch nicht, dann ist der Subtree nicht im Baum enthalten
    if tree_node is None:
        return False

    # Wenn die Werte der aktuellen Knoten im Baum und im Subtree uebereinstimmen
    if tree_node.val == subtree_node.val:
        # Rekursive Suche in den linken Teilbaeumen von Baum und Subtree
        left_match = check_subtree_structure(tree_node.left, subtree_node.left)
        # Rekursive Suche in den rechten Teilbaeumen von Baum und Subtree
        right_match = check_subtree_structure(tree_node.right, subtree_node.right)

        # Nur wenn beide Suchen erfolgreich sind, wird True zurueckgegeben
        return left_match and right_match

    # Wenn die Werte der aktuellen Knoten im Baum und im Subtree nicht uebereinstimmen, wird die Suche fortgesetzt
    left_match = check_subtree_structure(tree_node.left, subtree_node)
    right_match = check_subtree_structure(tree_node.right, subtree_node)

    # Wenn einer der beiden rekursiven Suchaufrufe erfolgreich ist, wird True zurueckgegeben
    return left_match or right_match


###### SEARCH FOR SUBTREE ######
def subtree_search(tree, subtree):
    # Wenn der Baum leer ist
    if tree is None:
        return False
    # Subtree suchen
    if check_subtree_structure(tree, subtree):
        return True

    # Es wird einmal auf der linken Seite und einmal auf der rechten Seite rekursiv weiter gesucht
    # Gibt eine der beiden Aufrufe TRUE zurueck, wurde der Subtree gefudnden
    # Geben beide FALSE zurueck, wurde der Subtree nicht gefunden
    return subtree_search(tree.left, subtree) or subtree_search(tree.right, subtree)
