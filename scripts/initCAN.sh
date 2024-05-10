#!/bin/bash
var="E"
var=$(ls /dev|grep "ttyACM" )
echo "Init device : "${var}
sudo slcand -o -c -s8 /dev/${var} can0
sudo ifconfig can0 up
sudo ifconfig can0 txqueuelen 1000
