#!/usr/bin/env python3
"""
连接测试脚本
用于验证 Alpaca API 连接和配置
"""

import sys
from config import load_config
from alpaca_trade_api.rest import REST


def test_connection():
    """测试API连接"""
    try:
        print("🔍 正在加载配置...")
        config = load_config()
        print("✅ 配置加载成功")
        
        print("\n📋 当前配置:")
        print(config)
        
        print("\n🔗 正在连接 Alpaca API...")
        api = REST(config.api_key, config.secret_key, config.base_url)
        
        print("📊 获取账户信息...")
        account = api.get_account()
        
        print("✅ API 连接成功!")
        print(f"   账户状态: {account.status}")
        print(f"   交易模式: {'模拟交易' if config.is_paper_trading() else '真实交易'}")
        print(f"   账户余额: ${account.cash}")
        print(f"   可用资金: ${account.buying_power}")
        
        print("\n📅 检查交易日历...")
        import datetime
        today = datetime.date.today()
        cal = api.get_calendar(start=today.isoformat(), end=today.isoformat())
        
        if cal:
            print(f"✅ 今天 ({today}) 是交易日")
            market_open = cal[0].open
            market_close = cal[0].close
            print(f"   市场开放时间: {market_open} - {market_close}")
        else:
            print(f"❌ 今天 ({today}) 不是交易日")
            
        print("\n🎯 测试完成! 您的配置正确，可以开始使用自动交易器。")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        print("\n🔧 请检查:")
        print("1. API 密钥是否正确")
        print("2. 网络连接是否正常")
        print("3. .env 文件是否存在并配置正确")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1) 