
Here are some examples showing how to use the atmospheric_dispersion code in IDL. This goes through many of the same exercises as shown in the pythone notebook. 

**Define location and atmospheric conditions**

    longitude   = -156.2564  ; deg,
    latitude    =  20.7067   ; deg,
    altitude    =  3067      ; m 

    temp        = 8.2 ; u.deg_C,                                                             
    pressure    = 70965 ; u.Pa,                                                           
    humidity    = 30 ; %                                                                 
    co2_conc    = 4002 ; ppm                                                              
    wavelengths = [396.9, 656.3] 

**Calculate refractivity for a individual wavelengths**

refrac = refractivity(wavelengths, temp, pressure, humidity, co2_conc, verbose=2) 

    wavelength - 396.90  nm
    n(axs):  28291.7  <>  n(ws):    318.6  <>  rho(a/axs):        0.713946  <>  rho(w/ws)::        0.255684  <>  n(prop):  20280.2
    n(air):  20198.8 <>  n(water):     81.5
    wavelength - 656.30  nm
    n(axs):  27624.2  <>  n(ws):    307.9  <>  rho(a/axs):        0.713946  <>  rho(w/ws)::        0.255684  <>  n(prop):  19800.9
    n(air):  19722.2 <>  n(water):     78.7

**Compute the atmospheric dispersion between two selected wavelengths**

    wavelengths = (findgen(46)*10 + 400)  ; u.nm
    times = julday(02,22,2021,18,00,00) 
    refraction_atm = atmospheric_refraction(wavelengths, time, $
        latitude=latitude, longitude=longitude, altitude=altitude, air_temp=temp,$)
        air_pressure=pressure, humidity=humidity, co2_conc=co2_conc, verbose=1) 
        
    plot,wavelengths,refraction_atm.refraction_mag,/yn,xtitle='Wavelength [nm]',$
        ytitle='Refraction [arcsec]',title='Total Atmosphere Refraction'
        
**Compute the atmospheric dispersion between two selected wavelengths**

    ref_wave        = 500 ; u.nm
    idx_refwave_min = min(abs(wavelengths - ref_wave), idx_refwave)
    ref_wave        = wavelengths[idx_refwave]

    dispersion_torefwave = refraction_atm.refraction_mag -  refraction_atm.refraction_mag[idx_refwave]
    plot,wavelengths,dispersion_torefwave,/yn,xtitle='Wavelength [nm]',$
        ytitle='Dispersion Magnitude [arcsec]',title='Atmospheric dispersion relative to ' + strtrim(ref_wave,2) + ' nm'
        
**Compute dispersion-induced offsets in solar NS-EW coordinates**
    times = julday(05,23,2021,17,00,00) + findgen(60*9)/(24LL*60)

    Obs_Coord        = [ longitude, latitude, altitude]
    Meteo_Conditions = [ temp, pressure, humidity, co2_conc ]
    
    offsets = atmospheric_refraction_shifts(times, wavelengths, Obs_Coord=Obs_Coord, Meteo_Conditions=Meteo_Conditions)
    
    
    
    
    
