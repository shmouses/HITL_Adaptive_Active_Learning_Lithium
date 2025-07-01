"""
Setup script for HITL Adaptive Active Learning Lithium project.

This script allows for easy installation and development setup of the project.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    """Read README.md file for long description."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Read requirements from requirements.txt
def read_requirements():
    """Read requirements from requirements.txt file."""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="hitl-lithium",
    version="1.0.0",
    author="Shayan Mousavi Masouleh",
    author_email="",
    description="Human-AI Synergy in Adaptive Active Learning for Lithium Carbonate Crystallization Optimization",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/shmouses/HITL_Adaptive_Active_Learning_Lithium",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "jupyter>=1.0.0",
            "notebook>=7.0.2",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "nbsphinx>=0.8.0",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.xlsx", "*.npy", "*.json"],
    },
    entry_points={
        "console_scripts": [
            "hitl-lithium=hitl_lithium.cli:main",
        ],
    },
    keywords=[
        "active learning",
        "human-in-the-loop",
        "lithium carbonate",
        "crystallization",
        "optimization",
        "machine learning",
        "gaussian process",
        "materials science",
        "chemical engineering",
    ],
    project_urls={
        "Bug Reports": "https://github.com/shmouses/HITL_Adaptive_Active_Learning_Lithium/issues",
        "Source": "https://github.com/shmouses/HITL_Adaptive_Active_Learning_Lithium",
        "Documentation": "https://github.com/shmouses/HITL_Adaptive_Active_Learning_Lithium/docs",
        "Paper": "",
    },
) 