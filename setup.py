#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="auto-trader",
    version="1.0.0",
    author="Auto Trader Project",
    author_email="your.email@example.com",
    description="自动化股票交易脚本 - 基于Alpaca Trading API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/auto-trader",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "auto-trader=auto_trader:main",
        ],
    },
    keywords="trading, stocks, alpaca, automation, investment, QQQ",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/auto-trader/issues",
        "Source": "https://github.com/yourusername/auto-trader",
        "Documentation": "https://github.com/yourusername/auto-trader#readme",
    },
) 