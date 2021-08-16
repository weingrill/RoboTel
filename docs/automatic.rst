Remote or Robotic Operation
===========================

The telescope is primarily designed to be operated remotely or robotic. The main
interface is the Beckhoff ADS connection to the `TelescopeControl` by setting the
respective variables listed below. Since the ADS communication cycle is in the
order of tens of seconds this can be considered a realtime interface.

The following conditions have to be met for remote or robotic operations:

#. The main power switch is turned ON.
#. The brake clearance is OPEN (ON).
#. The pendant control has the `MANUAL` set to `OFF`.
#. The selector on the pendant control is in setting 15, 14 or 11.

API Description
---------------

Since ADS does not implement protected variables, specific input and output
variables have been defined.

Input Variables
^^^^^^^^^^^^^^^

* `power`: activates the the telescope.
  The telescope performs the following actions:

  #. activate the hydraulic pumps (:doc:`hydraulics`)
  #. opens the covers (:doc:`covers`)
  #. enable the elevation and azimuth
  #. enable the dome, if available (:doc:`dome`)
  #. enable the de-rotator (:doc:`derotator`)
  #. enable the filterwheel (:doc:`filterwheel`)
  #. enable the focuser (:doc:`focus`)

  If the `power` command is issued for the first time after a hardreset or
  power-cycle, the calibation cycle for each axis will be performed.
  When disabling the `power` signal the axes will be disabled in reverse order
  and the covers will be closed.
* `gohome`: The telescope moves to the hard-coded home position. Azimuth 180 degrees
  and elevation 45 degrees.
* `park`: the telescope moves to the hard-coded parking position and closes the
  covers. After reaching the parking position, the telescope is powered down.
* `ra`: new right ascension. Issue a `goto` command to move the telescope there.
* `de`: new declination. Issue a `goto` command to move the telescope there.
* `track`: start tracking at the current position. This operates the elevation,
  azimuth and de-rotator axis.
* `goto`: moves the telescope to the `ra` and `de` position.
* `stop`: aborts the current movement of the telescope.
* `pumping`: moves the telescope and the de-rotator to the hard-coded position
  for pumping the Dewar.
* `reset` performs a reset of all axis errors.
* `elevation_offset`: offset for the elevation in degrees.
* `azimuth_offset`: offset for the azimuth in degrees.
* `time_offset`: offset for the time in seconds.
* `derotator_offset`: offset for the de-rotator in degrees.
* `Nasmyth_port`: desired Nasmyth port (1 or 2).
* `focus_position`: position in millimeters for the focuser.
* `filter_position`: new position of the filterwheel.

Output Variables
^^^^^^^^^^^^^^^^

* `ready`: signals that the last command has been executed and the telescope is
  ready for a new command.
* `error`: signals an (axis-)error
* `errorid`: NC axis error number
* `sliding`: the telescope is moving to a new position
* `tracking`: the telescope is in tracking mode and follows the set right
  ascension and declination position.
* `stopped`: the telescope is not moving.
* `slewtime`: time in seconds, until the telescope reaches its goto-position.
* `tracktime`: time in seconds, until the telescope will reach a limit-switch.
* `homed`: signals if all axis are calibrated.
