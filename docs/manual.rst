Manual Operation
================

The telescope can be operated manually for commissioning, testing or
observation. To enable manual operation:
* Turn the power switch on the main panel to "ON".
* Start the hydraulic system, if necessary.
* Turn the brake clearance to "ON".
* On the pendant control turn the manual key switch to "ON".

The manual operation overrides any remote command.

The selector switch (1-15) enables the individual components on the telescope.
It is advised to leave the manual switch in "OFF" position, while turning the selector.
Turning the selector in manual operation may cause drive errors.
If not otherwise noted, these general rules apply for all selections:
* "ENABLE" enables the drive. Pressing "ENABLE" a second time disables the drive.
* "RESET" resets the drive or error.
* Buttons that can be pressed are illuminated.
* When a limit switch is reached, the respective button is disabled.

1 Cover 1
---------
* Buttons "↑" and "↓" open and close the cover.

*Cover 1 is not installed on RoboTel.*

See also :doc:`covers`

2 Cover 2
---------

* Buttons "↑" and "↓" open and close the cover.
* Cover 3 must be opened first, for cover 2 to operate.

See also :doc:`covers`

3 Cover 3
---------

* Buttons "↑" and "↓" open and close the cover.
* Cover 2 has to be closed first.

See also :doc:`covers`

4 Nasmyth / Mirror M3 Control
-----------------------------

* "ENABLE" opens the lock.
* Buttons "←" and "→" rotate the mirror left and right.
* Moving the mirror without unlocking will cause in an error.
* "RESET" locks the mirror in position.

5 Focus
-------

The lock is opened as soon as the focus is manually selected.
* "ENABLE" executes the homing procedure.
* Buttons "↑" and "↓" move the mirror outwards and inwards.
* Moving the focus without unlocking will cause in an error.
* "RESET" locks the focus in position.

See also :doc:`focus`

6 De-rotator
------------

* "ENABLE" executes the homing procedure.
* Buttons "←" and "→" rotate the de-rotator counter-clockwise and clockwise.

See also :doc:`derotator`

7 Elevation
-----------

The hydraulic brake is opened, as soon as the drive is enabled to avoid a drive error.

* "ENABLE" enables/disables the drive.
* Buttons "↑" and "↓" increase and decrease the elevation.
* Pressing the buttons "↑" and "↓" simultaneously immediately closes the brake.
* Open the covers to ensure a balanced telescope, when activating the elevation manually.

**WARNING** Enabling the drive will automatically open the brake for both elevation
and azimuth.

8 Azimuth
---------

* "ENABLE" enables/disables the drive.
* Buttons "←" and "→" rotate the azimuth counter-clockwise and clockwise.

**WARNING** Enabling the azimuth also enables the elevation, since the break will be opened.

9 Dome Control
--------------
* Buttons "←" and "→" rotate the dome counter-clockwise and clockwise.
* Buttons "↑" and "↓" open and close the slit and the flap.

*Due to the design there is a latency of up to five seconds until the command
is executed. This also applies for pressing the emergency stop.*

**The emergency stop is not directly connected to the dome controls.**

10 Filter Wheel
---------------

* "ENABLE" executes the homing procedure.
* Buttons "←" and "→" rotate the filter wheel counter-clockwise and clockwise.
* If homing has been performed successfully, the buttons "↑" and "↓" increase
  and decrease the filter number from 0 to 23.

See also :doc:`filterwheel`

12 Semi automatic operation II
------------------------------

* Button "↓" issues a `gohome` command.
* Button "↑" issues a `park` command.
* Button "→" issues a `goto` command.
* "ENABLE" toggles the tracking command.
* "RESET" issues a `stop` command.

See also :doc:`automatic` for a detailed description for each command.

13 Semi automatic operation I
-----------------------------

* "ENABLE" activates the power signal in the `TelescopeControl`.
* Buttons "←" and "→" decrease or increase the azimuth offset.
* Buttons "↑" and "↓" decrease or increase the elevation offset.
* Switching to "MANUAL" calculates the new right ascension and declination
  based on the current telescope position.

14 unused
---------

Use this setting for automatic operation.
Enabling the manual operation mode will sound the horn as a warning.

15 Hydraulics
-------------

* "ENABLE" starts/stops the hydraulic system.
* The button "↑" opens (releases) the brake.
* The button "↓" closes (locks) the brake.
* The lamp "←" indicates that the main pump is running.
* The lamp "→" indicates that the suction pump is running.
* The lamp "↑" indicates an open brake.
* The lamp "↓" indicates a closed brake.

**To immediately stop the hydraulic system press the emergency button.**

See also :doc:`hydraulics`
