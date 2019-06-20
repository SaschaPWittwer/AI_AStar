## AI Projekt Zenji
### by Sascha Wittwer, Yves Beutlus Navigatus and Joris Baiutti

### 1. Ansatz
Da wir die Aufgabe nicht richtig gelesen haben, haben wir im ersten Schritt den A* Algorithmus mit phython implementiert und das Resultat auf der Konsole ausgegeben.
```
X 1 0 0 1 0 1 0 0 0
X 1 0 0 1 0 1 0 0 0
X 1 0 0 X 0 1 0 0 0
X 1 0 X 1 X 1 0 0 0
X 1 X 0 1 X 1 0 0 0
X 1 X 0 1 X 1 0 0 0
X 1 X 0 1 X 1 0 0 0
X 1 X 0 1 X 1 0 0 0
0 X 0 0 1 0 X 0 0 0
0 0 0 0 1 0 0 X X X
```
Die "x" Werte stellen den gefundenen Weg dar.

**Todo: Describe Algorithm shortly**

### 2. Ansatz
In einem zweiten Versuch haben wir eine check field funktion implementiert welche ein Feld überprüft ob es einen Eingang und einen Ausgang hat. Falls
das Feld einen Eingang hat wird es solange gedreht (max 4) bis der Eingang zu einem Feld links oder oben, zu einem Ausgang passt.
