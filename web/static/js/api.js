/**
 * API 模块 - 处理所有后端通信
 */

const API = {
    baseUrl: '',
    
    // 获取 API 配置
    getConfig() {
        return {
            base_url: document.getElementById('apiBaseUrl')?.value?.trim() || '',
            api_key: document.getElementById('apiKey')?.value?.trim() || ''
        };
    },
    
    // 保存 API 配置到本地
    saveConfig(config) {
        localStorage.setItem('llm_api_config', JSON.stringify(config));
    },
    
    // 加载 API 配置
    loadConfig() {
        const saved = localStorage.getItem('llm_api_config');
        return saved ? JSON.parse(saved) : null;
    },
    
    // 测试连接
    async testConnection(model) {
        const config = this.getConfig();
        const response = await fetch('/api/test-connection', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...config, model })
        });
        return response.json();
    },
    
    // 获取测试用例
    async getTestCases(dimension, lang = 'zh') {
        const response = await fetch(`/api/test-cases/${dimension}?lang=${lang}`);
        return response.json();
    },
    
    // 运行单个测试
    async runTest(params) {
        const config = this.getConfig();
        const response = await fetch('/api/test', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...config, ...params })
        });
        return response.json();
    },
    
    // 图片分类测试
    async classifyImage(imageData, model, prompts) {
        const config = this.getConfig();
        const response = await fetch('/api/classify-image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                ...config, 
                model, 
                image: imageData,
                ...prompts
            })
        });
        return response.json();
    },
    
    // 获取可用维度
    async getDimensions() {
        const response = await fetch('/api/dimensions');
        return response.json();
    },
    
    // 获取可用模型列表（预设）
    async getModels() {
        const response = await fetch('/api/models');
        return response.json();
    },
    
    // 从 API 获取可用模型列表
    async fetchModelsFromAPI() {
        const config = this.getConfig();
        if (!config.base_url || !config.api_key) {
            throw new Error('请先配置 API Base URL 和 API Key');
        }
        
        const response = await fetch('/api/fetch-models', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(config)
        });
        
        const result = await response.json();
        if (!result.success) {
            throw new Error(result.error || '获取模型列表失败');
        }
        
        return result.models || [];
    }
};

// 导出
window.API = API;

