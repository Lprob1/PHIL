from imports import *

#below: formats for inputs
class Audio:
    accepted_formats = ["wav", "mp3"]
    format: str
    audio_content: Any
    def __init__(self, format, audio_content):
        if format in Audio.accepted_formats:
            self.format = format
            self.content = audio_content
        else:
            print(f'format {format} is not supported\n')
            return
        

class Text:
    text_content: str
    def __init__(self, text_content):
        self.content = text_content

#below: types of things that can be added to a ready queue
class Input:
    """A class to descript an input for the AI to process"""
    def __init__(self, type: Audio | Text, content: Any):
        self.type = type
        self.content = content

class Command:
    """A class to describe the commands for the system to run"""
    def __init__(self, content: str):
        self.command: str = content
    
    def run(self):
        os.system(self.command)

class Output:
    """A class to describe the outputs of the system. Possible types:
        - write to terminal
        - voice"""
    out_type: Text | Audio
    content: Any
    def __init__(self, out_type, content):
        self.out_type = out_type
        self.content = content

