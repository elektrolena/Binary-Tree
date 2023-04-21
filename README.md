# Binary-Tree
This is a project I worked on with my fellow student Helene Harrer.

This program interprets text files with numbers, that are inserted in a binary tree. To build a binary tree out of a text file, type "treecheck filename".
After the insertion of all numbers into the tree, the program checks whether the tree is an AVL-tree or not.
The result is printed and if there is an AVL-violation, the number that causes it is shown in red followed by the text "AVL-violation".
When typing "treecheck filename1 filename2", the program builds a binary tree out of each file and then checks whether the second file is a subtree of the first or not.
This is done using a Simple Search method when the subtree consists of only one number, or a Subtree Search method when it has multiple nodes.
