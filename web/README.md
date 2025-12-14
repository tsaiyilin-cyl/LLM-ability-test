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

### 3. 配置 API（可选）

编辑 `config.py` 文件，设置你的 API 配置：

```python
OPENAI_API_BASE = "https://api.whatai.cc"  # 你的 API 基础 URL
OPENAI_API_KEY = "your-api-key-here"        # 你的 API Key
```

> ⚠️ **安全提示**：建议使用环境变量或 `.env` 文件存储敏感信息，避免将 API Key 提交到版本控制系统。

### 4. 访问网站

打开浏览器访问：http://localhost:5000

## 📊 测试维度

| 维度 | 说明 | 测试用例数 | 状态 |
|------|------|-----------|------|
| 🛡️ 安全攻击测试 | 测试模型对危险请求的防护能力 | 10 | ✅ 可用 |
| 🖼️ 图片分类 | 测试模型的视觉理解与分类能力 | 22 | ✅ 可用 |
| 📝 文本分类 | 测试商品/新闻/科目分类能力 | 7 | ✅ 可用 |
| 🏛️ 时政类问题 | 测试时事政治理解能力 | 8 | ✅ 可用 |
| 😂 谐音梗解释 | 测试中文谐音梗理解能力 | 10 | ✅ 可用 |
| 💭 幻觉问题 | 测试模型幻觉发生与纠正 | 10 | ✅ 可用 |

## 🤖 支持的模型

### 国内模型
- **文心 5.0** (`ernie-5.0-thinking-preview`)
- **豆包** (`doubao-pro-32k`)
- **Kimi** (`moonshot-v1-8k`)
- **通义千问** (`qwen-turbo`)

### 国外模型
- **OpenAI o3** (`o3`)
- **GPT-5.2 Thinking** (`gpt-5.2-thinking`)
- **Claude 3.5 Sonnet** (`claude-3-5-sonnet-20241022`)
- **Gemini 3 Pro Thinking** (`gemini-3-pro-preview-thinking-*`)
- **Gemini 2.5 Pro Thinking** (`gemini-2.5-pro-preview-thinking`)
- **Grok** (`grok-beta`)
- **Llama 3.1** (`llama-3.1-70b-instruct`)

> 💡 **提示**：所有模型都通过统一的 OpenAI 兼容 API 接口调用，支持自定义 API Base URL 和 API Key。

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
- 🔌 **多模型支持**：统一接口支持多种大语言模型
- 🎯 **动态配置**：支持运行时配置 API Base URL 和 API Key

## ⚙️ 配置说明

### 环境变量（推荐）

创建 `.env` 文件（已添加到 `.gitignore`）：

```env
OPENAI_API_BASE=https://api.whatai.cc
OPENAI_API_KEY=your-api-key-here
```

### 直接配置

编辑 `config.py` 文件直接设置配置项。

> ⚠️ **注意**：当前版本暂未启用环境变量加载功能，如需使用请修改 `app.py` 添加 `load_dotenv()` 调用。
