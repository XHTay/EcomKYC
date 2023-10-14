import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "ECommerceKYC"

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebooks/EDA.ipynb",
    "artifacts/raw" # Delete raw later  
]

for filepath in list_of_file:
    filepath = Path(filepath) # Detects the OS and converts the string into the filepath in the os version, eg Windows("path")
    filedir, filename = os.path.split(filepath) # Splits directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If file already contains code, size will > 0
        with open(filepath, "w") as f:
            pass # Just creating the file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists.")

