Hier ist der konvertierte Markdown-Code aus dem von Ihnen bereitgestellten HTML:

[](https://www.google.com/search?q=%23shallow-and-deep-copy)

## Shallow and Deep Copy

In Python kopieren Zuweisungsanweisungen keine Objekte; sie erstellen eine neue Variable, die auf das ursprüngliche Objekt verweist. Daher müssen wir das Modul `copy` verwenden, das Werkzeuge für **sowohl tiefes als auch flaches Kopieren** enthält. Eine *flache Kopie* erstellt ein neues Objekt, das Verweise auf die untergeordneten Objekte des Originals speichert, um sicherzustellen, dass Änderungen an der Kopie das Originalobjekt nicht beeinflussen.

Lassen Sie uns Objektverweise und flache Kopien anhand von zwei Beispielen vergleichen. Zuerst der Objektverweis:

```python
original_object = [1, 2, 3]
copied_object = original_object

print(original_object) # [1, 2, 3]
print(copied_object)    # [1, 2, 3]

print(id(original_object))	# 4301497856
print(id(copied_object))	# 4301497856

copied_object.append(4)

print(original_object) # [1, 2, 3, 4]
print(copied_object)    # [1, 2, 3, 4]
```

Ein Beispiel für die Verwendung einer flachen Kopie:

```python
import copy

original_object = [1, 2, 3]
copied_object = copy.copy(original_object)

print(original_object)	# [1, 2, 3]
print(copied_object)	# [1, 2, 3]

print(id(original_object))	# 4349772672
print(id(copied_object))	# 4349736896

copied_object.append(4)

print(original_object)	# [1, 2, 3]
print(copied_object)	# [1, 2, 3, 4]
```

Dieses Beispiel zeigt, dass bei einer flachen Kopie das Ändern der untergeordneten Kopie (`copied_object`) die übergeordnete Kopie (`original_object`) nicht beeinflusst. Bei einer flachen Kopie wird im Gegensatz zu einem Verweis ein neues Objekt mit einer neuen ID erstellt.

Wenn wir beide Objekte vollständig unabhängig voneinander halten möchten, müssen wir eine *tiefe Kopie* mit `deepcopy()` verwenden, die eine verschachtelte Kopie durchführt. Das Kopieren einer Liste von Klasseninstanzen mit einer tiefen Kopie erstellt beispielsweise eine neue Liste mit vollständig neuen Instanzen. Um eine tiefe Kopie zu erstellen, müssen wir die Funktion `deepcopy()` verwenden:

```python
import copy

original_object = [1, 2, [3]]
copied_object = copy.deepcopy(original_object)

print(original_object)	# [1, 2, [3]]
print(copied_object)	# [1, 2, [3]]

print(id(original_object))	# 4372153216
print(id(copied_object))	# 4372117440


print(id(original_object[2]))	# 4377412480
print(id(copied_object[2]))		# 4377412864
```

Wie gezeigt, haben die gleichen Objekte in der Liste unterschiedliche IDs.