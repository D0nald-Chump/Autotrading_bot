# ❓ 常见问题 FAQ

## 📋 目录
- [基础问题](#基础问题)
- [安装问题](#安装问题)
- [配置问题](#配置问题)
- [运行问题](#运行问题)
- [交易问题](#交易问题)
- [安全问题](#安全问题)
- [高级问题](#高级问题)

---

## 🔰 基础问题

### Q1: 这个脚本是做什么的？
**A**: 这是一个自动化股票交易脚本，会在您设定的时间自动买入指定的股票（默认是QQQ）。就像设定一个闹钟，到时间就自动帮您买股票。

### Q2: 我需要什么基础知识？
**A**: 您需要：
- 基本的电脑操作能力（复制粘贴、编辑文本文件）
- 一个Alpaca交易账户
- 不需要编程经验

### Q3: 会不会很复杂？
**A**: 不会，按照快速入门指南，5分钟就能运行起来。

### Q4: 免费吗？
**A**: 是的，完全免费：
- 脚本本身免费
- Alpaca账户免费
- 模拟交易免费

---

## 🛠️ 安装问题

### Q5: 如何安装Python？
**A**: 
- **Windows**: 从 [python.org](https://www.python.org/downloads/) 下载安装包，勾选"Add Python to PATH"
- **Mac**: 使用 `brew install python3` 或从官网下载
- **Linux**: 使用包管理器，如 `apt install python3`

### Q6: 安装时报错"找不到Python"怎么办？
**A**: 
1. 确认Python已正确安装
2. 重新安装Python时勾选"Add Python to PATH"
3. 重启命令行窗口

### Q7: `pip install` 失败怎么办？
**A**: 
```bash
# 尝试使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 或者升级pip
python -m pip install --upgrade pip
```

### Q8: 虚拟环境是什么？必须要吗？
**A**: 虚拟环境是Python的隔离环境，不是必须的，但强烈推荐：
- 避免包冲突
- 保持系统环境干净
- 方便管理依赖

---

## ⚙️ 配置问题

### Q9: 如何获取Alpaca API密钥？
**A**: 
1. 注册 [Alpaca](https://alpaca.markets/) 账户
2. 登录后进入"API Keys"页面
3. 点击"Generate New Key"
4. 复制 Key ID 和 Secret Key

### Q10: 模拟交易和真实交易有什么区别？
**A**: 
| 模拟交易 | 真实交易 |
|---------|---------|
| 虚拟资金 | 真实资金 |
| 无风险 | 有风险 |
| 练习用 | 正式交易 |
| `paper-api.alpaca.markets` | `api.alpaca.markets` |

### Q11: 配置文件里的参数都是什么意思？
**A**: 
- `APCA_API_KEY_ID`: 您的API密钥ID
- `APCA_API_SECRET_KEY`: 您的API密钥Secret
- `TRADING_SYMBOL`: 股票代码（QQQ、AAPL等）
- `TRADING_QUANTITY`: 买入数量
- `TRIGGER_TIME`: 触发时间（24小时制）

### Q12: 时间设置用什么时区？
**A**: 使用美国东部时间（EST/EDT）：
- 夏令时: EDT (UTC-4)
- 冬令时: EST (UTC-5)
- 交易时间: 09:30-16:00

---

## 🏃 运行问题

### Q13: 如何知道脚本是否正在运行？
**A**: 
- 查看控制台输出
- 检查日志文件: `tail -f auto_trader.log`
- 运行测试: `python test_connection.py`

### Q14: 脚本运行后什么都没显示怎么办？
**A**: 
- 检查是否到达触发时间
- 检查是否是交易日
- 使用 `--once` 参数测试
- 查看日志文件

### Q15: 如何停止脚本？
**A**: 
- 按 `Ctrl+C` 停止
- 关闭命令行窗口
- 使用任务管理器结束进程

### Q16: 脚本可以后台运行吗？
**A**: 
```bash
# Linux/Mac 后台运行
nohup python auto_trader.py &

# Windows 使用任务计划程序
# 或者使用 pm2 等进程管理器
```

---

## 📈 交易问题

### Q17: 为什么没有执行交易？
**A**: 检查以下几点：
1. 当前时间是否匹配触发时间
2. 今天是否是交易日
3. 账户余额是否充足
4. 股票代码是否正确
5. 市场是否开放

### Q18: 可以买入多只股票吗？
**A**: 当前版本只支持一只股票，如需多只：
- 创建多个配置文件
- 同时运行多个脚本实例

### Q19: 支持卖出操作吗？
**A**: 当前版本只支持买入，卖出功能计划在后续版本中添加。

### Q20: 如何设置止损止盈？
**A**: 当前版本不支持，可以：
- 在Alpaca网站手动设置
- 使用其他交易软件
- 等待后续版本更新

### Q21: 交易失败了怎么办？
**A**: 
1. 查看错误日志
2. 检查账户余额
3. 确认股票代码有效
4. 检查网络连接
5. 联系Alpaca客服

---

## 🔒 安全问题

### Q22: API密钥安全吗？
**A**: 
- 密钥保存在本地 `.env` 文件中
- 不会上传到服务器
- 建议定期更换密钥
- 不要分享给他人

### Q23: 会不会被黑客攻击？
**A**: 
- 使用官方API，安全性高
- 建议使用模拟交易测试
- 定期更新软件
- 使用防火墙和杀毒软件

### Q24: 如何保护我的资金？
**A**: 
- 先使用模拟交易
- 设置交易限额
- 定期检查账户
- 不要在公共网络使用

---

## 🚀 高级问题

### Q25: 如何修改检查频率？
**A**: 
```bash
# 每30秒检查一次
python auto_trader.py --interval 30
```

### Q26: 如何添加更多股票？
**A**: 
目前需要运行多个脚本实例：
```bash
# 终端1
python auto_trader.py --config qqq.env

# 终端2  
python auto_trader.py --config aapl.env
```

### Q27: 如何自定义交易策略？
**A**: 
- 修改 `auto_trader.py` 文件
- 在 `should_trade_now()` 方法中添加条件
- 需要Python编程知识

### Q28: 如何添加邮件通知？
**A**: 
可以修改代码添加邮件功能，或使用第三方监控工具。

### Q29: 支持其他交易平台吗？
**A**: 
目前只支持Alpaca，添加其他平台需要：
- 修改API接口
- 适配不同的数据格式
- 处理不同的认证方式

### Q30: 如何贡献代码？
**A**: 
1. Fork项目
2. 创建功能分支
3. 提交代码
4. 创建Pull Request

---

## 📞 获取更多帮助

### 文档资源
- 📚 详细说明: `用户手册.md`
- ⚡ 快速上手: `快速入门指南.md`
- 📖 项目文档: `README.md`

### 社区支持
- 🐛 报告问题: [GitHub Issues](https://github.com/yourusername/auto-trader/issues)
- 💬 讨论交流: [GitHub Discussions](https://github.com/yourusername/auto-trader/discussions)
- 📧 邮件联系: your.email@example.com

### 提问建议
在提问时，请提供：
1. 操作系统和Python版本
2. 详细的错误信息
3. 重现问题的步骤
4. 配置文件内容（删除敏感信息）

---

## 🔄 更新日志

### 常见问题持续更新中...

如果您有新的问题或建议，欢迎：
- 在GitHub Issues中提出
- 通过邮件联系我们
- 在社区讨论区分享

**我们会持续改进这个FAQ文档，让更多用户能够顺利使用自动交易脚本！**

---

*最后更新: 2025年7月10日* 