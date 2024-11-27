"""
This file contains all the imports for the project
"""

#general imports
import os
from typing import Any

#data structures
from queue import Queue

#threading imports
import time #to help handle the threads
from threading import Thread, Lock

#speech to text and back
import speech_recognition as sr
from yapper import Yapper, PiperSpeaker, PiperQuality, PiperVoice, DefaultEnhancer, Persona

#openai chatbot
import openai