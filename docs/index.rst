.. RoboTel documentation master file, created by
   sphinx-quickstart on Thu Jan 21 16:06:06 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RoboTel Firmware documentation
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   safety
   init
   manual
   automatic
   hydraulics
   filterwheel
   focus
   dome
   covers
   derotator
   pointing

Introduction
------------
RoboTel was build by Halfmann and upgraded by AIP in 2020/2021. All important
electronic components have been replaced by Beckhoff modules.
A central Beckhoff PLC controls the servo controllers, DC controllers,
temperature sensors and digital I/Os.

**Please read the :doc:`safety` before operating the telescope.**

RoboTel is a robotic telescope, which means that it is either operated remotly
or autonomous.
It has limited capabilities to be operated by hand mainly for maintenance, testing
and commissioning.
There are several levels of protection to prevent remote operation of the telescope.

#. Pressing the emergency stop deactivates all electric circuits and all motors.
#. Deactivating the brake clearance prevents movement of azimuth and elevation.
#. Turning the power switch to off also prevents movement of azimuth and elevation.
#. Switching to manual operation on the pendant control overrides remote operation.

*Be aware that many settings except for the emergency stop can be enforced by the
TwinCAT3 IDE in debugging mode.*

Logical Structure
-----------------
The telescope electronics have been split up into several components for security,
safety and design reasons.

Main Cabinet
^^^^^^^^^^^^
The main cabinet contains the main PLC and the high voltage components for the
servo drivers, which are also situated here. Azimuth, elevation and de-rotator
drives are powered and controlled from here as well as the hydraulic system.
The yellow modules are responsible for the safety system TwinSAFE.

The other subsystems like the telescope cabinet and the weather station are connected
here using EtherCAT over fibre connections.

The main cabinet features the following controls on the side:

* green button: start the hydraulic pumps
* red button: stop the hydraulic pumps
* black button: reset the TwinSAFE system if power key is off otherwise reset an error.
* white light: indicates if power is ready
* brake clearance: open (I) or lock (O) the brake for azimuth and elevation.
* power key: enable high power for the drives.
* red light: indicates an error.
* emergency stop button: deactivate all systems

Telescope Cabinet
^^^^^^^^^^^^^^^^^
The small cabinet at the telescope contains all DC drivers for the covers, M2(focus)
and M3 (Nasmyth mirror). It also interfaces all temperature sensors and digital
inputs for the limit switches.

An EtherCAT fibre link connects to the dome control.

Dome Control
^^^^^^^^^^^^
The dome azimuth and the dome shutters are controlled from here. See also :doc:`dome`

Weather Station
^^^^^^^^^^^^^^^
The weather station has analog inputs for the wind, temperature und humidity
sensors and a digital input for the rain sensor.

Design issues
-------------
The RoboTel telescope has some design flaws originating from the original design
by Halfmann. See :doc:`issues` for a detailed analysis and potential upgrades of
the system.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
