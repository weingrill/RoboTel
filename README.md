# RoboTel TwinCAT firmware repository

# Bedienungsanleitung Handsteuerung
Für alle nachfolgenden Punkte ist es notwendig, dass die Leistung auf "ein" steht und der Wahlschalter der Handsteuerung auf "Manual".

1. Klappe 1 (bei RoboTel nicht vorhanden)
2. Klappe 2
3. Klappe 3
4. Nasmyth/M3: Enable/Reset öffnet und schließt Bremse
5. Fokus: Enable/Reset öffnet und schließt Bremse
6. Derotator
7. Elevation
8. Azimut
9. Dome
10. Filterrad (noch nicht implementiert)
11. reserviert
12. reserviert
13. reserviert
14. reserviert
15. Hydraulik: Enable = Hydraulik start; Reset = Hydraulik stop; Auf = Bremse auf; Ab = Bremse zu: Links zeigt Betrieb der Vorlaufpumpe an; Rechts = Betrieb Rücklauf

**Vor Programm 7 oder 8 Bremse lösen!**
In Programmen 1-9 löscht "Reset" etwaige Motorfehler. (Fehleranzeige an Handsteuerung defekt)



# ToDo
* Glasfasern in Triflexkette einziehen (MW+FT)
* RoboTel Server mit InfluxDB+Grafana (Dockercontainer?) (AJ)
* Software (JW+TG)
* Homing Focus
* Homing Azimut
* Homing Elevation
* Homing FilterWheel
* Homing Derotator

## Optional:
* Hauptschranklüfter über Ralais (WB)

# Programmierhinweise
* MC_SetAcceptBlockedDriveSignal verfaehrt den Antrieb aus der Endlage
* MC_ExtSetPointGenFeed -Enable / -Disable fuer externen Sollwertgenerator

# Informations
## Probe Unit / Homing
[https://infosys.beckhoff.com/index.php?content=../content/1031/ax5000_usermanual/html/AX5000_Homing_ProbeUnit.htm]
