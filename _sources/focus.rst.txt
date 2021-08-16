Focus
=====

The focus can be either controlled manually on the pendant control or
by using the API.

API Description
---------------

* The axis is enabled automatically as soon as `TelescopeControl.power` is TRUE.
* If the axis is not calibrated, the filter wheel moves to the calibration
  position first. This is the far end of the M2.
* `Reset` resets the axis or an error condition.
* The desired focus position is selected by setting the `focus_position` to
  a value between 0 and 97.6. If the actual focus position differs from the set
  position, the focus moves to the new position and stops if the `focus_precision`
  is reached.
* `Ready` indicates, if the desired focus position has been reached and the focus
  is locked.
* `inward` moves the M2 closer to M1.
* `outward` moves the M2 away from M1.
* `position` new position for the focus axis.
* `HomeAxis` perform calibration of the axis.
* `MoveAxis` move the axis to the new position.
* `Calibrated` indicates, if the axis has been calibrated successfully.

System parameters
-----------------

| reference velocity (110%) = mm/s
| maximum velocity (100%) = mm/s
| maximum acceleration = mm/s^2
| maximum deceleration = mm/s^2
| default acceleration = mm/s^2
| default deceleration = mm/s^2
| jerk = mm/s^3

| homing speed = mm/s
| jog max = mm/s
| jog min = mm/s
| jog pulse = mm/s

| Nc feed constant = mm/motor rotation
| Scale factor numerator = mm/Inc
| Manual Velocity (Fast) = mm/s
| Manual Velocity (Slow) = mm/s
