# Group Project Presentation
> Notice of Preliminary  :
> - A 3-minute brief introduction to the project topic, literature investigation, and implementation plan, presented with ~5 slides.
> - Time: Oct 23, 2024
> - Send slides to LIU Xindi, Cindy at xindi1025.liu@connect.polyu.hk before 2:00PM on Oct 23, 2024

## Remote sensing-based evolutionary analysis of park vegetation - A case study of Shenzhen City

### 1. 研究意义背景 | Research Significance & Background （1页 Feng）
#### Background
In recent years, the rapid development of urbanization in Shenzhen has led to significant changes in land use/land cover. Urban green space has important effects on urban biodiversity and urban heat island.

#### Significance
Through the analysis of vegetation evolution in Shenzhen park, it is helpful to provide information for urban vegetation planning, environmental management and strengthening ecological health of the city.

### 2. 文献综述 | Literature Review （2页 Liang）

#### 1. Page 1
In vegetation analysis by remote sensing, remote sensing provides multi-temporal and high-resolution data that allow us to monitor vegetation dynamics.The study by Pettorelli et al. (2014) points out that remote sensing has a great potential for application in ecological research, but also faces challenges in interpreting the data.
 
Next up is the question of vegetation change in urban parks. zhou et al. (2011) studied the situation in Shanghai, showing how urban green spaces change as urbanization progresses. We can learn from these studies and combine remote sensing techniques to analyze vegetation evolution in urban parks.
 
Landsat satellite data and the NDVI index are widely used in vegetation health monitoring. the NDVI method proposed by Tucker (1979) has become a common tool for assessing vegetation health.
 
Next, we will see a specific case study where Wu et al. (2014) analyzed the impact of urbanization on green space in Shenzhen. They used remote sensing to show the changes in vegetation in Shenzhen parks.
 
However, despite the large number of studies on urban green spaces and remote sensing, there are still fewer studies that address the detailed classification of different types of parks under rapid urbanization.Seto et al. (2012) point out that the direct impacts of global urban expansion on biodiversity and carbon sinks need more research.
 
From these literature reviews, we can conclude that remotely sensed data, especially Landsat and NDVI, are significant in monitoring vegetation in urban parks, especially in rapidly urbanizing areas like Shenzhen. Based on these methods, this study will further analyze the evolution of park vegetation and classify different types of parks.
 
#### 2. Page 2

In this map, we can see the NDVI image of Shenzhen in 2020. This map was generated from Landsat data and shows the health of vegetation in different areas.
 
In the map, the green areas indicate areas with more lush vegetation, while the yellow areas show areas with less vegetation or in poorer health.The NDVI index is derived by calculating the difference between the near-infrared and red light bands, a method that is very effective in reflecting the growth of vegetation.
 
By analyzing these NDVI data, we can more accurately assess the vegetation health of different parks in Shenzhen and further study the impact of urbanization on these parks. The next study will be based on these data to classify different types of parks and explore their relationship with surrounding urbanization.”

### 3. 数据 & 研究范围 | Data & Study Areab （1页）（Zeng & Zhou）

   | name | type | time | resolution | source |
   | --- | --- | --- | --- | --- |
   | OSM | vector | 2024 | 1m | Zeng |
   | 地表覆盖分类(GLC_FCS30-2020) | raster | 2000 - 2020(+5) | 30m | https://data.casearth.cn/dataset/5fbc7904819aec1ea2dd7061 |
   | Landsat | raster | 2000 - 2020 | 30m | https://earthexplorer.usgs.gov/ |


### 4. 研究方法 & 研究计划（1页）（Dong）
1. 公园数据预处理及分类
   1. 根据公园矢量边界计算面积，并舍去面积小于指定阈值的公园
   2. 结合 Landsat 影像数据 ：根据公园周边建筑物分布（例如归一化建筑物指数）划分城市公园和自然公园
   3. 结合人口密度数据 ：分析公园潜在的效益及受益人群
2. 植被面积变化分析
   1. 利用 Landsat 和 GLC_FCS30-2020 数据，计算植被面积变化
   2. 利用 NDVI 数据，分析植被变化趋势
3. 物候信息提取
   1. 利用 Landsat 和 GLC_FCS30-2020 数据计算 NDVI 数据，并拟合物候模型提取公园植被物候

### Report （Li）

### Docs & PPT（Yao & Pan） 

## References
1. Examining Vegetation Change and Associated Spatial Patterns in Wuyishan National Park at Different Protection Levels : https://www.webofscience.com/wos/woscc/full-record/WOS:000781585600001
2. 2013~2023深圳湾红树林的分布变化 : https://www.hanspub.org/journal/paperinformation?paperid=95206
3. Analysis of Changes in Vegetation Condition in Grasslands National Park Using Remote Sensing	: https://www.webofscience.com/wos/woscc/full-record/WOS:000260989400146
4. WANG Haiyi，WANG Hongrong，CHEN Shuxin，et al.Dynamic change analysis of vegetation cover‐age and landscape pattern characteristics in Longquan Mountain Urban Forest Park， Chengdu City［J］.Remote Sensing Technology and Application，2023，38（6）：1455-1466.［王海熠，王洪荣，陈树新，等.成都市龙泉山城市森林公园植被覆盖度与景观格局特征动态变化分析［J］.遥感技术与应用，2023，38（6）：1455-1466.］
5. 2000—2020 年我国五大国家公园植被覆盖时空变化特征
