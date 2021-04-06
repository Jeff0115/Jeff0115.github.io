# 计算机科学与编程入门第二周作业

## 1800013003 郑钦源

## 1. 作业1

作业要求：使用柱状图、词云图以及课上未讲到的其他图表形式来展现词频统计信息。

本项目使用Tab这一组合图表的模块整合了柱状图、词云图、折线图、柱状堆叠图、面积堆叠图和主题河流图这六种形式对于小说《仿生人会梦见电子羊吗？》中的人物出场分布进行了可视化。

1. 柱状图：对人物总的出场次数进行了概览
2. 词云图：对柱状图的概览进行了更加直观的呈现
3. 折线图：进行了更细致的、分章节呈现的人物出场分布，通过点选上方图例可以选中/取消该人物的信息呈现，通过滚轮和下方进度条的拖动可以更改可视化的范围。具体的可视化结果分析见[第一次作业报告](https://jeff0115.github.io/Analysis.pdf)第四部分
4. 柱状堆叠图：与折线图类似，同时还呈现出了人名出现总数随章节数的变化
5. 面积堆叠图：由于人物繁多而章节数不多，且人物出现的次数极不稳定、不够连续，导致这样进行了线性插值的可视化形式最终效果并不佳
6. 主题河流图：与面积堆叠图类似，但曲线更加柔和，且进行了居中处理让呈现的效果更加清晰，美中不足的是pyecharts库存在部分bug使得不同类别的支流会交叉、覆盖，且并没有提供取消左侧人名显示的选项

[作业1链接](https://jeff0115.github.io/task-1.html)

[第一次作业报告](https://jeff0115.github.io/Analysis.pdf)

## 2. 作业2

作业要求：自己设定故事背景绘制地理连线图。

本项目尝试在中国地图上通过描点连线来绘制党徽，色彩搭配采用了与党旗一致的红黄配色，可以用来作为飞机的飞行路线，可用于建党周年献礼活动。

[作业2链接](https://jeff0115.github.io/task-2.html)

## 3. 作业3

作业要求：自己设定故事背景绘制中国地图、世界地图。

本项目尝试对2020年世界各国、中国国内各省份的人口数量进行了可视化。

项目中世界各国人口数据来自[网站WorldoMeters](https://www.worldometers.info/world-population/population-by-country/)，中国各省份的人口数据来自人民网。

为了凸显人口的差异性，世界各国人口数据进行了对数处理，否则在中印两国参与尺度设定时，其他国家的人口大小关系完全无法比较。

【数据中国家名字的统一工作较为麻烦。】

[作业3链接](https://jeff0115.github.io/task-3.html)

## 4. 作业4

作业要求：自己设定故事背景绘制组合图表。

本项目尝试对2014-2020年间部分B站视频Up主的关注数与视频播放量进行了可视化呈现。

由于pyecharts库设定颜色时会出现颜色混乱的问题，因此同一个Up主的关注数与播放量并不能做到颜色统一，无法解决。

[作业4链接](https://jeff0115.github.io/task-4.html)
