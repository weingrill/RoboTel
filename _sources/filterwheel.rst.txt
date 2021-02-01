Filter-Wheel
============

The filter wheel can be either controlled manually on the pendant control or
by using the API.

API Description
---------------

* The axis is enabled automatically as soon as `TelescopeControl.power` is TRUE.
* If the axis is not calibrated, the filter wheel moves to the calibration
  position first.
* `Reset` resets the axis
* The desired optical filter is selected by setting the `filter_position` to
  a value between 0 and 23. If the actual filter differs from the set position,
  the filter wheel starts repositioning itself.
* `Ready` indicates, if the desired filter has been selected.

System parameters
-----------------

| reference velocity (110%) = 114.216667 deg/s
| maximum velocity (100%) = 103.833333 deg/s
| maximum acceleration = 15000.0 deg/s^2
| maximum deceleration = 15000.0 deg/s^2
| default acceleration = 155.75 deg/s^2
| default deceleration = 155.75 deg/s^2
| jerk = 467.25 deg/s^3

| homing speed = 1.0383 deg/s
| jog max = 31.15  deg/s
| jog min = 5.1916667 deg/s
| jog pulse = 5.0 deg/s

| Nc feed constant = 5 deg/motor rotation
| Scale factor numerator = 5 deg/Inc
| Manual Velocity (Fast) = 31.15 deg/s
| Manual Velocity (Slow) = 5.1916667 deg/s
