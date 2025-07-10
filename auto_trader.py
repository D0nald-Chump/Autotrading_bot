#!/usr/bin/env python3
"""
自动交易脚本 - 每日定时购买QQQ
基于Alpaca Trading API实现自动化股票交易
"""

import os
import sys
import time
import logging
import datetime
import pytz
import argparse
from typing import Optional

from alpaca_trade_api.rest import REST
from dotenv import load_dotenv


class AutoTrader:
    """自动交易类"""
    
    def __init__(self, config_path: str = ".env"):
        """
        初始化交易器
        
        Args:
            config_path: 环境变量文件路径
        """
        self.setup_logging()
        self.load_config(config_path)
        self.setup_api()
        self.eastern = pytz.timezone("US/Eastern")
        
    def setup_logging(self):
        """设置日志记录"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('auto_trader.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def load_config(self, config_path: str):
        """加载配置"""
        if os.path.exists(config_path):
            load_dotenv(config_path)
            
        self.api_key = os.getenv("APCA_API_KEY_ID")
        self.secret_key = os.getenv("APCA_API_SECRET_KEY")
        self.base_url = os.getenv("APCA_BASE_URL", "https://paper-api.alpaca.markets")
        self.symbol = os.getenv("TRADING_SYMBOL", "QQQ")
        self.quantity = int(os.getenv("TRADING_QUANTITY", "1"))
        self.trigger_time = os.getenv("TRIGGER_TIME", "15:50")
        
        if not self.api_key or not self.secret_key:
            raise ValueError("请设置API密钥环境变量：APCA_API_KEY_ID 和 APCA_API_SECRET_KEY")
            
    def setup_api(self):
        """初始化API连接"""
        try:
            self.api = REST(self.api_key, self.secret_key, self.base_url)
            # 测试连接
            account = self.api.get_account()
            self.logger.info(f"API连接成功 - 账户状态: {account.status}, 可用资金: ${account.cash}")
        except Exception as e:
            self.logger.error(f"API连接失败: {e}")
            raise
            
    def is_trading_day(self, date: datetime.date) -> bool:
        """
        检查是否为交易日
        
        Args:
            date: 要检查的日期
            
        Returns:
            bool: 是否为交易日
        """
        try:
            cal = self.api.get_calendar(start=date.isoformat(), end=date.isoformat())
            return len(cal) > 0
        except Exception as e:
            self.logger.error(f"获取交易日历失败: {e}")
            return False
            
    def place_buy_order(self) -> bool:
        """
        提交买单
        
        Returns:
            bool: 是否成功提交订单
        """
        try:
            self.logger.info(f"⏳ 准备提交 {self.symbol} 买单...")
            
            order = self.api.submit_order(
                symbol=self.symbol,
                qty=self.quantity,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            
            self.logger.info(f"✅ 已提交 {self.quantity} 股 {self.symbol} 市价买单")
            self.logger.info(f"订单ID: {order.id}, 状态: {order.status}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ 下单失败: {e}")
            return False
            
    def should_trade_now(self, now: datetime.datetime) -> bool:
        """
        检查当前是否应该交易
        
        Args:
            now: 当前时间
            
        Returns:
            bool: 是否应该交易
        """
        time_str = now.strftime('%H:%M')
        
        # 检查是否是交易日
        if not self.is_trading_day(now.date()):
            self.logger.info(f"❌ {now.date()} 不是交易日，跳过")
            return False
            
        # 检查是否到达触发时间
        if time_str == self.trigger_time:
            self.logger.info(f"🕒 {now.strftime('%Y-%m-%d %H:%M:%S')} 是交易日，触发下单")
            return True
        else:
            self.logger.debug(f"等待中：当前时间 {time_str}，不是 {self.trigger_time}")
            return False
            
    def run_once(self) -> bool:
        """
        运行一次检查
        
        Returns:
            bool: 是否执行了交易
        """
        now = datetime.datetime.now(self.eastern)
        
        if self.should_trade_now(now):
            success = self.place_buy_order()
            if success:
                time.sleep(61)  # 防止重复下单
                return True
        
        return False
        
    def run_continuous(self, check_interval: int = 60):
        """
        持续运行交易器
        
        Args:
            check_interval: 检查间隔（秒）
        """
        self.logger.info(f"🚀 自动交易器启动")
        self.logger.info(f"交易标的: {self.symbol}")
        self.logger.info(f"交易数量: {self.quantity}")
        self.logger.info(f"触发时间: {self.trigger_time} (美国东部时间)")
        self.logger.info(f"检查间隔: {check_interval}秒")
        
        try:
            while True:
                self.run_once()
                time.sleep(check_interval)
                
        except KeyboardInterrupt:
            self.logger.info("👋 用户中断，交易器停止")
        except Exception as e:
            self.logger.error(f"💥 交易器发生错误: {e}")
            raise


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="自动交易脚本")
    parser.add_argument("--config", default=".env", help="配置文件路径")
    parser.add_argument("--once", action="store_true", help="只运行一次检查")
    parser.add_argument("--interval", type=int, default=60, help="检查间隔（秒）")
    parser.add_argument("--dry-run", action="store_true", help="模拟运行（不实际下单）")
    
    args = parser.parse_args()
    
    try:
        trader = AutoTrader(args.config)
        
        if args.once:
            trader.run_once()
        else:
            trader.run_continuous(args.interval)
            
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 