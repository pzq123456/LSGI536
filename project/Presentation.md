# Group Project Presentation(lecture En-Zh)
> Notice of Preliminary  :
> - A 3-minute brief introduction to the project topic, literature investigation, and implementation plan, presented with ~5 slides.
> - Time: Oct 23, 2024
> - Send slides to LIU Xindi, Cindy at xindi1025.liu@connect.polyu.hk before 2:00PM on Oct 23, 2024
## Remote sensing-based evolutionary analysis of park vegetation - A case study of Shenzhen City
- [Group Project Presentation(lecture En-Zh)](#group-project-presentationlecture-en-zh)
  - [Remote sensing-based evolutionary analysis of park vegetation - A case study of Shenzhen City](#remote-sensing-based-evolutionary-analysis-of-park-vegetation---a-case-study-of-shenzhen-city)
    - [1. 研究意义背景 | Research Significance \& Background （1页 Feng）](#1-研究意义背景--research-significance--background-1页-feng)
      - [Background](#background)
      - [Significance](#significance)
    - [2. 文献综述 | Literature Review （2页 Liang）](#2-文献综述--literature-review-2页-liang)
      - [1. Page 1](#1-page-1)
      - [2. Page 2](#2-page-2)
    - [3. 数据 \& 研究范围 | Data \& Study Areab （1页）（Zeng \& Zhou）](#3-数据--研究范围--data--study-areab-1页zeng--zhou)
    - [4. 研究方法 \& 研究计划 | Research Method \& Plan （1页）（Dong）](#4-研究方法--研究计划--research-method--plan-1页dong)
    - [Report （Li）](#report-li)
    - [Docs \& PPT（Yao \& Pan）](#docs--pptyao--pan)
  - [References](#references)

### 1. 研究意义背景 | Research Significance & Background （1页 Feng）

#### Background
- 近年来，深圳市城市化进程迅速发展，土地利用/覆盖发生了显著变化。城市绿地对城市生物多样性和城市热岛具有重要影响。
- In recent years, the rapid development of urbanization in Shenzhen has led to significant changes in land use/land cover. Urban green space has important effects on urban biodiversity and urban heat island.

#### Significance
- 通过对深圳市公园植被演变的分析，有助于为城市植被规划、环境管理提供信息，加强城市生态健康。
- Through the analysis of vegetation evolution in Shenzhen park, it is helpful to provide information for urban vegetation planning, environmental management and strengthening ecological health of the city.

### 2. 文献综述 | Literature Review （2页 Liang）

#### 1. Page 1
- 通过遥感进行植被分析，遥感提供了多时相和高分辨率的数据，使我们能够监测植被动态。Pettorelli等人（2014）的研究指出，遥感在生态研究中具有巨大潜力，但也面临着解释数据的挑战。
- In vegetation analysis by remote sensing, remote sensing provides multi-temporal and high-resolution data that allow us to monitor vegetation dynamics.The study by Pettorelli et al. (2014) points out that remote sensing has a great potential for application in ecological research, but also faces challenges in interpreting the data.

- 下一步是城市公园植被变化的问题。周等人（2011）研究了上海的情况，展示了随着城市化进程的推进，城市绿地空间如何变化。我们可以借鉴这些研究，结合遥感技术分析城市公园植被演变。
- Next up is the question of vegetation change in urban parks. zhou et al. (2011) studied the situation in Shanghai, showing how urban green spaces change as urbanization progresses. We can learn from these studies and combine remote sensing techniques to analyze vegetation evolution in urban parks.
- Landsat卫星数据和NDVI指数在植被健康监测中被广泛使用。Tucker（1979）提出的NDVI方法已成为评估植被健康的常用工具。
- Landsat satellite data and the NDVI index are widely used in vegetation health monitoring. the NDVI method proposed by Tucker (1979) has become a common tool for assessing vegetation health.
- 接下来，我们将看到一个具体案例研究，吴等人（2014）分析了城市化对深圳绿地的影响。他们使用遥感技术展示了深圳公园植被的变化。
- Next, we will see a specific case study where Wu et al. (2014) analyzed the impact of urbanization on green space in Shenzhen. They used remote sensing to show the changes in vegetation in Shenzhen parks.
- 然而，尽管有大量关于城市绿地和遥感的研究，仍然缺乏针对快速城市化地区如深圳的不同类型公园的详细分类研究。Seto等人（2012）指出，全球城市扩张对生物多样性和碳汇的直接影响需要更多研究。
- However, despite the large number of studies on urban green spaces and remote sensing, there are still fewer studies that address the detailed classification of different types of parks under rapid urbanization.Seto et al. (2012) point out that the direct impacts of global urban expansion on biodiversity and carbon sinks need more research.
- 综上所述，我们可以得出结论，遥感数据，尤其是Landsat和NDVI，在城市公园植被监测中具有重要意义，尤其是在像深圳这样快速城市化的地区。基于这些方法，本研究将进一步分析公园植被的演变，并对不同类型的公园进行分类。
- From these literature reviews, we can conclude that remotely sensed data, especially Landsat and NDVI, are significant in monitoring vegetation in urban parks, especially in rapidly urbanizing areas like Shenzhen. Based on these methods, this study will further analyze the evolution of park vegetation and classify different types of parks. 
#### 2. Page 2
- 在这张地图中，我们可以看到2020年深圳的NDVI图像。这幅地图是从Landsat数据生成的，显示了不同区域植被的健康状况。
- In this map, we can see the NDVI image of Shenzhen in 2020. This map was generated from Landsat data and shows the health of vegetation in different areas.
- 在地图中，绿色区域表示植被更加茂盛的区域，而黄色区域表示植被较少或健康状况较差的区域。NDVI指数是通过计算近红外和红光波段之间的差异得出的，这种方法在反映植被生长方面非常有效。
- In the map, the green areas indicate areas with more lush vegetation, while the yellow areas show areas with less vegetation or in poorer health.The NDVI index is derived by calculating the difference between the near-infrared and red light bands, a method that is very effective in reflecting the growth of vegetation.
- 通过分析这些NDVI数据，我们可以更准确地评估深圳不同公园的植被健康状况，并进一步研究城市化对这些公园的影响。下一步研究将基于这些数据对不同类型的公园进行分类，并探讨它们与周围城市化的关系。
- By analyzing these NDVI data, we can more accurately assess the vegetation health of different parks in Shenzhen and further study the impact of urbanization on these parks. The next study will be based on these data to classify different types of parks and explore their relationship with surrounding urbanization.”

### 3. 数据 & 研究范围 | Data & Study Areab （1页）（Zeng & Zhou）

- 深圳市地处广东省中南部，位于北回归线以南，毗邻香港。在城市发展进程中，提出“千园之城”“公园城市”等多个战略目标，并于2021年底公园数量达到1238个。
- Shenzhen is located in the central and southern part of Guangdong Province. It is located south of the north and is adjacent to Hong Kong. In the process of urban development, it  proposes a number of strategic goals such as "the city of thousands of gardens" and "park city". The number of parks has reached 1,238 at the end of 2021.


- 研究采用多源遥感数据，包括2015和2020年土地覆盖数据、Landsat8影像数据，及深圳市公园矢量面数据等。
- Research uses multi-source data, including land coverage data in 2015 and 2020, Landsat8 remote sensing data, and Shenzhen Park vector data.

Table 1. Details of research data.

| DataName | Spatial Resolution | Data Source |
| --- | --- | --- |
| Land cover | 30m×30m | Global 30-m land-cover dynamic monitoring product from 1985 to 2022 (Zhang et al., 2021.) |
| Remote sensing imagery data-Landsat 8 | 30m×30m | USGC (https://www.usgs.gov/) |
| NDVI (extracted from remote sensing images) | 30m×30m | Calculated from Landsat8 images |
| Shenzhen park data | .Shp | Extracted from Open Street Map (https://www.openstreetmap.org/) |
| Administrative boundary data | .Shp | National platform for common geospatial information services (https://www.tianditu.gov.cn/) |

### 4. 研究方法 & 研究计划 | Research Method & Plan （1页）（Dong）
- 通过文献综述做出研究假设:不同面积大小的公园和不同类型的公园(如自然公园和城市公园)在植被绿度变化和物候模式上会有所不同。

- Based on the literature review, we propose the following research hypotheses: Parks of different sizes and types (e.g., natural parks and urban parks) will exhibit different changes in vegetation greenness and phenology.

- 本研究希望通过将公园按照建筑和人口密度以及面积进行分类,并提取关键的植被指标，来研究和比较不同类型和大小的公园在不同时间点的生态特性。便于监测和评估公园植被的健康状况及其随时间的变化,对城市绿地管理和规划具有重要意义。

- This study aims to classify parks based on building and population density as well as area, and extract key vegetation indicators to study and compare the ecological characteristics of parks of different types and sizes at different time points. This will help monitor and evaluate the health of park vegetation and its changes over time, which is of great significance for urban green space management and planning.

- 用两种方法对公园进行分类:
   1. 通过空间分析和基于阈值的分类方法，根据周围建筑和人口密度的数据，将公园划分为自然公园和城市公园。
   2. 使用自然断点法对公园面积进行分类，将公园划分为大型、中型和小型。

- Use two methods to classify parks:
   1. Through spatial analysis and threshold-based classification methods, parks are divided into natural parks and urban parks based on data on surrounding building and population density.
   2. Use the natural breakpoint method to classify park areas into large, medium, and small.

- 公园植被指标提取:
  1. 面积指标: 植被占比、常绿植被占比和落叶植被占比。植被占比反映了植被在公园总面积中的分布情况，是衡量生物多样性和生态系统服务的基础。常绿植被占比和落叶植被占比有助于了解公园植被的组成，分析不同类型植被对季节变化和气候因素的响应。例如，常绿植被可能在冬季提供更多的生态服务，而落叶植被在春季和秋季的表现可能更为突出。
  2. 绿度指标: 包括 NDVI峰值、年平均 NDVI 和季节平均 NDVI。NDVI 峰值提供了年内公园植被绿度的最高表现，反映了植被生长的最佳状态。年平均 NDVI反映了整个年度的平均植被状况，而季节平均NDVI揭示季节性变化，有助于理解植被在不同季节的表现及其对季节性气候变化的响应。
  3. 物候指标: 生长季节开始和结束。反映了气候变化对植被生长周期的影响。开始时间可以指示春季的到来，而结束时间则标志着生长季的结束。

- Extraction of park vegetation indicators:
  1. Area indicators: Vegetation coverage, evergreen vegetation coverage, and deciduous vegetation coverage. Vegetation coverage reflects the distribution of vegetation in the total area of the park and is the basis for measuring biodiversity and ecosystem services. Evergreen vegetation coverage and deciduous vegetation coverage help to understand the composition of park vegetation and analyze the response of different types of vegetation to seasonal changes and climate factors. For example, evergreen vegetation may provide more ecosystem services in winter, while deciduous vegetation may perform better in spring and autumn.
  2. Greenness indicators: Including NDVI peak, annual average NDVI, and seasonal average NDVI. The NDVI peak provides the highest performance of park vegetation greenness during the year, reflecting the optimal state of vegetation growth. The annual average NDVI reflects the average vegetation condition throughout the year, while the seasonal average NDVI reveals seasonal changes, helping to understand the performance of vegetation in different seasons and its response to seasonal climate changes.
  3. Phenological indicators: Start and end of the growing season. Reflects the impact of climate change on the vegetation growth cycle. The start time can indicate the arrival of spring, while the end time marks the end of the growing season.

- 时间分析: 
  - 对同一类别的公园在 2015 年和 2020年两个时间点的8个生态指标进行对比分析,使用独立样本T检验来判断两个时间点的数据是否存在统计学上的显著差异。

- Temporal analysis:
  - Compare and analyze 8 ecological indicators of parks of the same category at two time points in 2015 and 2020, and use independent sample T-test to determine whether there is a statistically significant difference between the data at the two time points.

### Report （Li）

### Docs & PPT（Yao & Pan） 

## References
1. **Introduction to Remote Sensing in Vegetation Studies**
- Remote sensing has become a crucial tool for monitoring vegetation dynamics due to its ability to provide multi-temporal, high-resolution data.
- Pettorelli, N., et al. (2014). Satellite remote sensing for applied ecologists: opportunities and challenges. Journal of Applied Ecology, 51(4), 839-848.

2. **Vegetation Changes and Urban Parks**
- Urban parks play a vital role in maintaining biodiversity and regulating the urban environment. Remote sensing helps in tracking the changes in vegetation over time, especially in rapidly urbanizing regions such as Shenzhen.
- Zhou, W., et al. (2011). Urban green space dynamics and its association with urbanization: A case study of Shanghai, China. Landscape and Urban Planning, 100(3), 186-194.

3. **Use of Landsat and NDVI for Vegetation Monitoring**
- Landsat data and NDVI (Normalized Difference Vegetation Index) are widely used for assessing vegetation health and detecting changes in plant phenology.
- Tucker, C. J. (1979). Red and photographic infrared linear combinations for monitoring vegetation. Remote Sensing of Environment, 8(2), 127-150.

4. **Case Study: Vegetation Changes in Shenzhen**
- Shenzhen has undergone rapid urbanization, affecting its green spaces. Recent studies have used remote sensing to track these changes.
Wu, J., et al. (2014). Urban green space changes in Shenzhen, China: A remote sensing perspective. Remote Sensing, 6(10), 9387-9406.

5. **Gaps in the Literature**
- While there is substantial research on urban green spaces and remote sensing, there is limited work focusing specifically on the detailed classification of different park types in rapidly urbanizing cities like Shenzhen.
- Seto, K. C., et al. (2012). Global forecasts of urban expansion to 2030 and direct impacts on biodiversity and carbon pools. Proceedings of the National Academy of Sciences, 109(40), 16083-16088.

