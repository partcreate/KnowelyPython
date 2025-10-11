## `datetime`

Dieses Modul ähnelt `time`, bietet aber zusätzlich die Möglichkeit, sowohl mit der Uhrzeit als auch mit dem Datum zu arbeiten. Wir importieren es wie folgt:

```python
import datetime
```

Die Funktion `datetime.datetime.now()` gibt das aktuelle Datum und die aktuelle Uhrzeit zurück. Wir können spezifische Informationen aus dem zurückgegebenen Wert abrufen, zum Beispiel den Tag, die Minute usw.:

```python
from datetime import datetime

today = datetime.now()	

print(today)			# 2022-09-28 14:04:34.464598
print(today.date())		# 2022-09-28
print(today.time())		# 14:04:34.464598

print(today.day)		# 28
print(today.month)		# 9
print(today.year)		# 2022
print(today.hour)		# 14
print(today.minute)		# 4
print(today.second)		# 34
```

Um eine Zeitspanne (Tage, Stunden, Jahre), die seit einem Datum vergangen ist, zu berechnen, verwenden wir die Funktion `.timedelta()`, wobei wir die zu berechnende Zeiteinheit und ihren Wert angeben:

```python
import datetime

current_date = datetime.datetime.now()

print(current_date)                                 # 2022-09-28 14:12:16.805400
print(current_date+datetime.timedelta(days=1))     # 2022-09-29 14:12:16.805400
print(current_date-datetime.timedelta(days=1))    	# 2022-09-27 14:12:16.805400
print(current_date+datetime.timedelta(hours=5))     # 2022-09-28 19:12:16.805400
print(current_date-datetime.timedelta(minutes=3))   # 2022-09-28 14:09:16.805400
```

Wir können ein Datum in einen String konvertieren, ohne es als Klasseninstanz zu verwenden:

```python
current_date = datetime.datetime.now()
print(str(current_date))	# 2022-09-28 14:15:21.546316
```

Um das Erscheinungsbild eines Strings zu ändern, verwenden wir die Funktion `datetime.strftime()`:

```python
current_date = datetime.datetime.now()

print(current_date.strftime("%A, %I:%M%p"))           # Wednesday, 02:16PM
print(current_date.strftime("%A, %d %B %I:%M"))       # Wednesday, 28 September 02:16
print(current_date.strftime("%I:%M%p %d/%B/%Y"))    	# 02:16PM 28/September/2022
```

Die Funktion `datetime.strptime()` konvertiert einen String in ein `datetime`-Objekt:

```python
current_date = datetime.datetime.now()

print(current_date.strptime("02:16PM 28/September/2022", "%I:%M%p %d/%B/%Y"))  
# 2022-09-28 14:16:00
```

Und die Methode `.utcnow()` ruft die UTC-Zeit (Coordinated Universal Time) ab:

```python
from datetime import datetime


today = datetime.now()
print(today)			# 2022-09-28 12:24:54.921541
today_by_utc = datetime.utcnow()
print(today_by_utc)		# 2022-09-28 09:24:54.921558
```

```
```