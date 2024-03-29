Telescope Initialisation
========================

After powering the telescope for the first time, upgrading the firmware or in
case of a power loss, the telescope initialises itself when setting the power flag
in automatic mode.

#. The main PLC boots the TwinCAT firmware.
#. If the PLC firmware is running, a blue signal is enabled on the PLC.
#. The TwinSAFE is reset within 15 seconds, if no emergency stop is pressed.
#. The power transformer is activated after one second, if the power switch on
   the main panel is in "ON" position.
#. Available power is indicated by the power lamp.
#. After TwinSAFE is ready the hydraulics system can be activated by pressing the
   "START" button.
#. If "BRAKE CLEAR" is in "ON" position on the main panel, the hydraulic brakes
   will be opened.
#. When the hydraulic brakes open, the azimuth axis and the elevation axis will
   perform a self calibration ("wake-and-shake").
#. When all axis are ready, they move to their predefined home position.
