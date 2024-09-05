# Lecture 1 Introduction to Remote Sensing
## 1. Introduction to Remote Sensing
1. What is “Remote Sensing”? (3 points)
    - sensor (a device)
    - obtaining information, extracting environmental information
    - not in contact with the object, not in physical contact

2. System Types
   - Passive systems record reflected, naturally occurring radiation (e.g., natural light, infrared radiation)
   - Active systems record the reflection of emitted radiation (e.g., radar, sonar)

3. Why “Remote Sensing”?
   - global coverage, Cost effective
   - historical data and provide long-term change
   - detect light that beyond human vision

## 2. Physical Principles of Imaging
1. Visible Light, 400 to 700nm, is the only region that human are sensitive to.
    - longer wavelength is seen as Red (~650nm)
    - middle wavelength is seen as Green (~550nm)
    - shorter wavelength is seen as Blue (~450nm)
    - visible light is used extensively in remote sensing

2. 红外 Infrared, 700 nm to 1 mm, can be sub-divided into
    - Near IR (700 to 1300 nm)
    - Shortwave IR (1.1 to 3 μm)
    - Mid IR (3 to 5 μm)
    - Longwave or Thermal IR (8 to 15 μm)
    - IR is extensively used in remote sensing for plant health monitoring

3. 微波 Microwaves(pass through clouds, can work in cloudy or rainy days), 1mm to 1m, can penetrate through cloud cover and most weather conditions
    - good for communication
    - can be used for detecting precipitation, monitoring and mapping natural resources
    - microwaves can be used in both passive and active sensors

4. Radio Waves, 1m to 1km, have the longest wavelength and are used for data transmission. 
5. Why Landset different bands have differnrnt special resulation? e.g. Landsat Band 1 (blue) and Band 6 (thermal)
   - longer wave length -> lower energy -> reduced spacial reoultion (have more noise and less useful informtion) 
6. Atmospheric windows
   - The places where energy passes through are called “atmospheric windows”.
   - The places with limited or almost no absorption by the atmosphere is known as the atmospheric window.
   - The wavelength ranges in which the atmosphere is particularly transmissive of energy are referred as Atmospheric Windows.

7. Energy interactions in the atmosphere 
- The net effect of the atmosphere varies with:
    - Difference in path length 
    - Magnitude of the energy signal 
    - Atmospheric condition (pollution, air quality)
    - Wavelengths involved 
- Two types of interactions are normally observed:
    - Scattering : 
    - Absorption : energy absorpted by something, the enrgy is disappeared.

8. Atmospheric scattering : Scattering occurs when particles or large gas molecules present in the atmosphere interact with and cause electromagnetic radiation to be redirected from its original path.1
- Three types of scattering
  - Rayleigh or molecular scattering : occurs when particles are smaller than its the wavelength of the radiation, shorter wavelengths scattered more than longer wavelengths. 
- Mie or non-molecular scattering : 
  - occurs when particles are about same size as the wavelength of the radiation.
- Non-selective scattering (100% scattering): 
  - occurs when the particles (water or dust) are much larger than the wavelength of the radiation.
- The sunlight is scattered in all directions by the gases in the air when it reaches the Earth’s atmosphere. The types of gases mostly scatter the shorter and choppier waves of blue lights.

9. Atmospheric absorption Absorption is the other main type of interaction that electromagnetic radiation interacts with the atmosphere.
    - Ozone: absorb the harmful ultraviolet radiation from the sun. Without Ozone layer our skin would get burnt when exposed to sunlight.
    - Carbon dioxide (CO2): absorbs strongly in the far infrared region
        – the area associated with thermal heating – thus heat is trapped inside the atmosphere.
    - Water vapor: absorbs much of the infrared and microwave radiation (between 22μm and 1m).

## 3. Digital Image Processing and Analysis
1. Atmospheric correlation : Atmosphere-top reflection, surface reflection