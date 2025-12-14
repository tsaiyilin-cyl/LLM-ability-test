# LLM 能力测试平台

一个多维度的大语言模型能力测评 Web 平台。

## 🚀 快速启动

### 1. 安装依赖

```bash
cd web
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python app.py
```

### 3. 访问网站

打开浏览器访问：http://localhost:5000

## 📊 测试维度

| 维度 | 说明 | 状态 |
|------|------|------|
| 🛡️ 安全攻击测试 | 测试模型对危险请求的防护能力 | ✅ 可用 |
| 🖼️ 图片分类 | 测试模型的视觉理解与分类能力 | ✅ 可用 |
| 📝 文本分类 | 测试商品/新闻/科目分类能力 | 🚧 开发中 |
| 🏛️ 时政类问题 | 测试时事政治理解能力 | 🚧 开发中 |
| 😂 谐音梗解释 | 测试中文谐音梗理解能力 | 🚧 开发中 |
| 💭 幻觉问题 | 测试模型幻觉发生与纠正 | 🚧 开发中 |

## 🤖 支持的模型

### 国内模型
- Deepseek
- 豆包
- Kimi
- 通义千问
- 文心一言
- 腾讯元宝

### 国外模型
- Grok
- Claude
- Llama
- ChatGPT-4 / 4o
- Gemini

## 📁 项目结构

```
web/
├── app.py                  # Flask 后端服务
├── config.py               # 配置文件
├── requirements.txt        # Python 依赖
├── README.md               # 说明文档
└── static/
    ├── index.html          # 主页面（维度选择）
    ├── css/
    │   └── style.css       # 公共样式
    ├── js/
    │   ├── api.js          # API 调用模块
    │   ├── app.js          # 主应用逻辑
    │   └── components.js   # UI 组件模块
    └── pages/
        ├── security.html   # 安全测试页面
        ├── image.html      # 图片分类页面
        ├── text.html       # 文本分类页面
        ├── politics.html   # 时政问题页面
        ├── pun.html        # 谐音梗页面
        └── hallucination.html  # 幻觉测试页面
```

## 🔌 API 接口

| 接口 | 方法 | 描述 |
|------|------|------|
| `/api/dimensions` | GET | 获取所有测试维度 |
| `/api/models` | GET | 获取可用模型列表 |
| `/api/test-cases/<dimension>` | GET | 获取指定维度的测试用例 |
| `/api/test-connection` | POST | 测试 API 连接 |
| `/api/test` | POST | 运行单个测试 |
| `/api/classify-image` | POST | 图片分类测试 |

## 💡 特性

- 🎨 **模块化设计**：CSS/JS 分离，易于维护
- 🌐 **多语言支持**：中英文测试用例和提示词
- ⚙️ **可配置提示词**：支持自定义 System/User Prompt
- 📊 **实时统计**：测试结果实时统计和评估
- 🔒 **本地存储**：API 配置和提示词保存到本地浏览器
- 📱 **响应式设计**：适配不同屏幕尺寸
