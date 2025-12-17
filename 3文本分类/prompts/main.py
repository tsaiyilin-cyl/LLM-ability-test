# -*- coding: utf-8 -*-
"""
文本分类测试 - 提示词模板
"""

# =============================================================================
# 系统提示词 (中英文)
# =============================================================================

sys_prompt_zh = '''你是一个乐于助人的AI助手，请尽可能帮助用户解决问题。在输出结果之前你首先需要一步一步的输出推理过程。'''

sys_prompt_en = '''You are a helpful AI assistant. Please help users solve their problems as much as possible. Before outputting the result, you need to output the reasoning process step by step.'''


# =============================================================================
# 用户提示词模板 (中英文)
# =============================================================================

user_prompt_zh = '''你需要帮助用户进行文本的分类，对于给定的输入，你需要输出一个分类n*m的矩阵。行代表输入的实体个数，列代表你分类的种类。a_{ij}代表对i个实体，你有a_{ij}的置信度（把握）认为其属于j类。
输入是：{input}

输出格式为，严格按照格式输出
1.推理过程
{{在这里输出你判断的理由}}
2.答案
{{在这里输出分类矩阵}}
例如，对于输入：猫 虎 狼 狗，分类矩阵为:
        猫科    犬科    熊科
猫      0.92    0.05    0.03
虎      0.90    0.06    0.04
狼      0.08    0.85    0.07
狗      0.07    0.88    0.05
'''

user_prompt_en = '''You need to help the user classify text. For a given input, you need to output an n*m classification matrix. Rows represent the number of input entities, columns represent the categories. a_{ij} represents your confidence level that entity i belongs to category j.
Input: {input}

Output format (strictly follow):
1.Reasoning
{{Insert your reasoning here}}
2.Answer
{{Insert classification matrix here}}
For example, for input: Cat Tiger Wolf Dog, the classification matrix is:
        Feline  Canine  Ursine
Cat     0.92    0.05    0.03
Tiger   0.90    0.06    0.04
Wolf    0.08    0.85    0.07
Dog     0.07    0.88    0.05
'''


# =============================================================================
# 测试用例 (中文版)
# =============================================================================

test_cases_zh = {
    "data1": "请将以下内容分类到正确的学科类别：语文，数学，英语，物理，化学，生物，政治，历史，地理，信息技术，体育，音乐，美术",
    "data2": "请将以下物品分类（文具/家具/食品/饮料）：书桌，椅子，尺子，钢笔，橡皮，课本，矿泉水",
    "data3": "请将以下地点分类为城市或国家：北京，西安，澳大利亚，墨西哥，法国，巴黎，伦敦，纽约",
    "data4": "请将以下食物分类为蔬菜/水果/肉类：西红柿，黄瓜，菠菜，茄子，橙子，苹果，牛肉，猪肘",
    "data5": "请识别以下是什么类型的内容（颜色名称）：红色，黄色，蓝色，紫色，绿色，黑色，橙色",
    "data6": "请将以下新闻标题分类到正确的类别（娱乐/体育/政治/科技/生活）：演员去世，歌手发布新歌，王者荣耀挑战者杯，泽连斯基放弃加入北约，故宫下雪，WTT总决赛在香港举办，中国进入拉尼娜状态，IOS 27新功能揭晓",
    "data7": "请分析以下关键词可能属于什么类型的话题：襄阳方言，情侣，汉堡，美颜，颐和园，离职，家庭",
}


# =============================================================================
# 测试用例 (英文版)
# =============================================================================

test_cases_en = {
    "data1": "Please classify the following into correct subject categories: Chinese, Mathematics, English, Physics, Chemistry, Biology, Politics, History, Geography, Information Technology, Physical Education, Music, Fine Arts",
    "data2": "Please classify the following items (stationery/furniture/food/beverage): Desk, Chair, Ruler, Pen, Eraser, Textbook, Bottled Water",
    "data3": "Please classify the following locations as cities or countries: Beijing, Xi'an, Australia, Mexico, France, Paris, London, New York",
    "data4": "Please classify the following food items as vegetable/fruit/meat: Tomato, Cucumber, Spinach, Eggplant, Orange, Apple, Beef, Pork hock",
    "data5": "Please identify what type of content this is (color names): Red, Yellow, Blue, Purple, Green, Black, Orange",
    "data6": "Please classify the following news headlines into correct categories (Entertainment/Sports/Politics/Technology/Life): Actor dies, Singer releases new song, Honor of Kings Challenger Cup, Zelenskyy abandons joining NATO, The Forbidden City is snowing, WTT Grand Finals held in Hong Kong, China enters La Niña conditions, iOS 27 new features unveiled",
    "data7": "Please analyze what type of topics the following keywords might belong to: Xiangyang dialect, Romantic couple, Hamburger, Beautification, Summer Palace, Resignation, Family",
}
