
## **Was ist eine Hash-Tabelle?**

Eine Hash-Tabelle (Hash Table) ist eine Datenstruktur, die dazu dient, Schlüssel-Wert-Paare schnell einzufügen, nachzuschlagen und zu entfernen. Sie basiert auf dem **Hashing-Konzept**, bei dem jeder Schlüssel mittels einer Hash-Funktion in einen eindeutigen Index in einem Array umgewandelt wird. Der Index dient als Speicherort für den entsprechenden Wert. Einfacher ausgedrückt, sie bildet die Schlüssel auf den Wert ab.



---

## Was ist der Lastfaktor (Load Factor)?

Der Lastfaktor einer Hash-Tabelle wird durch das Verhältnis der dort gespeicherten Elemente zur Größe der Tabelle bestimmt. Ist der Lastfaktor hoch, kann die Tabelle überladen sein, was zu längeren Suchzeiten und Kollisionen führen kann. Ein idealer Lastfaktor kann durch eine gute Hash-Funktion und die richtige Größenanpassung der Tabelle (Table Resizing) aufrechterhalten werden.

---

## Was ist eine Hash-Funktion?

Eine Funktion, die Schlüssel in Array-Indizes übersetzt, wird als Hash-Funktion bezeichnet. Eine gute Hash-Funktion sollte die Schlüssel gleichmäßig über das Array verteilen, um Kollisionen zu reduzieren und schnelle Zugriffszeiten zu gewährleisten.

1. **<ins>Integer universe assumption:</ins>** Die Annahme des Ganzzahl-Universums geht davon aus, dass die Schlüssel Ganzzahlen innerhalb eines bestimmten Bereichs sind. Dies ermöglicht die Verwendung einfacher Hash-Operationen wie Divisions- oder Multiplikations-Hashing.
2. **<ins>Hashing by division:</ins>** Diese unkomplizierte Hashing-Technik verwendet den Restwert des Schlüssels nach der Division durch die Größe des Arrays als Index. Sie funktioniert gut, wenn die Array-Größe eine Primzahl ist und die Schlüssel gleichmäßig verteilt sind.
3. **<ins>Hashing by multiplication:</ins>** Bei dieser einfachen Hashing-Operation wird der Schlüssel mit einer Konstante zwischen 0 und 1 multipliziert, bevor der gebrochene Teil des Ergebnisses genommen wird. Danach wird der Index durch Multiplikation des gebrochenen Teils mit der Größe des Arrays bestimmt. Auch diese Funktion funktioniert effektiv, wenn die Schlüssel gleichmäßig verteilt sind.

### [Choosing a hash function](https://www.geeksforgeeks.org/dsa/what-are-hash-functions-and-how-to-choose-a-good-hash-function/)

Die Wahl einer geeigneten Hash-Funktion hängt von den Eigenschaften der Schlüssel und der beabsichtigten Funktionalität der Hash-Tabelle ab. Es ist entscheidend, eine Funktion zu verwenden, die die Schlüssel gleichmäßig verteilt und Kollisionen reduziert.

<br>

**Kriterien, nach denen eine Hash-Funktion ausgewählt wird:**

1. Um sicherzustellen, dass die Anzahl der Kollisionen auf ein Minimum reduziert wird, sollte eine gute Hash-Funktion die Schlüssel gleichmäßig über die Hash-Tabelle verteilen. Das bedeutet, dass die Wahrscheinlichkeit, dass zwei Schlüssel auf dieselbe Position in der Tabelle gehasht werden, für alle Schlüsselpaare ziemlich konstant sein sollte.
2. Die Hash-Funktion sollte **recheneffizient** sein, um schnelles Hashing und Abrufen von Schlüsseln zu ermöglichen.
3. Es sollte **schwierig** sein, den Schlüssel aus seinem Hash-Wert abzuleiten. Dadurch wird die Wahrscheinlichkeit verringert, dass Versuche, den Schlüssel anhand des Hash-Werts zu erraten, erfolgreich sind.
4. Eine Hash-Funktion sollte **flexibel** genug sein, um sich an Änderungen in den gehashten Daten anzupassen. Wenn sich beispielsweise die Größe oder das Format der gehashten Schlüssel ändert, muss die Hash-Funktion weiterhin ordnungsgemäß funktionieren.

### [Collision resolution techniques](https://www.geeksforgeeks.org/dsa/collision-resolution-techniques/)

Kollisionen treten auf, wenn zwei oder mehr Schlüssel auf denselben Array-Index verweisen. **Chaining (Separate Verkettung)**, **Open Addressing (Offene Adressierung)** und **Double Hashing (Doppeltes Hashing)** sind einige Techniken zur Behebung von Kollisionen.



<br>

1. **[Open addressing](https://www.geeksforgeeks.org/dsa/open-addressing-collision-handling-technique-in-hashing/):** Kollisionen werden durch die Suche nach dem nächsten freien Platz in der Tabelle behoben. Wenn der erste Slot bereits belegt ist, wird die Hash-Funktion auf die nachfolgenden Slots angewendet, bis einer frei ist. Es gibt verschiedene Möglichkeiten, diesen Ansatz zu verwenden, darunter **Double Hashing**, **Linear Probing** und **Quadratic Probing**.
2. **[Separate Chaining](https://www.geeksforgeeks.org/dsa/separate-chaining-collision-handling-technique-in-hashing/):** Bei der separaten Verkettung (Separate Chaining) ist für jeden Slot in der Hash-Tabelle eine verknüpfte Liste von Objekten vorhanden, die auf diesen Slot hashen. Zwei Schlüssel werden in die verknüpfte Liste aufgenommen, wenn sie auf denselben Slot hashen. Diese Methode ist recht einfach anzuwenden und kann mehrere Kollisionen bewältigen.
3. **[Robin Hood hashing](https://www.geeksforgeeks.org/dsa/robin-hood-hashing/):** Um die Länge der Kette zu verringern, werden Kollisionen beim Robin Hood Hashing durch den Austausch von Schlüsseln behoben. Der Algorithmus vergleicht den Abstand zwischen dem Slot und dem belegten Slot der beiden Schlüssel, wenn ein neuer Schlüssel auf einen bereits belegten Slot hasht. Der vorhandene Schlüssel wird durch den neuen ersetzt, wenn dieser näher an seinem idealen Slot liegt. Dadurch wird der vorhandene Schlüssel näher an seinen idealen Slot gebracht. Diese Methode neigt dazu, Kollisionen und die durchschnittliche Kettenlänge zu reduzieren.

### Dynamic resizing:

Diese Funktion ermöglicht es der Hash-Tabelle, sich in Abhängigkeit von der Anzahl der enthaltenen Elemente zu vergrößern oder zu verkleinern. Dies fördert einen idealen Lastfaktor und schnelle Zugriffszeiten.

---

## Beispielimplementierung einer Hash-Tabelle

Python, Java, C++ und Ruby sind nur einige der Programmiersprachen, die Hash-Tabellen unterstützen. Sie können zusätzlich zur Aufnahme in die Standardbibliothek auch als benutzerdefinierte Datenstruktur verwendet werden.

**Beispiel: hashIndex = key % noOfBuckets**
**Einfügen (Insert)**: Bewege dich zu dem Bucket, der dem oben berechneten Hash-Index entspricht, und füge den neuen Knoten am Ende der Liste ein.
**Löschen (Delete)**: Um einen Knoten aus der Hash-Tabelle zu löschen, berechne den Hash-Index für den Schlüssel, bewege dich zu dem Bucket, der dem berechneten Hash-Index entspricht, und durchsuche die Liste in diesem Bucket, um den Knoten mit dem angegebenen Schlüssel zu finden und zu entfernen (falls gefunden).

<p align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/chain-hashing-1.png" alt="Chain Hashing Beispiel" width="inherit" height="inherit">
</p>

Bitte beziehe dich für Details auf **[Hashing | Set 2 (Separate Chaining)](https://www.geeksforgeeks.org/dsa/separate-chaining-collision-handling-technique-in-hashing/)**.



```python
# Python3 program to implement hashing with chaining
BUCKET_SIZE = 7


class Hash(object):
    def __init__(self, bucket):
        # Number of buckets
        self.__bucket = bucket
        # Hash table of size bucket
        self.__table = [[] for _ in range(bucket)]

    # hash function to map values to key
    def hashFunction(self, key):
        return (key % self.__bucket)

    def insertItem(self, key):
        # get the hash index of key
        index = self.hashFunction(key)
        self.__table[index].append(key)

    def deleteItem(self, key):
        # get the hash index of key
        index = self.hashFunction(key)

        # Check the key in the hash table
        if key not in self.__table[index]:
            return

        # delete the key from hash table
        self.__table[index].remove(key)

    # function to display hash table
    def displayHash(self):
        for i in range(self.__bucket):
            print("[%d]" % i, end='')
            for x in self.__table[i]:
                print(" --> %d" % x, end='')
            print()


# Drive Program
if __name__ == "__main__":
    # array that contains keys to be mapped
    a = [15, 11, 27, 8, 12]

    # Create a empty has of BUCKET_SIZE
    h = Hash(BUCKET_SIZE)

    # insert the keys into the hash table
    for x in a:
        h.insertItem(x)

    # delete 12 from the hash table
    h.deleteItem(12) # Korrektur: sollte 12 statt x sein, basierend auf dem C++ und Java Code

    # Display the hash table
    h.displayHash()
```

```javascript
class Hash {
    constructor(V) {
        this.BUCKET = V; // No. of buckets
        this.table = new Array(V); // Pointer to an array containing buckets
        for (let i = 0; i < V; i++) {
            this.table[i] = new Array();
        }
    }

    // inserts a key into hash table
    insertItem(x) {
        const index = this.hashFunction(x);
        this.table[index].push(x);
    }

    // deletes a key from hash table
    deleteItem(key) {
        // get the hash index of key
        const index = this.hashFunction(key);

        // find the key in (index)th list
        const i = this.table[index].indexOf(key);

        // if key is found in hash table, remove it
        if (i !== -1) {
            this.table[index].splice(i, 1);
        }
    }

    // hash function to map values to key
    hashFunction(x) {
        return x % this.BUCKET;
    }

    // function to display hash table
    displayHash() {
        for (let i = 0; i < this.BUCKET; i++) {
            let str = `${i}`;
            for (let j = 0; j < this.table[i].length; j++) {
                str += ` --> ${this.table[i][j]}`;
            }
            console.log(str);
        }
    }
}

// Driver program 
const a = [15, 11, 27, 8, 12];
const n = a.length;

// insert the keys into the hash table
const h = new Hash(7);    // 7 is count of buckets in hash table
for (let i = 0; i < n; i++) {
    h.insertItem(a[i]);
}

// delete 12 from hash table
h.deleteItem(12);

// display the Hash table
h.displayHash();
```

<br>**Output**

```
0
1 --> 15 --> 8
2
3
4 --> 11
5
6 --> 27
```

-----

## Komplexitätsanalyse einer Hash-Tabelle:

Hash-Tabellen haben eine durchschnittliche Zeitkomplexität von **O(1)** für Such-, Einfüge- und Löschvorgänge. Im **schlimmsten Fall** können diese Operationen jedoch **O(n)** Zeit erfordern, wobei *n* die Anzahl der Elemente in der Tabelle ist.

-----

## Anwendungen einer Hash-Tabelle:

  * Hash-Tabellen werden häufig zum **Indizieren und Suchen** großer Datenmengen verwendet. Eine Suchmaschine könnte beispielsweise eine Hash-Tabelle verwenden, um die von ihr indizierten Webseiten zu speichern.
  * Daten werden in der Regel über Hash-Tabellen im **Speicher zwischengespeichert (cached)**, was einen schnellen Zugriff auf häufig verwendete Informationen ermöglicht.
  * Hash-Funktionen werden in der **Kryptographie** häufig verwendet, um digitale Signaturen zu erstellen, Daten zu validieren und die Datenintegrität zu gewährleisten.
  * Hash-Tabellen können zur Implementierung von **Datenbank-Indizes** verwendet werden, was einen schnellen Zugriff auf Daten basierend auf Schlüsselwerten ermöglicht.

-----