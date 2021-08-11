Telescope Covers
================

The covers are opened in automatic mode prior to enabling the elevation drive to
ensure a balanced load in the calibration phase. After wake and shake the position
control es enabled and can compensate for the torque, if the covers are still
closed.

In automatic operation the covers are opened by setting the ``open`` flag in
CoverControl. Setting the ``close`` flag overrides the open flag and closes the
cover.
Since cover 3 is blocking cover 2 for the opening procedure, opening of cover 2
is delayed as well as closing of cover 3.

If the limit switches are in an unlogical state, an error is rised. If the covers
take to long to open or to close, a timeout error is raised.

Since the drives are lacking any positional feedback, the motors for the covers
could also be driven by source-sink Beckhoff modules (EL2084).
