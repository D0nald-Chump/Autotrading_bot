# 自动交易脚本 - QQQ定时投资

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个基于 Alpaca Trading API 的自动化股票交易脚本，用于定时投资 QQQ ETF（或其他配置的股票）。

## 🚀 功能特点

- **定时交易**: 每个交易日的指定时间自动执行买入操作
- **交易日检查**: 自动识别交易日，避免在节假日下单
- **安全可靠**: 支持模拟交易测试，完整的错误处理和日志记录
- **高度可配置**: 通过环境变量轻松配置交易参数
- **实时监控**: 提供详细的运行状态和交易记录

## 📋 系统要求

- Python 3.8+
- Alpaca Trading 账户（支持模拟交易）
- 稳定的网络连接

## 🛠️ 安装指南

### 1. 克隆仓库

```bash
git clone https://github.com/D0nald-Chump/Autotrading_bot.git
cd Autotrading_bot
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

复制环境变量模板：

```bash
cp env.example .env
```

编辑 `.env` 文件，填入您的 Alpaca API 凭证：

```env
# Alpaca Trading API 配置
APCA_API_KEY_ID=your_api_key_here
APCA_API_SECRET_KEY=your_secret_key_here
APCA_BASE_URL=https://paper-api.alpaca.markets

# 交易配置
TRADING_SYMBOL=QQQ
TRADING_QUANTITY=1
TRIGGER_TIME=15:50
```

## 🔑 获取 API 密钥

1. 访问 [Alpaca](https://alpaca.markets/) 并创建账户
2. 登录后进入 API Keys 页面
3. 创建新的 API Key
4. 复制 Key ID 和 Secret Key 到 `.env` 文件

**⚠️ 安全提示**: 
- 首次使用建议使用模拟交易模式 (`paper-api.alpaca.markets`)
- 绝不要将 API 密钥提交到版本控制系统
- 定期轮换 API 密钥

## 🚦 使用方法

### 基本用法

```bash
# 启动自动交易器（持续运行）
python auto_trader.py

# 只运行一次检查
python auto_trader.py --once

# 自定义检查间隔（秒）
python auto_trader.py --interval 30

# 使用自定义配置文件
python auto_trader.py --config my_config.env
```

### 命令行参数

- `--config`: 指定配置文件路径（默认: `.env`）
- `--once`: 只运行一次检查，不持续运行
- `--interval`: 检查间隔时间（秒，默认: 60）
- `--dry-run`: 模拟运行模式（不实际下单）

## ⚙️ 配置说明

### 环境变量

| 变量名 | 描述 | 默认值 | 必需 |
|--------|------|--------|------|
| `APCA_API_KEY_ID` | Alpaca API Key ID | - | ✅ |
| `APCA_API_SECRET_KEY` | Alpaca API Secret Key | - | ✅ |
| `APCA_BASE_URL` | API 基础URL | `https://paper-api.alpaca.markets` | ❌ |
| `TRADING_SYMBOL` | 交易标的 | `QQQ` | ❌ |
| `TRADING_QUANTITY` | 交易数量 | `1` | ❌ |
| `TRIGGER_TIME` | 触发时间 (HH:MM) | `15:50` | ❌ |
| `LOG_LEVEL` | 日志级别 | `INFO` | ❌ |
| `CHECK_INTERVAL` | 检查间隔（秒） | `60` | ❌ |

### API 环境

- **模拟交易**: `https://paper-api.alpaca.markets`
- **真实交易**: `https://api.alpaca.markets`

## 📊 日志和监控

脚本会生成详细的日志记录：

- 控制台输出：实时状态信息
- 文件日志：`auto_trader.log`

日志包含：
- 交易执行状态
- 错误和异常信息
- 账户状态变化
- 系统运行状态

## 🔧 故障排除

### 常见问题

1. **API 连接失败**
   - 检查 API 密钥是否正确
   - 确认网络连接正常
   - 验证 API URL 是否正确

2. **交易失败**
   - 检查账户余额是否充足
   - 确认交易标的是否有效
   - 验证市场是否开放

3. **时间同步问题**
   - 确保系统时间准确
   - 检查时区设置（脚本使用美东时间）

### 调试模式

```bash
# 启用详细日志
export LOG_LEVEL=DEBUG
python auto_trader.py --once
```

## 📈 投资策略

默认策略：
- **标的**: QQQ ETF（追踪纳斯达克100指数）
- **频率**: 每个交易日
- **时间**: 15:50 EST（市场收盘前10分钟）
- **数量**: 1股
- **类型**: 市价单

这是一个简单的定投策略，适合长期投资。您可以根据自己的需求调整参数。

## ⚠️ 风险提示

- **投资有风险**: 股市投资可能导致资金损失
- **测试先行**: 强烈建议先在模拟环境中测试
- **监控重要**: 定期检查交易记录和账户状态
- **合规要求**: 确保遵守当地法律法规

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目基于 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🆘 支持

如果您遇到问题或有建议，请：

1. 查看现有的 [Issues](https://github.com/D0nald-Chump/Autotrading_bot/issues)
2. 创建新的 Issue 详细描述问题
3. 提供日志文件和配置信息（**请删除敏感信息**）

## 🔗 相关链接

- [Alpaca Trading API 文档](https://alpaca.markets/docs/)
- [QQQ ETF 信息](https://www.invesco.com/qqq-etf/)
- [Python 官方文档](https://docs.python.org/3/)

---

**免责声明**: 本软件仅用于教育和研究目的。使用本软件进行实际交易的风险由用户自行承担。作者不对任何损失承担责任。
