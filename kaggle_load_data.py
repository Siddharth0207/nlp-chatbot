import os
import zipfile
import pandas as pd
import kaggle
from src.chat_bot.logger import logging


def load_dataset():

    """
    This function download dataetfrom kaggle and extract.
    This requires your kaggle.json file to be in the ~/.kaggle directory.
    
    """
    file_path = r"C:\Users\DNK109\Documents\Sid\nlp-chatbot\raw_data"
    zip_file = os.path.join(file_path, "flipkart-laptop-reviews.zip")
    csv_path = os.path.join(file_path, "laptops_dataset_final_600.csv")

    # Download if not already present
    if not os.path.exists(zip_file):
        logging.info("Downloading dataset from Kaggle...")
        kaggle.api.dataset_download_files("gitadityamaddali/flipkart-laptop-reviews", path=file_path, unzip=False)
        logging.info(f"Downloaded to {file_path}")

    # Extract if CSV doesn't exist
    if not os.path.exists(csv_path):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(file_path)
        logging.info(f"Extracted files to {file_path}")

    # Load the CSV
    df = pd.read_csv(csv_path)
    logging.info("Dataset loaded successfully:")
    return df

if __name__ == "__main__":
    load_dataset()