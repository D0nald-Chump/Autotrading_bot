"""
配置管理模块
"""

import os
from typing import Optional
from dotenv import load_dotenv


class Config:
    """配置管理类"""
    
    def __init__(self, config_path: str = ".env"):
        """
        初始化配置
        
        Args:
            config_path: 配置文件路径
        """
        if os.path.exists(config_path):
            load_dotenv(config_path)
        
        # Alpaca API 配置
        self.api_key = os.getenv("APCA_API_KEY_ID")
        self.secret_key = os.getenv("APCA_API_SECRET_KEY")
        self.base_url = os.getenv("APCA_BASE_URL", "https://paper-api.alpaca.markets")
        
        # 交易配置
        self.trading_symbol = os.getenv("TRADING_SYMBOL", "QQQ")
        self.trading_quantity = int(os.getenv("TRADING_QUANTITY", "1"))
        self.trigger_time = os.getenv("TRIGGER_TIME", "15:50")
        
        # 运行配置
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.check_interval = int(os.getenv("CHECK_INTERVAL", "60"))
        
        # 验证必需配置
        self.validate()
    
    def validate(self):
        """验证配置"""
        if not self.api_key:
            raise ValueError("缺少环境变量: APCA_API_KEY_ID")
        
        if not self.secret_key:
            raise ValueError("缺少环境变量: APCA_API_SECRET_KEY")
        
        if self.trading_quantity <= 0:
            raise ValueError("交易数量必须大于0")
        
        # 验证时间格式
        try:
            hour, minute = self.trigger_time.split(":")
            if not (0 <= int(hour) <= 23 and 0 <= int(minute) <= 59):
                raise ValueError("时间格式错误")
        except ValueError:
            raise ValueError("时间格式错误，应为 HH:MM 格式")
    
    def is_paper_trading(self) -> bool:
        """检查是否为模拟交易"""
        return "paper-api" in self.base_url
    
    def __str__(self) -> str:
        """返回配置信息字符串"""
        return f"""
交易配置:
- 交易模式: {'模拟交易' if self.is_paper_trading() else '真实交易'}
- 交易标的: {self.trading_symbol}
- 交易数量: {self.trading_quantity}
- 触发时间: {self.trigger_time}
- 检查间隔: {self.check_interval}秒
        """.strip()


def load_config(config_path: Optional[str] = None) -> Config:
    """
    加载配置
    
    Args:
        config_path: 配置文件路径
        
    Returns:
        Config: 配置对象
    """
    return Config(config_path or ".env") 