"""
Date: 2021.3.17
Author: 郑钦源
"""
import csv
from pyecharts import options as opts
from pyecharts.charts import Graph


# 全局变量的定义，jieba词库的扩充
chapter_list = ['一','二','三','四','五','六','七','八','九','十',
    '十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二']
singlename_list = ['仿生人', '加兰德']
character_list = [('里克','德卡德'), ('埃尔登','罗森'), ('蕾切尔','罗森'),
    ('伊兰','德卡德'), ('威尔伯','默瑟'), ('马克斯','波洛科夫'),
    ('伊姆加德','贝蒂'), ('罗伊','贝蒂'), ('哈里','布赖恩特'), ('菲尔','雷施'),
    ('戴夫','霍尔登'), ('鲁芭','勒夫特'), ('普里斯','斯特拉顿'),('约翰','伊西多尔')]
firstname_list = []
lastname_list = []
all_namewords = []
full_names = []
for w in singlename_list:
    all_namewords.append(w)
    full_names.append(w)
for c in character_list:
    all_namewords.append(c[0])
    all_namewords.append(c[1])
    firstname_list.append(c[0])
    lastname_list.append(c[1])
    full_names.append(c[0]+'·'+c[1])
full_names.sort()


##--- 第0步：准备工作
# 输入文件
#node_file_name = './data/仿生人会梦见电子羊吗-段落示例-人物节点.csv'
#link_file_name = './data/仿生人会梦见电子羊吗-段落示例-人物连接.csv'
node_file_name = './output/仿生人会梦见电子羊吗-人物节点.csv' # 手工增加国别分类
link_file_name = './output/仿生人会梦见电子羊吗-人物连接.csv'
# 输出文件
out_file_name = './output/关系图-仿生人会梦见电子羊吗.html'

##--- 第1步：从文件读入节点和连接信息
node_file = open(node_file_name, 'r')
node_line_list = node_file.readlines()
node_file.close()
del node_line_list[0]  # 删除标题行

link_file = open(link_file_name, 'r')
link_line_list = link_file.readlines()
link_file.close()
del link_line_list[0]  # 删除标题行

##--- 第2步：解析读入的信息，存入列表
# 类别列表，用于给节点分成不同系列，会自动用不同颜色表示
categories=[{}, {'name':'主人公同伴'}, {'name':'中期角色'},{'name':'后期角色'},{'name':'关键词'}]

node_in_graph = []
for one_line in node_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    node_in_graph.append(opts.GraphNode(
            name=one_line_list[0], 
            value=int(one_line_list[1]), 
            symbol_size=int(one_line_list[1])/20,  # 手动调整节点的尺寸
            category=int(one_line_list[2])))  # 类别，例如categories[2]=='蜀'
#print('-'*20)  # 测试点
link_in_graph = []
for one_line in link_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    link_in_graph.append(opts.GraphLink(
            source=one_line_list[0], 
            target=one_line_list[1], 
            value=int(one_line_list[2])))


##--- 第3步：画图
c = Graph(init_opts=opts.InitOpts(page_title='关系图-仿生人会梦见电子羊吗？',width='1400px',height='700px'))
c.add("", 
      node_in_graph, 
      link_in_graph, 
      edge_length=[100,400], 
      repulsion=100,
      categories=categories, 
      is_draggable = True,
#      linestyle_opts=opts.LineStyleOpts(curve=0.2),  # 增加连线弧度
      layout="force",  # "force"-力引导布局，"circular"-环形布局
      )
c.set_global_opts(title_opts=opts.TitleOpts(title="关系图-仿生人会梦见电子羊吗？"))
c.render(out_file_name)