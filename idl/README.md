
<<<<<<< HEAD
The IDL version of the Solar Atmospheric Dispersion Module also requires the installation of the IDL Astronomy User's Library, available here:

https://idlastro.gsfc.nasa.gov

Here are some examples showing how to use the atmospheric_dispersion code in IDL. This goes through many of the same exercises as shown in the jupyter notebook for the Python version. 

## Define location and atmospheric conditions

Two key components of the following calculations are the location of the observer and the atmospheric conditions.
The observer location allows the determination of the elevation of the Sun at any given time.
The atmospheric conditions allow the atmospheric profile to be estimated, and hence the determination of the refractivity of the air.
=======
The IDL version of the Solar Atmospheric Dispersion Module also requires the installation of the IDL Astronomy User's Library, originally available here: <BR>
https://asd.gsfc.nasa.gov/archive/idlastro/
<BR> but now with a github repository: <BR>
https://github.com/wlandsman/IDLAstro

Here are some examples showing how to use the atmospheric_dispersion code in IDL. This goes through many of the same exercises as shown in the jupyter notebook for the Python version. 
>>>>>>> db4f99b (updating README files, adding github repository for IDL Astronomy Library)

## Define location and atmospheric conditions

Two key components of the following calculations are the location of the observer and the atmospheric conditions.
The observer location allows the determination of the elevation of the Sun at any given time.
The atmospheric conditions allow the atmospheric profile to be estimated, and hence the determination of the refractivity of the air.
    
    ; these are the coordinates and conditions for DKIST on Haleakala
    longitude   = -156.2564  ; deg,
    latitude    =  20.7067   ; deg,
    altitude    =  3067      ; m 

    temp        = 8.2 ; u.deg_C,                                                             
    pressure    = 70965 ; u.Pa,                                                           
    humidity    = 30 ; %                                                                 
    co2_conc    = 400 ; ppm                                                              
    wavelengths = [396.9, 656.3] 

## Calculate refractivity for a individual wavelengths

The basis of the dispersion calculation is computing the atmospheric refractivity at various wavelengths. The refractivity depends on the atmospheric height profile, but can be approximated if the temperature, pressure, humidity, and CO2 fraction is known.

    refrac = refractivity(wavelengths, temp, pressure, humidity, co2_conc, verbose=2) 

    wavelength - 396.90  nm
    n(axs):  28291.7  <>  n(ws):    318.6  <>  rho(a/axs):        0.713946  <>  rho(w/ws)::        0.255684  <>  n(prop):  20280.2
    n(air):  20198.8 <>  n(water):     81.5
    wavelength - 656.30  nm
    n(axs):  27624.2  <>  n(ws):    307.9  <>  rho(a/axs):        0.713946  <>  rho(w/ws)::        0.255684  <>  n(prop):  19800.9
    n(air):  19722.2 <>  n(water):     78.7

<<<<<<< HEAD
**Compute atmospheric refraction for a range of wavelengths at a single time
=======
## Compute atmospheric refraction for a range of wavelengths at a single time
>>>>>>> db4f99b (updating README files, adding github repository for IDL Astronomy Library)

Here we compute the total refraction at a single time as a function of wavelength. This is the amount of upward deflection of the object with respect to its true position.

    wavelengths = (findgen(46)*10 + 400)  ; u.nm
    times = julday(02,22,2021,18,00,00) 
    refraction_atm = atmospheric_refraction(wavelengths, time, $
        latitude=latitude, longitude=longitude, altitude=altitude, air_temp=temp,$)
        air_pressure=pressure, humidity=humidity, co2_conc=co2_conc, verbose=1) 
        
    plot,wavelengths,refraction_atm.refraction_mag,/yn,xtitle='Wavelength [nm]',$
        ytitle='Refraction [arcsec]',title='Total Atmosphere Refraction'
        
## Compute the atmospheric dispersion between two selected wavelengths

Here we compute the difference in the magnitude of refraction between two wavelength.

    ref_wave        = 500 ; u.nm
    idx_refwave_min = min(abs(wavelengths - ref_wave), idx_refwave)
    ref_wave        = wavelengths[idx_refwave]

    dispersion_torefwave = refraction_atm.refraction_mag -  refraction_atm.refraction_mag[idx_refwave]
    plot,wavelengths,dispersion_torefwave,/yn,xtitle='Wavelength [nm]',$
        ytitle='Dispersion Magnitude [arcsec]',title='Atmospheric dispersion relative to ' + strtrim(ref_wave,2) + ' nm'
        
## Compute dispersion-induced offsets in solar NS-EW coordinates

The dispersion calculated above is the magnitude of the offset between two wavelengths along the direction perpendicular to the horizon.
But observations are often obtained (or corrected to, as part of the data reduction process) with the image plane held in a constant orientation with respect to the solar disk.
So what is more useful from the observers' perspective, is the magnitude of the dispersion offsets in the N-S and E-W direction of the solar helioprojective coordinate system.


    times = julday(05,23,2021,17,00,00) + findgen(60*9)/(24LL*60)

    Obs_Coord        = [ longitude, latitude, altitude]
    Meteo_Conditions = [ temp, pressure, humidity, co2_conc ]
    
    offsets = atmospheric_refraction_shifts(times, wavelengths, Obs_Coord=Obs_Coord, Meteo_Conditions=Meteo_Conditions)
    
## Compute dispersion and parallactic angle for a full year

One useful capability, especially for planning purposes, is the possibility of calculating the atmospheric dispersion for a extended time periods. In this case, we will compute the dispersion for all times over the course of a year.

We return the elevation and aximuth information so we can create a mask of times when the Sun is suitably above the horizon.

    times_1year = julday(01,01,2022,0,00,00) + findgen(24*60,365)/(24LL*60)
    wavelengths = [396.8, 854.2] ; u.nm

    refraction_atm = atmospheric_refraction(wavelengths, times_1year, $
        latitude=latitude, longitude=longitude, altitude=altitude, air_temp=temp,$)
        air_pressure=pressure, humidity=humidity, co2_conc=co2_conc, alt_sun=alt_all,az_sun=az_all, verbose=1) 
        
    dispersion    = refraction_atm.refraction_mag[*,0] - refraction_atm.refraction_mag[*,1]
    dispersion    = reform(dispersion,1440,365)
    altitude_mask = alt_all GE 5
    ; shift by 626 minutes (10.4 hours) to put local noon at the center of the display
    tvscl,shift(dispersion * altitude_mask,626,0)   
    
    ; or display parallactic angle (which is wavelength independent)
    tvscl,SHIFT(refraction_atm.parallactic_angle * altitude_mask,626,0)

