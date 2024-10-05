# Part1

> LSGI536-Lab1-24037665g-PanZhiQing

## Introduction for Part1

You need to download a satellite image, then present it using ERDAS IMAGINE software. The image attribute, spectral profile, surface profile, and spatial profile are required to be shown in the report. 

## Spectral profile
Click Multispectral, Panchromatic, Relief, or Thematic tab > locate Utilities group > Spectral Profile. I chose some vegatation area to check the spectral of the image. The spectral profile of the image is shown in Figure 1, and we can find that there is a peak at band 5.

![](./imgs/p1.png)
Figure 1: Spectral profile of the image
<div STYLE="page-break-after: always;"></div>

## Surface profile
Click Multispectral, Panchromatic, Relief, or Thematic tab > locate Utilities group > Surface Profile. I chose a rectangle area of the human-made building to check the surface profile of the image. 

![](./imgs/p2.png)
Figure 2: Surface profile of the image
## Spatial profile
Click Multispectral, Panchromatic, Relief, or Thematic tab > Utilities group > click Profile. I have chosen a diagonal line to check the spatial profile of the image. We can see that the right-bottom corner of the image is the darkest area, and in the spacial profile, the pixel value is the lowest.

![](./imgs/p3.png)
Figure 3: Spatial profile of the image
<div STYLE="page-break-after: always;"></div>

## Image attribute
<!-- ![](./imgs/p4.png) -->
<!-- 保留愿比例 缩减到80% -->
<img src="./imgs/p4.png" width="60%" height="60%">

Figure 4: Image attribute of the image
## Reference
1. [data set](https://earthexplorer.usgs.gov/scene/metadata/full/5e83d14f2fc39685/LC81220442024220LGN00/)



<div STYLE="page-break-after: always;"></div>


# Part 2

## Introduction for Part2
You need to register the image with map and image with image, respectively, using the dataset in the ‘data’ folder. Then export two maps of the registered images with ArcGIS software (overlay the registered image and reference road map, registered image and reference image separately).

## Image to map registration

![](./imgs/p6.jpg)
<div STYLE="page-break-after: always;"></div>

## Image to image registration

Select “Multispectral → Transform & Orthocorrect → Control points” to open the registration panel. I setted the reference layer as the SPOT image, and the Landsat TM image as the image layer. Then, I selected 10 points in both images as the control points. For the points, the peak, crossroad, and the edge of the lake are selected. 

![](./imgs/p7.png)