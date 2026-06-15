from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dskit-cli",
    version="1.0.0",
    author="Your Name",
    author_email="your@email.com",
    description="🔬 A fast, multi-language CLI utility belt for data scientists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dskit",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "pyarrow>=10.0.0",
        "openpyxl>=3.0.0",
        "tabulate>=0.9.0",
    ],
    extras_require={
        "profile": ["ydata-profiling>=4.0.0"],
        "dev": ["pytest", "black", "ruff"],
    },
    entry_points={
        "console_scripts": [
            "dskit=dskit.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="data science cli csv parquet json profiling cleaning statistics",
)
