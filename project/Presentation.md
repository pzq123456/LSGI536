# Notice of Preliminary Group Project Presentation
> - A 3-minute brief introduction to the project topic, literature investigation, and implementation plan, presented with ~5 slides.
> - Time: Oct 23, 2024
> - Send slides to LIU Xindi, Cindy at xindi1025.liu@connect.polyu.hk before 2:00PM on Oct 23, 2024

## Remote sensing-based evolutionary analysis of park vegetation - A case study of Shenzhen City

### 1. 研究意义背景

### 2. 文献综述

### 3. 数据

- OSM 公园边界数据（Zeng）（2024）筛选大小公园
  - 公园分类
- 30m 分辨率的地表覆盖 (https://data.casearth.cn/dataset/5fbc7904819aec1ea2dd7061) 2000 - 2020 (间隔5年)
- Landsat 遥感影像数据 


｜ name | type | time | resolution | source |
| --- | --- | --- | --- | --- |
| OSM | vector | 2024 | 1m | Zeng |
| 地表覆盖分类(GLC_FCS30-2020) | raster | 2000 - 2020(+5) | 30m | https://data.casearth.cn/dataset/5fbc7904819aec1ea2dd7061 |
| Landsat | raster | 2000 - 2020 | 30m | https://earthexplorer.usgs.gov/ |


### 4. 研究范围
1. 时间范围： 2015 - 2020 年
2. 


### 4. 研究方法 & 研究计划
1. 植被面积变化 LandSat + GLC_FCS30-2020
2. NDVI 变化分析（现成的）
3. 提取物候信息，LandSat + GLC_FCS30-2020
   1. NDVI 一年曲线 拟合 模型 
4. 公园分类（基于矢量数据）
   1. 面积 
   2. 根据周边的建筑物 城市公园和自然公园 
   3. 人口密度 

## References
1. Examining Vegetation Change and Associated Spatial Patterns in Wuyishan National Park at Different Protection Levels : https://www.webofscience.com/wos/woscc/full-record/WOS:000781585600001
2. 2013~2023深圳湾红树林的分布变化 : https://www.hanspub.org/journal/paperinformation?paperid=95206
3. Analysis of Changes in Vegetation Condition in Grasslands National Park Using Remote Sensing	: https://www.webofscience.com/wos/woscc/full-record/WOS:000260989400146
4. WANG Haiyi，WANG Hongrong，CHEN Shuxin，et al.Dynamic change analysis of vegetation cover‐age and landscape pattern characteristics in Longquan Mountain Urban Forest Park， Chengdu City［J］.Remote Sensing Technology and Application，2023，38（6）：1455-1466.［王海熠，王洪荣，陈树新，等.成都市龙泉山城市森林公园植被覆盖度与景观格局特征动态变化分析［J］.遥感技术与应用，2023，38（6）：1455-1466.］
5. 2000—2020 年我国五大国家公园植被覆盖时空变化特征
