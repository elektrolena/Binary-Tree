from colors import *

####### Commands werden am Beginn des Programms ausgegeben ######
def printCommands():
    print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + "WELCOME TO TREECHECK!"
                                                              "\n\nYour available Commands:" + bcolors.RESET)

    print(bcolors.CYAN + bcolors.UNDERLINE + "\n(1) treecheck filename: " + bcolors.RESET)
    print("\nBuilds a Binary Tree with the values from your chosen file (input is possible with or "
          "without .txt)"
          "\n" + bcolors.CYAN + "Output: " + bcolors.RESET + " Minimum Value, Maximum Value, Average, Balance Factors, AVL-Value" + bcolors.RESET)

    print(bcolors.GREEN + bcolors.UNDERLINE + "\n\n(2) treecheck tree-filename subtree-filename:" + bcolors.RESET)
    print("\nChecks whether a Sub-binary-tree can be found within your chosen Binary Tree"
          "\n" + bcolors.GREEN + "Output: " + bcolors.RESET + " Subtree found! or Subtree not found!" + bcolors.RESET)


