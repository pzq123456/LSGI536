# Group Project Presentation
> Notice of Preliminary  :
> - A 3-minute brief introduction to the project topic, literature investigation, and implementation plan, presented with ~5 slides.
> - Time: Oct 23, 2024
> - Send slides to LIU Xindi, Cindy at xindi1025.liu@connect.polyu.hk before 2:00PM on Oct 23, 2024

## Remote sensing-based evolutionary analysis of park vegetation - A case study of Shenzhen City

### 1. 研究意义背景 | Research Significance & Background （1页 Feng）

### 2. 文献综述 | Literature Review （2页 Liang）

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
