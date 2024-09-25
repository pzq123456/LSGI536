# Lecture 3 : Remote Sensing Image Pre-processing
1. The goal of pre-processing is to
    - correct distorted (geometric) or degraded (radiometric) image data.
    - to create a more faithful representation of the original image.
    - depict the reality prior to any further enhancement, interpretation, or analysis.

2. Image pre-processing
   - Signal Noise Removal : This is mainly related to the senor and its platform and should be removed before applying other corrections.
   - Geometric Correction : Due to altitude, orientation and velocity of the platform Earth curvature and rotation.
   - Cloud Screening 
   - Radiometric Correction : 
     - Conversion from DN to radiance, related to sensor sensitivity and calibration.
     - Sun Angle correction: apply to images acquired under different solar illumination angles by normalization assuming the sun was at the zenith on each of the sensing.
   - Atmospheric Correction
     - Radiation attenuation due to scattering and absorption
     - May not be necessary for some applications such as classification for single date. But crucial for spectral 

3. What are tiers? – Real Time, Tier 1, Tier 2
   - Real Time: Raw data, no processing
   - Level 1: without atmospheric correction, Top of Atmosphere (TOA) reflectance
   - Level 2: Surface reflectance, atmospheric correction

## 2. Radiometric Pre-processing
### 2.1. Noise removal
1. Noise : It is unwanted disturbance in image data that is due to limitations in the sensing, signal digitation, or data recording process. 
   1. systematic(e.g. 
      - Line drop. Can be solved by replacing the defective DNs with the average of the values of the pixels occurring in the lines just above and below.) 
      - Bad pixels. 
        - phenomenon : “salt and pepper” or “snowy” appearance. 
        - detect: Noise can be identified by comparing each pixel in an image with its neighbours. Normally change much more abruptly than true image values. 
        - removal : The noisy pixel value can then be replaced by the average of its neighbouring values. Moving neighbourhoods or windows of 3 х 3 or 5 x 5 pixels are typically used in such procedures.
    - Stripe noise : De-striping is using low pass filter/noise removal filter.(低通滤波)
   2. random speckle. 

### 2.2. Radiometric correction
2. DN-to-Radiance conversion
   1. Depends on the scene calibration data available in the header file(s) 线性拉伸
      1. Gain & Bias Method Use Gain and Bias (or Offset) values from the header file
         1. High gain mode is used when the surface brightness is low and low gain mode is used when surface brightness is high.（similar to EV 曝光值）
    2. Spectral Radiance Scaling method Use the LMin and LMax spectral radiance scaling factors

3. Sun angle effects due to seasonal change
   > - 每一个波段的累积太阳辐射值，单位 W/m2 * μm 瓦特/平方米*微米
### 2.3. Atmospheric correction
- Atmospheric correction can be handled by
   1) Dark object subtraction/Dark pixel method （黑体法，理论上DN应该为0， 但是实际上多出来的就是path radiance Lp ）: 
       - Assumes that the darkest objects in the image should have a DN of zero and therefore, any response is accounted from path radiance (Lp) with the assumption that it affects the entire scene uniformly. 
       - This value can be subtracted from all pixels in that band.
       - 但是黑体会随着观察角度而改变
   2) Empirical methods 
   3) Radiation transfer models/methods: 
    - RTMs **simulate** the radiative transfer interactions of light scattering and absorption through the atmosphere. These models are typically used for the atmospheric correction of airborne/satellite data and allow for retrieving atmospheric composition.
    - Require parameters of atmospheric condition at the time of image acquisition such as visibility, pressure and so on, can be obtained from local meteorological station.
    - Available numerical models such as LOTRAN, MODTRAN, ATERM, ATCOR and 6S.
### 2.4. Topographic correction 地形校正
5. Topographic correction(for Mountainous areas, high buildings)

## 3. Geometric Pre-processing
- For image data, geometric correction comprises two parts: 
  - geocoding
  - resampling : Interpolation needs to transfer brightness value from an x’, y’ location in the original (distorted) to the rectified output image.
    - Nearest neighbor
    - Bilinear interpolation
    - Cubic convolution
- Two common methods:
  - image-to-map rectification, and
  - image-to-image registration
### Systematic distortions (predictable)
- Panoramic Distortion (or Tangential Scale Distortion) 大范围边缘畸变
  - The ground area imaged is proportional to the tangent of the scan angle rather than to the angle itself. Because data are sampled at regular intervals, this produces along-scan distortion
- Skew Distortion 由于地球自转而引起的畸变
### Non-systematic (random) distortions
- Variations in altitude(离传感器的距离), attitude(卫星姿态), and velocity of the sensor platform
- Variable speed of scanning mirror
- Atmospheric refraction
- Relief displacement (地形起伏引起的影像变形)

## Cloud screening
