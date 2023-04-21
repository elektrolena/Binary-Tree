class TreeNode:
    # KONSTRUKTOR
    def __init__(self, val=None):       # __init__ ist ein das gleiche wie ein Konstruktor in C++
                                        # self bezieht sich auf das Objekt selbst, das gerade ertellt wird
                                        # wenn val nicht angegeben wird, wird der Knoten auf None initialisiert
        self.val = val                  # Variable val wird gesetzte
        self.left = None                # linkes "Kind" des Knotens..werden vorerst auf NULL/None initialisiert
        self.right = None               # rechtes "Kind" des Knotens

    # INSERT METHODE
    def insert(self, val):          # Methode, die einen neuen Knoten mit dem Wert val in den binären Suchbaum einspeichert
        if self.val is None:        # ist der Knoten leer? --> wenn der Knoten noch nicht definiert ist
            self.val = val          # dann wird val gesetzt
            return self             # und der Knoten zurückgegeben
        elif self.val == val:       # existiert der Integerwert bereits im Baum, wird der Knoten nicht eingefügt und zurückgegeben
            return self             # Knoten wird nicht eingefügt und einfach zurückgegeben
        elif self.val > val:        # ist der einzufügende Wert kleiner als der aktuelle Knoten
            if self.left is None:   # dann wird gefragt, ob der linke Arm des akuellen Knotens leer ist
                self.left = TreeNode(val)   # Wenn ja, wird am linken arm des aktuellen Knotens der neue Knoten mit dem val erstellt
                return self.left    # und dann zurückgegeben
            else:                   # wenn links schon ein Knoten ist
                return self.left.insert(val)  # wenn nicht, wird die insert funktion mit dem neuen Knoten am linken Arm aufgerufen
        else:                       # ist der einzufügende Wert größer als der aktuelle Knoten
            if self.right is None:  # dann wird gefragt, ob der rechte Arm des aktuellen Knotens leer ist
                self.right = TreeNode(val)  # wenn ja, wird ein neuer Knoten am rechten arm erstellt
                return self.right
            else:                   # wenn rechts schon ein Knoten ist
                return self.right.insert(val)  # wird die Funktion nochmal mit dem neuen rechten Knoten aufgrerufen
