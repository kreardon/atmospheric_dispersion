# Atmospheric Dispersion Module for Solar Observations

This repository contains code for calculating the atmospheric refraction at different (visibile and infrared) wavelengths, and from the differences among wavelengths, the magnitude and direction of the dispersion. 
It is designed specifically for solar observations, with methods to calculate the dispersion for the Sun, given only an observer location and time. There is an additional method to decompose the dispersion into shifts in the two axes of the helioprojective coordinate system.

The IDL code was originally developed for the publication:<BR>
Reardon, K.P., 2006, "The Effects of Atmospheric Dispersion on High-Resolution Solar Spectroscopy", _Solar Physics_, *239*, pp. 503-517.<BR>
https://ui.adsabs.harvard.edu/abs/2006SoPh..239..503R/abstract
<BR>
Please cite this work when using this code.

The Python code is derived from the IDL code, thanks to work by Katie Lee and Ryan Hofmann. One significant change in the Python version is the means of calculating the solar position/ephemeris using SunPy.

KPR - 23 March, 2025
