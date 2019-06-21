## AI Projekt Zenji
### by Sascha Wittwer, Yves Beutler and Joris Baiutti

### 1. Ansatz
Um einen Einblick in die Problematik zu erlangen, haben wir als erstes eine einfache Implementation des A* Algorithmus gemacht. Dies gab uns gewisse Einblicke wie wir die gestellte Aufgabe angehen könnten.

Wir haben also eine rudimentäre Implementation des Algorithmus selbst in Python implementiert.
Als Input haben wir ein einfaches 10x10 Grid verwendet welches 0 und 1 Werte beinhaltete.
Ein 0 Wert stand für passierbare Felder während eine 1 ein nicht passierbares Feld kenzeichnet.
Das Test-Grid wurde von uns statisch zur verfügung gestellt und nicht etwa zufällig generiert.
Das haben wir so gewählt um die Komplexität zu senken da es "nur" eine Einführung in die Problemstellung geben sollte.

Unser gewähltes Test-Grid sah also wie folgt aus:
```
0 1 0 0 1 0 1 0 0 0
0 1 0 0 1 0 1 0 0 0
0 1 0 0 0 0 1 0 0 0
0 1 0 0 1 0 1 0 0 0
0 1 0 0 1 0 1 0 0 0
0 1 0 0 1 0 1 0 0 0
0 1 0 0 1 0 1 0 0 0
0 1 0 0 1 0 1 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
```
Unsere A* Implementation sollte nun einen bestmöglichen Weg von Punkt A nach Punkt B finden.
Dies funktionierte nach einigen Entwicklungs-Iterationen nicht schlecht und so konnten wir folgendes Ergebnis erzielen:

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
Die "X" Werte stellen den gefundenen Weg dar.

Diese erste Implementation des A* half uns sehr gut die Problemstellung zu verstehen und gab uns Einsicht in Punkte welche wir für die folgenden Aufgaben berücksichtigen müssen.

### 2. Ansatz
In einem zweiten Versuch haben wir eine check field Funktion implementiert, welche ein Feld überprüft, ob es einen Eingang und einen Ausgang hat.
Die Funktion prüft ob das Feld ein Nachbarfeld hat (oben und links), welches einen Ausgang hat, welcher auf einen Eingang beim aktuellen Feld passt.

```python
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
```python
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

Vorher:
```
-------  -------  -------  -------
|  1  |  |  1  |  |  0  |  |  0  |
| 0 2 |  | 2 0 |  | 0 0 |  | 0 0 |
|  0  |  |  0  |  |  0  |  |  0  |
-------  -------  -------  -------
-------  -------  -------  -------
|  0  |  |  0  |  |  1  |  |  0  |
| 0 0 |  | 2 1 |  | 2 0 |  | 0 0 |
|  0  |  |  0  |  |  0  |  |  0  |
-------  -------  -------  -------
-------  -------  -------  -------
|  0  |  |  1  |  |  0  |  |  0  |
| 0 0 |  | 0 0 |  | 0 0 |  | 0 0 |
|  0  |  |  2  |  |  0  |  |  0  |
-------  -------  -------  -------
-------  -------  -------  -------
|  0  |  |  1  |  |  0  |  |  0  |
| 0 0 |  | 0 2 |  | 1 2 |  | 1 0 |
|  0  |  |  0  |  |  0  |  |  0  |
-------  -------  -------  -------
```
Nachher:
```
-------  -------  -------  -------
|  1  |  |  0  |  |  0  |  |  0  |
| 0 2 |  | 1 0 |  | 0 0 |  | 0 0 |
|  0  |  |  2  |  |  0  |  |  0  |
-------  -------  -------  -------
-------  -------  -------  -------
|  0  |  |  1  |  |  1  |  |  0  |
| 0 0 |  | 0 0 |  | 2 0 |  | 0 0 |
|  0  |  |  2  |  |  0  |  |  0  |
-------  -------  -------  -------
-------  -------  -------  -------
|  0  |  |  1  |  |  0  |  |  0  |
| 0 0 |  | 0 0 |  | 0 0 |  | 0 0 |
|  0  |  |  2  |  |  0  |  |  0  |
-------  -------  -------  -------
-------  -------  -------  -------
|  0  |  |  1  |  |  0  |  |  0  |
| 0 0 |  | 0 2 |  | 1 2 |  | 1 0 |
|  0  |  |  0  |  |  0  |  |  0  |
-------  -------  -------  -------
```

### 3. Ansatz Tiefensuche
Im 3. Ansatz wollten wir einen Weg ein bisschen systematischer finden. Wir haben eine Funktion implementiert, welche überprüft ob sie einen Eingang zum vorherigen Feld hat und ob dann ein Ausgang entweder nach unten, nach rechts oder beides zeigt. Das Feld wird solange gedreht (max 4) bis der Eingang zum vorherigen Feld passt.
Wenn kein Eingang gefunden wird, wird abgebrochen. Falls ein Eingang und Ausgänge gefunden werden, wird für jeden Ausgang die gleiche Funktion rekursiv aufgerufen und das anliegende Feld mitgegeben. Zudem wird noch der Ausgang mitgegeben, damit die Funktion weiss,welcher Eingang beim neuen Feld überprüft werden muss. Die Rekursion hört auf, wenn kein Weg gefunden wurde oder wenn das Ziel erreicht wurde.

```python
def depthSearch(waterFrom, row, column, grid):
    # check goal state
    if (len(grid[row]) == row) and (len(grid[row][column]) == column):
        return 1
    
    # check borders
    if (len(grid) < row) or (len(grid) < column):
        return -1

    # rotate max 3 times
    for _i in range(4):
        if grid[row][column][waterFrom] == 1:
            if grid[row][column][1] == 2:
                # go right
                depthSearch(3, row, column+1, grid)
            if grid[row][column][2] == 2:
                # go down
                depthSearch(0, row+1, column, grid)
        else:
            rotateRight(grid, row, column)
    # this node is a dead end
    return -1
```

Auch so wurde ein Weg gefunden.

### 4. Ansatz Todo rotation count as cost
