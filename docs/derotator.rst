De-rotator
==========

The de-rotator is initialised in automatic mode on power-up. Lacking an absolute
encoder, the calibration is performed at the limit switch.

The parallactic angle p is calculated by:

p = asin(sin a * cos ƛ / cos δ),

where a is the azimuth of the target, ƛ is the latitude of the observer and δ is
the declination of the star. The position ɸ of the de-rotator is calculated by

ɸ = p + a + e,

where e is the elevation of the target.
