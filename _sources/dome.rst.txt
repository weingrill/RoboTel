Dome Operation
==============

The dome is operated by its own PLC but governed by the main PLC.
Closing or opening the dome requires approximately 70 seconds.

Manual Operation
----------------

The dome can always be operated by pressing a button on the two-button
control, directly connected to the azimuth dome control.

The second operating mode is by using the pendant control (selection 9).
* Buttons "←" and "→" rotate the dome counter-clockwise and clockwise.
* "RESET" resets the dome axis

API description
---------------

The dome is enabled automatically as soon as `TelescopeControl.power` is TRUE.
If the dome has not yet been calibrated, it moves to the calibration position.
If the calibration has been completed, the dome azimuth is tied to the
telescope azimuth.

* `DomeControl.Reset` resets the axis, after an error has occurred.
* `DomeControl.OpenDome` opens slit and flap.
* `DomeControl.CloseDome` closes slit and flap.
* `DomeControl.Light` alters the state of the dome illumination.
  The light is deactivated automatically after 60 minutes.

If the weather conditions are bad, the dome will be closed automatically.
If the Dome is opened, the dehumidifier is stopped.
