import jieba
import jieba.posseg as pseg

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
    jieba.add_word(w)
for c in character_list:
    all_namewords.append(c[0])
    all_namewords.append(c[1])
    jieba.add_word(c[0])
    jieba.add_word(c[1])
    firstname_list.append(c[0])
    lastname_list.append(c[1])
    full_names.append(c[0]+'·'+c[1])
full_names.sort()

def naive_cut(txt_filepath):
    result_filename = './output/仿生人会梦见电子羊吗-人物关系.csv'

    txt_file = open(txt_filepath, 'r', encoding='utf-8')
    line_list = txt_file.readlines()
    txt_file.close()
    
    ##--- 第1步：生成基础数据（一个列表，一个字典）
    line_name_list = []  # 每个段落出现的人物列表
    name_cnt_dict = {}  # 统计人物出现次数

    for line in line_list: # 逐个段落循环处理
        line_name_list.append([])
        for w in all_namewords:
            if w in line:
                if w != "德卡德" and w != "贝蒂":
                    for fn in full_names:
                        if w in fn:
                            line_name_list[-1].append(fn)
                            break
                else:
                    if w == "德卡德":
                        line_name_list[-1].append('里克·德卡德')

    relation_dict = {}
    for line_name in line_name_list:
        for name1 in line_name:  # 判断该人物name1是否在字典中
            if name1 in relation_dict.keys():
                pass  # 如果已经在字典中，继续后面的统计工作
            else:
                relation_dict[name1] = {}  # 把name1加入字典“键”，作为连接的起点
                #print('add ' + name1)  # 测试点
            
            # 统计name1与本段的所有人名（除了name1自身）的共现数量
            for name2 in line_name:
                if name2 == name1:   # 不统计name1自身
                    continue
                # 检查name1的值列表（即连接的终点）中是否已经有name2
                if name2 in relation_dict[name1].keys():
                    relation_dict[name1][name2] = relation_dict[name1][name2] + 1
                else:
                    relation_dict[name1][name2] = 1

    ##--- 第3步：输出统计结果
    #for k,v in relation_dict.items():  # 测试点
    #    print(k, ':', v)

    link_file = open(result_filename, 'w')
    # 连接文件，格式：Source,Target,Weight -> 人名1,人名2,共现数量
    link_file.write('Source,Target,Weight\n')
    for name1,link_dict in relation_dict.items():
        for name2,link in link_dict.items():
            link_file.write(name1 + ',' + name2 + ',' + str(link) + '\n')
    link_file.close()

naive_cut('./data/仿生人会梦见电子羊吗.txt')