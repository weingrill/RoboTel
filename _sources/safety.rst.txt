Safety Instructions
===================

RoboTel is designed to mainly operate in robotic or autonomous mode.
This implies that only the minimum required set of safety precautions have been
installed on this system.

The telescope can start at any time when automatic operation is enabled.

To stop the motion of the telescope or the operation of the hydraulics system
press the emergency button either on the main panel or on the manual controls.

Pressing the emergency button deactivates the high power modules within the
servo drivers. This stops any motion of the azimuth, elevation and de-rotator
axis immediately. As a consequence the TwinSAFE logic module and the AX5000
servo drivers go into an error condition.

Error Acknowledgement
---------------------
To reset an error condition the TwinSAFE has to be restarted:
1. Turn the power switch on the main panel to "OFF".
2. Press the RESET button on the main panel.

The error signal should disappear. If not, please check, if all emergency buttons
are pulled out for normal operation.

*Be aware that disconnecting the pendant control also triggers an emergency stop!*

Maintenance
-----------

Press the emergency button when performing maintenance on the telescope. If e.g.
operating the telescope cover is required, put the telescope in manual operation
mode, see :doc:`manual`
