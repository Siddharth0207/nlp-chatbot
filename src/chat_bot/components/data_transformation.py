from src.chat_bot.logger import logging
from src.chat_bot.exception import CustomException

import whisper
import os
import sys


class WhisperModel:
    def __init__(self, model_name: str = "small"):
        self.model_name = model_name
        self.model = self.__load_model(model_name)

    
    def __load_model(self, model_name):
        try:
            logging.info(f"Loading Model Initiated")
            model = whisper.load_model(model_name)
            return model
        except Exception as e:
            raise CustomException(e, sys)

    def transcribe_audio(self, audio_path):
        try:
            logging.info(f"Transcribing Audio Initiated")
            result = self.model.transcribe(audio_path)
            return result
        except Exception as e:
            raise CustomException(e, sys) 

