# RoboTel TwinCAT firmware repository

[![Build Status](https://travis-ci.com/weingrill/RoboTel.svg?branch=master)](https://travis-ci.com/weingrill/RoboTel)

The online manual can be found here:

https://weingrill.github.io/RoboTel/index.html

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
* Hauptschranklüfter über Relais (WB)

# Programmierhinweise
* MC_SetAcceptBlockedDriveSignal verfaehrt den Antrieb aus der Endlage
* MC_ExtSetPointGenFeed -Enable / -Disable fuer externen Sollwertgenerator

# Informations
## Probe Unit / Homing
[https://infosys.beckhoff.com/index.php?content=../content/1031/ax5000_usermanual/html/AX5000_Homing_ProbeUnit.htm]
