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

### 3. 配置 API

有两种方式配置 API：

#### 方式一：Web 界面配置（推荐）

启动服务后，在 Web 界面的"API 配置"部分直接配置：
- API Base URL：你的 API 服务地址
- API Key：你的 API 密钥

配置会自动保存到浏览器本地存储，无需修改代码。

#### 方式二：配置文件

编辑 `config.py` 文件，设置默认的 API 配置：

```python
OPENAI_API_BASE = "https://api.whatai.cc"  # 你的 API 基础 URL
OPENAI_API_KEY = "your-api-key-here"        # 你的 API Key
```

> ⚠️ **安全提示**：
> - 建议使用 Web 界面配置，配置信息保存在浏览器本地，不会提交到版本控制系统
> - 如果使用配置文件，建议使用环境变量或 `.env` 文件存储敏感信息
> - 不要将包含真实 API Key 的 `config.py` 提交到版本控制系统

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

## 🤖 支持的 API 服务

平台支持所有符合 OpenAI 兼容 API 格式的服务。以下是常见的 API Base URL：

### 国内云服务商

- **阿里云（通义千问）**
  - Base URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`
  - 文档: [阿里云 DashScope](https://help.aliyun.com/zh/model-studio/)

- **腾讯云（混元）**
  - Base URL: `https://api.hunyuan.cloud.tencent.com`
  - 文档: [腾讯云混元](https://cloud.tencent.com/product/hunyuan)

- **百度（文心一言/千帆）**
  - Base URL: `https://qianfan.baidubce.com/v2`
  - 文档: [百度千帆](https://cloud.baidu.com/product/qianfan.html)
  - ⚠️ **注意**：平台会自动识别并添加 `/v2` 路径

- **字节跳动（豆包）**
  - Base URL: `https://ark.cn-beijing.volces.com/api/v3`
  - 文档: [火山引擎豆包](https://www.volcengine.com/product/doubao)

- **智谱AI（GLM）**
  - Base URL: `https://open.bigmodel.cn/api/paas/v4`
  - 文档: [智谱AI开放平台](https://open.bigmodel.cn/)

- **月之暗面（Kimi）**
  - Base URL: `https://api.moonshot.cn/v1`
  - 文档: [Moonshot AI](https://platform.moonshot.cn/)

### 国外服务商

- **OpenAI**
  - Base URL: `https://api.openai.com/v1`
  - 文档: [OpenAI API](https://platform.openai.com/docs)

- **Anthropic（Claude）**
  - Base URL: `https://api.anthropic.com/v1`
  - 文档: [Anthropic API](https://docs.anthropic.com/)

- **Google（Gemini）**
  - Base URL: `https://generativelanguage.googleapis.com/v1`
  - 文档: [Google AI Studio](https://makersuite.google.com/app/apikey)

### 代理服务

- **WhatAI**（示例）
  - Base URL: `https://api.whatai.cc/v1`
  - 说明：第三方代理服务，支持多种模型

> 💡 **提示**：
> - 所有 API 都通过统一的 OpenAI 兼容接口调用
> - 如果 Base URL 未包含版本号（如 `/v1`），平台会自动添加 `/v1`（文心一言自动添加 `/v2`）
> - 支持通过 `/api/fetch-models` 接口从 API 服务端动态获取可用模型列表
> - 具体模型名称请参考各服务商的文档

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
| `/api/models` | GET | 获取预设的可用模型列表 |
| `/api/fetch-models` | POST | 从 API 服务端动态获取可用模型列表 |
| `/api/test-cases/<dimension>` | GET | 获取指定维度的测试用例 |
| `/api/test-connection` | POST | 测试 API 连接 |
| `/api/test` | POST | 运行单个测试 |
| `/api/classify-image` | POST | 图片分类测试 |

## 💡 特性

- 🎨 **模块化设计**：CSS/JS 分离，易于维护
- 🌐 **多语言支持**：中英文测试用例和提示词
- ⚙️ **可配置提示词**：支持自定义 System/User Prompt
- 🖼️ **动态提示词**：图片分类根据测试类型（颜色识别/情绪识别/动物识别）自动选择对应提示词
- 📊 **实时统计**：测试结果实时统计和评估
- 🔒 **本地存储**：API 配置和提示词保存到本地浏览器
- 📱 **响应式设计**：适配不同屏幕尺寸
- 🔌 **多模型支持**：统一接口支持多种大语言模型
- 🎯 **动态配置**：支持运行时配置 API Base URL 和 API Key
- 🔄 **动态模型获取**：支持从 API 服务端自动获取可用模型列表
- 🛡️ **特殊 API 适配**：自动识别并适配文心一言（千帆平台）等特殊 API
- 🔁 **一致性测试**：图片分类支持多次询问测试推理一致性

## ⚙️ 配置说明

平台支持多种配置方式，按优先级从高到低：

### 1. Web 界面配置（推荐）

在 Web 界面的"API 配置"部分直接配置 API Base URL 和 API Key，配置会自动保存到浏览器本地存储。这是最推荐的方式，因为：
- 配置信息保存在浏览器本地，不会提交到版本控制系统
- 无需修改代码文件
- 支持动态切换不同的 API 配置

### 2. 配置文件

编辑 `config.py` 文件直接设置默认配置项：

```python
OPENAI_API_BASE = "https://api.whatai.cc"
OPENAI_API_KEY = "your-api-key-here"
```

> ⚠️ **安全提示**：不要将包含真实 API Key 的 `config.py` 提交到版本控制系统。

### 3. 环境变量（可选）

如需使用环境变量，可以修改 `app.py` 添加 `load_dotenv()` 调用：

```python
from dotenv import load_dotenv
load_dotenv()
```

然后在 `.env` 文件中设置（已添加到 `.gitignore`）：

```env
OPENAI_API_BASE=https://api.whatai.cc
OPENAI_API_KEY=your-api-key-here
```

> 💡 **配置优先级**：Web 界面配置 > 配置文件 > 环境变量

## 🖼️ 图片分类动态提示词

图片分类测试支持根据测试用例类型自动选择对应的系统提示词：

| 测试类型 | 系统提示词 |
|---------|-----------|
| 颜色识别 | "你是一个出色的颜色识别助手，对于用户输入的一张纯色图，正确输出正确的颜色类别。" |
| 情绪识别 | "你是一个出色的情绪识别助手，对于用户输入的一张图片，识别图片中人物的情绪。" |
| 动物识别 | "你是一个出色的图片分类助手，对于用户输入的一张图片，可以识别图片中的主体，并且输出正确的类别。" |

### 使用方式

- **自动模式**：保持系统提示词为默认值，系统会根据每个测试用例的类型自动选择对应的提示词
- **自定义模式**：修改系统提示词为非默认值，所有测试用例将使用您自定义的提示词

### 一致性测试

图片分类支持推理一致性测试，可在同一对话中多次询问模型，测试其回答是否一致：
- 勾选"启用推理一致性测试"
- 设置重复询问次数（2-10次）
- 系统会返回所有回答，供人工评估一致性
