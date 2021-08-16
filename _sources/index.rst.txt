.. RoboTel documentation master file, created by
   sphinx-quickstart on Thu Jan 21 16:06:06 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RoboTel Firmware documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   safety
   init
   manual
   hydraulics
   filterwheel
   dome
   covers
   derotator

Introduction
------------
RoboTel was build by Halfmann and upgraded by AIP in 2020/2021. All important
electronic components have been replaced by Beckhoff modules.
A central Beckhoff PLC controls the servo controllers, DC controllers,
temperature sensors and digital I/Os.

Please read the :doc:`safety` before operating the telescope.

Design issues
-------------
The RoboTel telescope has some design flaws originating from the original design
by Halfmann. See :doc:`issues` for a detailed analysis and potential upgrades of
the system.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
