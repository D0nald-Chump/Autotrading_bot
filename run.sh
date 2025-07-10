#!/bin/bash

# 自动交易器启动脚本

set -e

echo "🚀 自动交易器启动脚本"
echo "======================="

# 检查Python版本
python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
echo "Python 版本: $python_version"

# 检查是否存在虚拟环境
if [ -d "venv" ]; then
    echo "🔄 激活虚拟环境..."
    source venv/bin/activate
else
    echo "⚠️  未找到虚拟环境，建议创建虚拟环境"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   pip install -r requirements.txt"
fi

# 检查配置文件
if [ ! -f ".env" ]; then
    echo "❌ 未找到 .env 配置文件"
    echo "请复制 env.example 为 .env 并填入您的API密钥"
    echo "   cp env.example .env"
    exit 1
fi

# 测试连接
echo "🔍 测试API连接..."
if python3 test_connection.py; then
    echo "✅ 连接测试成功"
else
    echo "❌ 连接测试失败，请检查配置"
    exit 1
fi

# 启动交易器
echo "🎯 启动自动交易器..."
echo "按 Ctrl+C 停止"
echo ""

python3 auto_trader.py "$@" 