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
In einem zweiten Versuch haben wir eine check field funktion implementiert welche ein Feld überprüft ob es einen Eingang und einen Ausgang hat.
Die Funktion prüft ob das Feld ein Nachbarfeld hat (oben und links), welches einen Ausgang hat, welcher auf einen Eingang beim aktuellen Feld passt.

```Python
def checkField(grid, row, column):
    if row == 0 and column == 0:
        if grid[row][column][0] == 1 and (grid[row][column][1] == 2 or grid[row][column][2] == 2):
            return True
        elif grid[row][column][3] == 1 and (grid[row][column][1] == 2 or grid[row][column][2] == 2):
            return True
        else:
            return False
    elif row-1 < 0 and column-1 >= 0:
        if grid[row][column][3] == 1 and grid[row][column-1][1] == 2:
            return True
        else:
            return False
    elif row-1 >= 0 and column-1 < 0:
        if grid[row][column][0] == 1 and grid[row-1][column][2] == 2:
            return True
        else:
            return False
    elif (grid[row][column][0] == 1 and grid[row-1][column][2] == 2) or (grid[row][column][3] == 1 and grid[row][column-1][1] == 2):
        return True
    else:
        return False
```

Diese Funktion haben wir auf jedem Feld ausgeführt und falls die Funktion ```False``` zurückgab, haben wir das Feld gedreht (max 4 mal).
Wir haben die Felder nicht systematisch geprüft, respektive wir sind Zeile für Zeile durchgegangen.
```
count = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        for y in range(4):
            if(checkField(grid, i, j) == True):
                break
            else:
                count += 1
                if (col[0] + col[1] + col[2] + col[3]) >= 3:
                    rotateRight(grid, i, j)
                else:
                    break
print("Rotation Count: " + str(count))
print("after:")
```
Es wurde ein Weg gefunden:
