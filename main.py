import os
import platform
from MyTree import *
from TraverseTree import *
from TreeSearch import *
from commands import *


##### CLEAR CONSOLE ######
def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")


###########################
##### INSERT VALUES #######
def build_tree(search_tree, filename):
    with open(filename, "r") as f:  # file oeffnen
        nums = [int(line.strip()) for line in f]    #alle Integer Werte aus der File in einen Array speichern

        for num in nums:
            search_tree.insert(num)  # jedes Value wird in den Baum insertet
    return search_tree  # Baum wird zurückgegeben


###########################
###### FILE EXISTS? #######
def check_file_exists(filename):
    if not os.path.isfile(filename):  # File existiert nicht
        print(bcolors.WARNING + f"Error: file {filename} does not exist." + bcolors.RESET)
        return False
    return True  # File existiert


###########################
###### TREECHECK 1 ########
def treecheck(tree, filename):
    if not check_file_exists(filename):  # File existiert nicht
        return

    tree = build_tree(tree, filename)  # Baum aufbauen

    check_avl_and_print_stats(tree)  # Baum auswerten


###################################################
############------------MAIN-----------############
###################################################

printCommands()
while True:
    # Command Inputfeld
    command = input(bcolors.BOLD + bcolors.WARNING + "\n\nCommand: " + bcolors.RESET)
    clear_console()
    # Eingabe wird aufgesplittet
    split_input = command.split()

    # Wenn die Eingabe Leer ist -> Ungueltiges Command
    if not command.strip():
        print(bcolors.WARNING + "\nInvalid command!" + bcolors.RESET)
        continue

    # Wenn "exit" eingegeben wurde -> Programm beenden
    if split_input[0] == "exit":
        clear_console()
        print(bcolors.CYAN + bcolors.BOLD + "Goodbye!" + bcolors.RESET)
        break

    # Wenn das Command NICHT treecheck ist -> Ungueltiges Command
    if split_input[0] != "treecheck":
        print(bcolors.WARNING + "\nInvalid command!" + bcolors.RESET)
        continue

    # Wenn nur ein Wort eingegeben wurde -> Ungueltiges Command
    if len(split_input) < 2:
        print(bcolors.WARNING + "\nPlease input valid Command!" + bcolors.RESET)
        continue

    # Filenames aufsplitten -> falls zwei Files eingegeben wurden
    filenames = split_input[1:]  # extrahiert alle Elemente ab dem Index 1 (also alles nach "treecheck")
    all_files_exist = True

    # existieren die Files
    for i in range(len(filenames)):
        if not filenames[i].endswith(".txt"):   #Wenn Endung .txt nicht eingegeben wurde, wird sie hinzugefügt
            filenames[i] += ".txt"
        if not check_file_exists(filenames[i]):
            all_files_exist = False
            break

    # Alle Files existieren
    if all_files_exist:

        # Eine File -> Baum auswerten
        if len(filenames) == 1:
            search_tree = TreeNode()
            treecheck(search_tree, filenames[0])

        # Zwei Files -> Suchbaum
        else:
            # Baume werden gebaut
            search_tree = build_tree(TreeNode(), filenames[0])
            subtree = build_tree(TreeNode(), filenames[1])

            # Simple Search -> nur nach einem Knoten suchen
            if subtree.left is None and subtree.right is None:  # Ein einzelner Knoten hat keinen linken und rechten Teilbaum
                print(bcolors.HEADER + bcolors.BOLD + "Simple Search" + bcolors.RESET)
                found, path = simple_search(search_tree, subtree.val)   # es wird ein Bool und der Pfad zurückgegeben

                #Suche erfolgreich
                if found:
                    #wandelt die Liste der Knotenwerte in einen String um, der die Werte durch Kommas getrennt enthält
                    path_str = ', '.join(map(str, path))
                    print(subtree.val, "found", path_str)
                else:
                    print(subtree.val, "not found!")

            # Subtree Search -> es wird nach einem Subtree gesucht
            else:
                print(bcolors.HEADER + bcolors.BOLD + "Subtree Search" + bcolors.RESET)
                result = subtree_search(search_tree, subtree)

                # Gefunden
                if result:
                    print(bcolors.GREEN + "Subtree found!" + bcolors.RESET)
                # Nicht gefunden
                else:
                    print(bcolors.FAIL + "Subtree not found!" + bcolors.RESET)
