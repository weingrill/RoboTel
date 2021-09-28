#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Joerg Weingrill"
__copyright__ = "Copyright 2021 Leibniz-Institute for Astrophysics Potsdam (AIP)"
__credits__ = ["Joerg Weingrill"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Joerg Weingrill"
__email__ = "jweingrill@aip.de"
__status__ = "Development"
__date__ = "2021-09-27"

import argparse
import paho.mqtt.client as mqtt


def send_command(command: str) -> None:
    client = mqtt.Client()
    client.connect("primitivo.aip.de", 1883, 60)

    client.publish("RoboTel/Telescope/SET", command)
    client.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='RoboTel Commandline Interface')
    parser.add_argument('--power', type=bool, help='set telescope power state')
    parser.add_argument('--home', action='store_true', help='home the telescope at predefined homing coordinates')
    parser.add_argument('--track', action='store_true', help='start telescope tracking')
    parser.add_argument('--stop', action='store_true', help='stop the telescope')
    parser.add_argument('--park', action='store_true', help='park the telescope')
    parser.add_argument('--ra', type=float, help='set the right ascension of the telescope')
    parser.add_argument('--de', type=float, help='set the declination of the telescope')
    parser.add_argument('--focus', type=float, help='set the focus position')
    parser.add_argument('--filter', type=float, help='set the filter wheel position')
    parser.add_argument('--derot', type=float, help='set the de-rotator offset of the telescope')
    parser.add_argument('--nasmyth', type=int, choices=[1, 2], help='set the Nasmyth port of the telescope')

    args = parser.parse_args()

    if args.power:
        send_command('command power=TRUE')
    if args.home:
        send_command('command home=TRUE')
    if args.track:
        send_command('command track=TRUE')
    if args.stop:
        send_command('command stop=TRUE')
    if args.park:
        send_command('command park=TRUE')
