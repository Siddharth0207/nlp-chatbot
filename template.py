import os 
import sys 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
project_name = 'chat_bot'

file_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "Dockerfile.dev",
    "docker-compose.yaml",
    "config/config.yaml",
    "requirements.txt",
    "setup.py"


]

# {2}Writing the below code in order to avoid the situation when you have already made file with name 
for filepath in file_list:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory :{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f :
            pass
        logging.info(f"Creating Empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists.")