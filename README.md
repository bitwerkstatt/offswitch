# offswitch.py
Python-Skript, dass die Spannung an einem PIN überwacht und bei Abfall einen Shutdown triggert.

# Installation



## Erstellen einer Service-Datei

```
sudo nano /etc/systemd/system/offswitch.service
```

## Inhalt der Datei

```
[Unit]
Description=Shutdown Button Script
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/offswitch.py #Achtung: Pfad auf den tatsächlichen Ort anpassen
WorkingDirectory=/home/pi/ #oder Home-Verzeichnis Deines Users
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi #Falls Du den geändert hast, dann stattdessen Deinen Nutzernamen

[Install]
WantedBy=multi-user.target
```

## Service aktivieren und starten

```
sudo systemctl enable offswitch.service
sudo systemctl start offswitch.service
````

Das Skript wird nun bei jedem Systemstart automatisch mitgestartet.

# Schaltung

Anmerkung: Das Kommando pinout gibt die physischen Pins aus. Nicht alle PIs sind da gleich. Entscheidend ist, die richtigen Pins für GPIO2 und GND zu finden.

Die Schaltung ist sehr einfach, Du benötigst nur einen Taster (Momentary Switch).

Ein Beinchen des Tasters wird mit Pin 3 (GPIO2) verbunden.

Das andere Beinchen des Tasters wird mit einem Ground-Pin (GND) verbunden (z.B. Pin 6).

Wenn der Taster nicht gedrückt ist, hält der interne Pull-up-Widerstand den GPIO-Pin auf einem HIGH-Signal (3,3V). Sobald du den Taster drückst, wird der Stromkreis zu GND geschlossen, wodurch die Spannung am PIN auf 0V abfällt. Darauf reagiert das Skript.