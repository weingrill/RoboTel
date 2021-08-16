Design Issues
=============

This is a collection of design issues that might affect the operational performance
of the telescope.

* The azimuth and elevation axis are lacking an absolute encoder. In the current
  situation, the drive has to undergo a 'wake and shake' initialisation routine
  to determine to commutator offset. Since the drive is under full load, this
  routine is not suitable for this method. Absolute encoders would overcome this
  procedure by using a fixed commutator offset.
* The azimuth and elevation brakes are not separated. This requires the position
  controller to be activated on both drives as soon as the brakes are opened.
  Having individual brakes would also offload the brake control directly to the
  servo drivers featuring a brake control output.
* The emergency stop chain for the pendant control is connected to the main
  panel. Using TwinSAFE would allow for a TwinSAFE EL1904 input in the
  telescope cabinet providing the same safety level and simplifying the wiring.
* The logic voltages Up and Us are not fused and supplied separately. This would
  allow a better control in case of an emergency stop and provide better
  electrical safety.
* The covers can be operated by sink-source digital outputs EL2084 instead of
  motor units. Since the covers are lacking a positional feedback, the EL72xx
  units can't operate in a control loop anyway.
* Using a motor control unit EL72xx for the fan is superfluous, since it can't
  reverse the polarity. A regular PWM unit EL2502 would be sufficient.
* Since M3 does not have a positional feedback, a motor control unit EL72xx
  does not make sense. Either a PWM unit EL2502 or a Push-Pull EL2084 would
  be sufficient.
* The phase watcher for the main power protecting the hydraulic pumps is
  redundant. The starter relays for the pumps also check the phases. It would
  be better to monitor the mains using a EL3483 and the power consumption using
  EL3433.
