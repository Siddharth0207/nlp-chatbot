import numpy as np
import pandas as pd
import sys
import os 
from src.chat_bot.logger import logging
from src.chat_bot.exception import CustomException


from datasets import load_dataset
from typing import List, Dict, Any
import kagglehub
from kagglehub import KaggleDatasetAdapter
import zipfile
import whisper



