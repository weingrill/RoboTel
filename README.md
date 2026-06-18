# RoboTel TwinCAT firmware repository

[![Build Status](https://travis-ci.com/weingrill/RoboTel.svg?branch=master)](https://travis-ci.com/weingrill/RoboTel)

This is the telescope firmware for Halfmann telescopes upgraded with Beckhoff hardware.
Electronic schematics are available upon request.

The online manual can be found here:

https://weingrill.github.io/RoboTel/index.html

This repository contains a TwinCAT3 project for controlling a telescope system with the following components:

- **Safety System**: TwinSafe implementation for safety-critical functions with safety-related POU files and GVLs
- **Runtime Control**: Main control logic with various control functions for telescope subsystems:
  - Azimuth/Elevation control
  - Dome control
  - Filter wheel control
  - Focus control
  - Hydraulics control
  - Auxiliary systems
  - Derotator control
  - Environment monitoring
- **Function Blocks**: Various control algorithms and utility functions
- **Data Types**: Defined data structures for system communication
- **Visualization**: HMI visualization components

This project is described in the SPIE paper "New electronic brains for Halfmann telescopes" by Jörg Weingrill, Thomas Granzer, Michael Weber, Wilbert Bittner, Carlo Seehaus, and Jan Mettke, published in Software and Cyberinfrastructure for Astronomy VII, Proc. of SPIE Vol. 12189, 121890F (2022). DOI: 10.1117/12.2629327

For more information about this project, please refer to the paper which describes:
- The upgrade of Halfmann telescopes from obsolete electronics to modern Beckhoff TwinCAT3 control system
- The replacement of the Linux computer with a Beckhoff PLC CX5140 as the new "electronic brain"
- The use of MQTT for commanding the telescope and reporting sensor values and position information
- The logging of sensor measurements and telescope state in an Influx database with visualization using Grafana
- The implementation of safety measures including TwinSAFE components
- The modular design with line replaceable units (LRUs) following ESO standards
- The use of EtherCAT bus system for interconnection
- The control of various telescope subsystems including azimuth, elevation, dome, covers, hydraulics, derotator, filter wheel, focus, and environment monitoring

# ToDo
* verification of moonpos algorithm
* testing of machine vision algorithm

# Licensing
see LICENSE.txt

Ⓒ 2019–2026 Dr.Jörg Weingrill, Leibniz-Institut für Astrophysik Potsdam
