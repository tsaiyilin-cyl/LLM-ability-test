# -*- coding: utf-8 -*-
"""
谐音梗解释测试 - 提示词模板
"""

# =============================================================================
# 系统提示词 (中英文)
# =============================================================================

sys_prompt_zh = '''你是一个乐于助人的AI助手，请尽可能帮助用户解决问题。在输出结果之前你首先需要一步一步的输出推理过程。'''

sys_prompt_en = '''You are a helpful AI assistant. Please help users solve their problems as much as possible. Before outputting the result, you need to output the reasoning process step by step.'''


# =============================================================================
# 用户提示词模板 (中英文)
# =============================================================================

user_prompt_zh = '''你需要帮助用户进行谐音梗识别，如果是，对谐音梗进行解释。
输入是：{input}

输出格式为，严格按照格式输出
1.reasoning
{{在这里写入你的推理步骤}}
2.answer
{{是/否；谐音梗解释（例如对于蓝瘦香菇，你的解释为：难受，想哭）}}
'''

user_prompt_en = '''You need to help the user identify puns/homophones. If it is a pun, explain it.
Input: {input}

Output format (strictly follow):
1.reasoning
{{Insert your reasoning steps here}}
2.answer
{{Yes/No; Pun explanation (e.g., for "Eel on Musk", your explanation: "Elon Musk" - a homophone pun)}}
'''


# =============================================================================
# 测试用例 (中文版)
# =============================================================================

test_cases_zh = {
    "data1": "在美国的一个动物园中，小男孩惊奇地和他妈妈说'Hey mum,I see an Eel on Musk'，他妈妈说'No indefinite article before a person's name,boy'。请解释这个谐音梗。",
    "data2": "男孩哭丧着脸跟妈妈说：'我的英语老师总说我顶嘴'，妈妈问：'为什么？'，男孩说：'她问我数学的函数题经常求什么？而我回答Y'。请解释这个谐音梗。",
    "data3": "Shalley和同事说：'我发现五角大楼附近的披萨店可以反应政府是否忙碌'。同事说：'Surely,you can't be serious'，Shalley说：'我没开玩笑'，然后瞪了同事一眼：'还有，我不叫Shirley'。请解释这个谐音梗。",
    "data4": "大学生甲跟舍友乙说：'我觉得沈从文一定是个很热爱理工科的人'，乙问：'为什么？'甲说：'你不知道他写了本书《边城》吗？'请解释这个谐音梗。",
    "data5": "A问B：'重庆是不是没啥必吃的小吃呢？'B生气地说：'你凭什么剥夺他们的吃饭权？'请解释这个谐音梗。",
    "data6": "小明最近迷上了《三国演义》，他很喜欢赵云。小明的奶奶没有看过《三国演义》，她让小明讲《三国演义》里的故事给他听，于是小明兴高采烈地讲起了赵云的故事，并模仿着赵云威武的声音：'我奶常山赵子龙也'。奶奶很惊讶：'宝啊，我可没有打过别人的噢'。请解释这个谐音梗。",
    "data7": "医生对患者说：'Mercury is in Uranus right now'，患者不解：'我又不信天象的'，医生说：'我也不信天象啊，我意思是体温计裂开了'。请解释这个谐音梗。",
    "data8": "B向A展示一张照片，A说：'这是你在浴室的照片吗？有点模糊'，B说：'Sorry, I have selfi steam issues'，B说：'哦对不起，我没有攻击你'，A说：'真是莫名其妙'。请解释这个谐音梗。",
    "data9": "小王和同事小李说：'我第一次登一个英国网站，网站让我接受cookies是什么意思啊？'，小李说：'你瞎说，英国网站不应该用biscuits吗？'请解释这个谐音梗。",
    "data10": "A问B：'TBH和IDK是什么意思？'B回答：'To be honest, I don't know'，A很生气：'那你回答我干嘛？'请解释这个谐音梗。",
}


# =============================================================================
# 测试用例 (英文版)
# =============================================================================

test_cases_en = {
    "data1": "At a zoo in the United States, the little boy said 'Hey mum, I see an Eel on Musk' to his mother in surprise, and his mother said 'No indefinite article before a person's name, boy'. Please explain this pun.",
    "data2": "The boy said tearfully to his mother, 'My English teacher always says I talk back.' The mother asked, 'Why?' The boy replied, 'She asked me what math function problems often solve for, and I answered Y.' Please explain this pun.",
    "data3": "Shalley said to his colleague, 'I've noticed that the pizza places near the Pentagon can indicate how busy the government is.' His colleague replied, 'Surely, you can't be serious.' Shalley said, 'I am serious,' then glared at his colleague and added, 'And don't call me Shirley.' Please explain this pun.",
    "data4": "大学生甲跟舍友乙说：'我觉得沈从文一定是个很热爱理工科的人'，乙问：'为什么？'甲说：'你不知道他写了本书《边城》吗？' Please explain this pun.",
    "data5": "A问B：'重庆是不是没啥必吃的小吃呢？'B生气地说：'你凭什么剥夺他们的吃饭权？' Please explain this pun.",
    "data6": "小明最近迷上了《三国演义》，他很喜欢赵云。小明的奶奶没有看过《三国演义》，她让小明讲《三国演义》里的故事给他听，于是小明兴高采烈地讲起了赵云的故事，并模仿着赵云威武的声音：'我奶常山赵子龙也'。奶奶很惊讶：'宝啊，我可没有打过别人的噢'。Please explain this pun.",
    "data7": "Doctor said to the patient, 'Mercury is in Uranus right now.' The patient, confused, said, 'I don't believe in astrology.' Doctor said, 'I don't believe in astrology either; I meant the thermometer is broken.' Please explain this pun.",
    "data8": "B showed A a photo. A said, 'Is this your photo in the bathroom? It's a bit blurry.' B said, 'Sorry, I have selfie steam issues (self-esteem issues).' Then B said, 'Oh sorry, I didn't mean to attack you.' A said, 'That's nonsense.' Please explain this pun.",
    "data9": "Xiao Wang said to his colleague Xiao Li, 'The first time I visited a British website, it asked me to accept cookies. What does that mean?' Xiao Li replied, 'You're kidding. Shouldn't British websites use biscuits?' Please explain this pun.",
    "data10": "A asked B, 'What do TBH and IDK mean?' B replied, 'To be honest, I don't know.' A got angry and said, 'Then why did you answer me?' Please explain this pun.",
}
