# shutdown_button_interrupt.py

import RPi.GPIO as GPIO
import os
import signal
import sys

# Definition des überwachten PINs 
shutdown_pin = 2 # GPIO2 ist der BCM-Name für Pin 3

# Callback-Funktion für den Shutdown-Button
def shutdown_callback(channel):
    GPIO.cleanup()
    os.system("sudo shutdown -h now")

try:
    # Verwende die BCM-Pin-Nummerierung
    GPIO.setmode(GPIO.BCM)

    # Richte den Pin als Eingang mit internem Pull-up-Widerstand ein,
    # Damit der Pin im Ruhezustand HIGH ist. Außerdem erspart das einen extra Widerstand in der Schaltung
    GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Füge den Event-Detektor hinzu, wenn die Spannung am PIN fällt, wird der Callback aufgerufen
    GPIO.add_event_detect(shutdown_pin, GPIO.FALLING, 
                          callback=shutdown_callback, 
                          bouncetime=300)

    # Das Skript wird hier in einen "Schlafzustand" versetzt und verbraucht fast keine CPU.
    # Es wartet auf Signale (wie den GPIO-Interrupt oder Strg+C).
    signal.pause()

except KeyboardInterrupt:
    print("\nAbbruch.")
finally:
    GPIO.cleanup()