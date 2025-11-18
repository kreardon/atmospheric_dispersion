from astropy import units as u
from astropy.coordinates import EarthLocation, AltAz, TETE
from astropy.time import Time
import numpy as np

import atm_dispersion as adm # Atmospheric Dispersion Module

atm_conditions = {
    'temp':     20*u.deg_C,
    'pressure': 71000.*u.Pa,
    'humidity': 40,
    'co2_conc': 400}


longitude =    -156.25*u.deg
latitude  =     20.71*u.deg
altitude  =     2800.*u.m
observing_loc = EarthLocation(lat=latitude, lon=longitude, height=altitude)

def refractivity_calc(wavelength):

    refrac = adm.refractivity(wavelength,
                atm_conditions['temp'],
                atm_conditions['pressure'],
                atm_conditions['humidity'],
                atm_conditions['co2_conc'],
                verbose=0)
    
    print(refrac)
    
    return refrac

def refraction_calc(wavelengths):
    time = Time('2021-05-23 17:00:00',scale='utc') + np.zeros((1))
    time.format = 'jd'

    refraction_atm = adm.atmospheric_refraction(wavelengths,    
                                            time,
                                            air_pressure = atm_conditions['pressure'],
                                            air_temp     = atm_conditions['temp'], 
                                            humidity     = atm_conditions['humidity'],
                                            co2_conc     = atm_conditions['co2_conc'],
                                            observer_location = observing_loc,
                                            verbose      = 0)
    return refraction_atm    

def test_refractivity_calc():
    """Check the calculation of the refractivity of air at a given wavelength."""
    import math

    wavelength = 500 * u.nm

    refractivity_calculated = refractivity_calc(wavelength)
    refractivity_expected   = 0.000200
    print(refractivity_calculated)

    assert math.isclose(refractivity_calculated, refractivity_expected, rel_tol=1e-1)

def test_refraction_calc():
    """Check the calculation of the total refraction at a given time, location, wavelength."""
    import math

    wavelengths = [500, 600] * u.nm
    refraction_minimum    = [140, 139]

    atmospheric_refraction, input_times = refraction_calc(wavelengths)
    atmospheric_refraction_mag = atmospheric_refraction['refraction_mag (arcsec)'][0]
    print(atmospheric_refraction_mag[0])

    assert atmospheric_refraction_mag[0]>  refraction_minimum[0]
    assert atmospheric_refraction_mag[1]>  refraction_minimum[1]
    assert atmospheric_refraction_mag[1] < atmospheric_refraction_mag[0]
    assert (atmospheric_refraction_mag[0] - atmospheric_refraction_mag[1]) >= 0.5
    assert (atmospheric_refraction_mag[0] - atmospheric_refraction_mag[1]) <  5.0
