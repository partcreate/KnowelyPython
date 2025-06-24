# Zusammenfassung: Git, GitHub, Windows und WSL/Debian Integration

Dieser Chat behandelt die Lösung von Authentifizierungsproblemen bei Git/GitHub-Operationen unter Windows, insbesondere wenn SSH-Schlüssel zuvor unter WSL/Debian verwendet wurden, und den initialen Push eines Projekts.

## 1. Problemstellung: "Permission denied (publickey)"

**Fehlermeldung:** `git@github.com: Permission denied (publickey). fatal: Could not read from remote repository.`

**Hauptursache:** Probleme mit SSH-Schlüsseln oder Zugriffsrechten.

**Häufige Gründe und Lösungen:**
* **Fehlende/Falsche SSH-Schlüssel:** Schlüssel nicht generiert, falscher Schlüssel verwendet, oder öffentlicher Schlüssel nicht korrekt bei GitHub hinterlegt.
    * **Lösung:** SSH-Schlüssel generieren (`ssh-keygen`), öffentlichen Schlüssel (`.pub`-Datei) zu GitHub-Einstellungen hinzufügen. Verbindung testen mit `ssh -T git@github.com`.
* **Falsche Repository-URL:** Falsche oder nicht berechtigte URL.
    * **Lösung:** `git remote -v` überprüfen. Sicherstellen, dass die URL die SSH-Form hat (`git@github.com:Benutzername/Repository.git`).
* **Fehlende Repository-Berechtigungen:** Das GitHub-Konto hat keine Schreibrechte.
    * **Lösung:** Berechtigungen prüfen, ggf. Fork erstellen.
* **SSH-Agent-Probleme:** Agent läuft nicht oder Schlüssel nicht geladen.
    * **Lösung:** Agent starten (`eval "$(ssh-agent -s)"`) und Schlüssel hinzufügen (`ssh-add ~/.ssh/id_rsa`).

## 2. SSH-Schlüssel von WSL nach Windows übertragen

**Ausgangslage:** SSH-Schlüssel liegen in WSL/Debian und sollen unter Windows (für PyCharm) genutzt werden.

**Schritte:**
1.  **SSH-Schlüssel in WSL finden:**
    * WSL-Terminal öffnen: `cd ~/.ssh`
    * Schlüssel auflisten: `ls -la` (suchen nach `id_rsa`, `id_rsa.pub` oder `id_ed25519`, `id_ed25519.pub`).
2.  **Verzeichnis in Windows erstellen (falls nicht vorhanden):**
    * `mkdir -p /mnt/c/Users/<DeinWindowsBenutzername>/.ssh`
3.  **Schlüssel nach Windows kopieren:**
    * `cp id_rsa /mnt/c/Users/<DeinWindowsBenutzername>/.ssh/id_rsa`
    * `cp id_rsa.pub /mnt/c/Users/<DeinWindowsBenutzername>/.ssh/id_rsa.pub`
    * (Analog für `id_ed25519`-Schlüsselpaare).

## 3. Git unter Windows für SSH konfigurieren

**Voraussetzung:** "Git for Windows" ist installiert.

**Schritte:**
1.  **SSH-Agent starten und Schlüssel hinzufügen:**
    * `Git Bash` öffnen (aus dem Startmenü).
    * Agent starten: `eval "$(ssh-agent -s)"`
    * Schlüssel hinzufügen: `ssh-add ~/.ssh/id_rsa` (oder den Namen Ihres Schlüssels).
    * *Hinweis:* Der Agent läuft nur für die aktuelle Sitzung; für Persistenz sind weitere Schritte nötig (z.B. Autostart-Skript).
2.  **SSH-Verbindung von Windows testen:**
    * Im `Git Bash` oder `PowerShell`: `ssh -T git@github.com`
    * Erwartete Ausgabe: "Hi [Ihr Benutzername]! You've successfully authenticated..."

## 4. PyCharm Konfiguration für Git unter Windows

PyCharm nutzt die systemweite Git- und SSH-Konfiguration.

**Einstellungen in PyCharm (`File -> Settings -> Version Control -> Git`):**
* **Path to Git executable:**
    * Sollte auf die eigentliche Git-Executable unter Windows zeigen: `C:\Program Files\Git\bin\git.exe`.
    * **Nicht** `git-bash.exe` oder `git-cmd.exe` verwenden, da dies Shells sind, nicht der Git-Client selbst.
* **SSH executable:**
    * Auf **"Native"** einstellen. Dies weist PyCharm an, den SSH-Client des Betriebssystems zu verwenden, der die Schlüssel aus dem Windows-`~/.ssh`-Verzeichnis liest.
* **Repository-URL:** Sicherstellen, dass das Remote-Repository die SSH-Form hat: `git@github.com:Benutzername/Repository.git`.

## 5. Initialer Projekt-Push auf ein leeres (oder README-Repo)

**Problem:** Git fordert einen `git pull`, obwohl das lokale Projekt die "richtige" Version ist und das GitHub-Repo nur eine `README.md` enthält. Ein normaler `pull` würde die lokale Historie mit der Remote-Historie vermischen.

**Lösung:** Initialer `git push --force` (oder `--force-with-lease`).

**Schritte:**
1.  **Lokales Projekt vorbereiten:**
    * Alle Dateien sind hinzugefügt (`git add .`) und committet (`git commit -m "Initial commit"`).
    * Im PyCharm-Terminal: `git status` überprüfen.
2.  **Remote-Repository hinzufügen (falls nicht geschehen):**
    * `git remote add origin git@github.com:IhrBenutzername/IhrRepositoryName.git`
    * Überprüfen mit `git remote -v`.
3.  **Initialen Force Push ausführen (im PyCharm-Terminal):**
    * **WICHTIG:** `git push --force origin main`
    * *Alternativ (sicherer bei Kollaboration, hier aber egal):* `git push --force-with-lease origin main`
    * Falls der Upstream-Branch noch nicht gesetzt ist: `git push --force --set-upstream origin main`
    * Dieser Befehl überschreibt die Historie im Remote-Repo mit der lokalen Historie.
    * **Vorsicht:** Force Push sollte nur verwendet werden, wenn Sie sicher sind, dass Sie die Remote-Historie überschreiben möchten.

**Ergebnis:** Das Projekt ist erfolgreich von Windows aus über SSH auf GitHub gepusht worden. Zukünftige Pushes können mit `git push origin main` erfolgen.