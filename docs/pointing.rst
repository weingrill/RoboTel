Pointing Model
==============

To compensate for alignment errors, a pointing model has been implemented in
the firmware.::

  Δaz = c_an∙sin(az)∙tan(h) - c_ae∙cos(az)∙tan(h) - c_npae∙tan(h) + c_ca/cos(h) + c_aoff
  Δh = c_an∙cos(az) - c_ae∙sin(az) + c_flex∙cos(h) + c_hoff

where `az` ist the azimuth and `h` is the elevation.

Source:
<http://stella-archive.aip.de/javadoc/scs/stella/util/PointingModel.html>
