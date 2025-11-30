[](#table-resize)

## Table Resize

Die anfängliche Größe der Tabelle beträgt `8` Zellen und sie muss wachsen, wenn sie zu mehr als `2/3` voll wird. 
In Python verdoppelt sich eine Hash-Tabelle in der Größe, wenn sie `2/3` ihrer Kapazität überschreitet. 
Die alten Werte werden neu gehasht und in einer neuen Tabelle platziert, wobei Schlüssel und Werte erhalten bleiben, sich aber die Indizes ändern.

Wie wir bereits erwähnt haben, beträgt die anfängliche Größe der Tabelle 8 Zellen. Und es ist ziemlich logisch anzunehmen, dass die Größe irgendwann zunehmen sollte. 
Aber dann stellt sich die Frage – wann und um wie viel?

In Python haben Hash-Tabellen die Eigenschaft, dass sie sich um den Faktor 2 vergrößern, wenn die Tabelle zu mehr als ⅔ ihrer Größe gefüllt ist. Wie das passiert:

* number of elements = ⅔ * table size + 1 (dasselbe wie number of elements > ⅔ * table size);
* die Größe der Tabelle wird verdoppelt;
* alte Werte werden einzeln aufgezählt (Schlüssel und Wert bleiben erhalten, aber der Index ändert sich).