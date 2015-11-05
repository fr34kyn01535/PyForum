# PyForum
Ein Forum welches für das Praktika WEB BI3 erstellt wurde.

##Autoren

    [@fr34kyn01535] - Sven - 975524

##Anforderungen
* im Forum werden Themen behandelt
  * zu jedem Thema kann es N Diskussionen geben
  * zu jeder Diskussion kann es M Beiträge geben
* es werden drei Rollen vorgesehen:
  * Rolle "Administrator"
    * gibt die Themen vor
    * kann alle Diskussionen und Beiträge bearbeiten und ggf. löschen (Ersetzen des Inhaltes mit einer Notiz das dieser entfernt ist)
    * pflegt die Benutzerkonten der Bearbeiter
    * kann einem Bearbeiter die Möglichkeit der Bearbeitung von Diskussionen / Beiträgen entziehen und wieder zuordnen
  * Rolle "Bearbeiter"
    * Benutzerkonto wird vom Administrator zugewiesen
    * kann neue Diskussionen zu einem Thema erstellen
    * kann neue Beiträge zu einer Diskussion erstellen
    * kann seine Beiträge ändern, solange es die jeweils jüngsten zu einer Diskussion sind
  * Rolle "Jedermann"
    * benötigt kein Benutzerkonto
    * kann alle Beiträge aller Diskussionen zu allen Themen im Forum einsehen
* die Themen werden alphabetisch aufgelistet
* die Diskussionen werden nach Zeitpunkt aufgelistet; maßgebend ist der Zeitpunkt des ersten Beitrags
* Beiträge werden nach Zeitpunkt aufgelistet
* jeder Beitrag enthält zumindest folgende Angaben:
  * Bearbeiter (wird automatisch zugeordnet)
  * Zeitpunkt (wird automatisch gesetzt)
  * Titel (zwingend erforderlich)
  * Inhalt


##Abhängigkeiten:
* Python 3.5.0
* CherryPy 3.8.0
* Mako 1.0.3

