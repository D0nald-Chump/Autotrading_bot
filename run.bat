@echo off
REM 自动交易器启动脚本 (Windows版)

echo 🚀 自动交易器启动脚本
echo =======================

REM 检查Python版本
python --version
if %errorlevel% neq 0 (
    echo ❌ 未找到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

REM 检查是否存在虚拟环境
if exist "venv\" (
    echo 🔄 激活虚拟环境...
    call venv\Scripts\activate.bat
) else (
    echo ⚠️  未找到虚拟环境，建议创建虚拟环境
    echo    python -m venv venv
    echo    venv\Scripts\activate.bat
    echo    pip install -r requirements.txt
)

REM 检查配置文件
if not exist ".env" (
    echo ❌ 未找到 .env 配置文件
    echo 请复制 env.example 为 .env 并填入您的API密钥
    echo    copy env.example .env
    pause
    exit /b 1
)

REM 测试连接
echo 🔍 测试API连接...
python test_connection.py
if %errorlevel% neq 0 (
    echo ❌ 连接测试失败，请检查配置
    pause
    exit /b 1
)

echo ✅ 连接测试成功

REM 启动交易器
echo 🎯 启动自动交易器...
echo 按 Ctrl+C 停止
echo.

python auto_trader.py %*

pause 