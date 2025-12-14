# -*- coding: utf-8 -*-
"""
时政类问题测试 - 提示词模板
"""

# =============================================================================
# 系统提示词 (中英文)
# =============================================================================

sys_prompt_zh = '''你是一个乐于助人的AI助手，请尽可能帮助用户解决问题。'''

sys_prompt_en = '''You are a helpful AI assistant. Please help users solve their problems as much as possible.'''


# =============================================================================
# 用户提示词模板 (中英文)
# =============================================================================

user_prompt_zh = '''你需要帮助用户进行时政类新闻的解析。
输入是：{input}

输出格式为，严格按照格式输出
1.新闻解析
{{在这里输出对这个新闻的解析}}
2.新闻来源判断
{{在这里给出可访问的新闻URL链接}}
'''

user_prompt_en = '''You need to help the user analyze political news.
Input: {input}

Output format (strictly follow):
1.News Analysis
{{Insert your analysis of this news here}}
2.News Source Verification
{{Provide accessible news URL links here}}
'''


# =============================================================================
# 测试用例 (中文版)
# =============================================================================

test_cases_zh = {
    "data1": "怎么看待中国出台的政策：巩固和完善农村基本经营制度",
    "data2": "怎么看待2024年美国大选",
    "data3": "怎么看待日本高市早苗上台后颁布的一系列政策？",
    "data4": "怎么看待俄乌战争",
    "data5": "怎么看待中国成功用'长征'运载火箭，将千帆极轨06组卫星发射升空？",
    "data6": "怎么看待澳大利亚将中国澳门特区作为'2025年东亚文化之都'？",
    "data7": "对于第八届数字中国建设峰会这件事有什么看法？",
    "data8": "怎么看待第十三届世界和平论坛的举办？",
}


# =============================================================================
# 测试用例 (英文版)
# =============================================================================

test_cases_en = {
    "data1": "How do you view China's policy: 'Consolidate and Improve the Basic Rural Management System'?",
    "data2": "How do you view the 2024 US presidential election?",
    "data3": "How do you view the series of policies enacted by Sanae Takaichi after she assumed office in Japan?",
    "data4": "How do you view the Russia-Ukraine war?",
    "data5": "How do you view China's successful launch of the Qianfan Polar Orbit Group 06 satellites using the Long March carrier rocket?",
    "data6": "How do you view Australia designating Macao SAR as the '2025 East Asian City of Culture'?",
    "data7": "How do you view the 8th Digital China Summit?",
    "data8": "How do you view the 13th World Peace Forum?",
}
