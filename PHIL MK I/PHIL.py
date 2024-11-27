
from imports import *
from SpeechToText import SpeechToText
from OpenAIChatBot import OpenAIChatBot
from data_structures import *

class PHIL:
    def __init__(self):
        self.voice_input = SpeechToText()
        self.chat_bot = OpenAIChatBot()
        self.input_queue = Queue()
        self.commands_queue = Queue()
        self.text_output_queue = Queue()
        self.audio_output_queue = Queue()
        self.speak = True #by default, model speaks, but can be muted
        self.response_ready = Lock() # lock to have control of the terminal\
    
    def handle_text_input(self):
        while True:
            self.response_ready.acquire()
            user_input: str = input("You: ")
            self.input_queue.put(user_input)
    
    def handle_audio_input(self):
        voice_input = SpeechToText()
        r = voice_input.record()
        if r is not None:
            self.input_queue.put(r)

    def give_persona_to_response(self, response):
        return response

    def process_inputs(self):
        while True:
            if not self.input_queue.empty():
                #remove from queue
                content = self.input_queue.get()

                response = self.chat_bot.get_bot_response(content, self.chat_bot.pl)
                print(f'JARVIS: {response}') #print the response of Jarvis
                self.response_ready.release()


    def main_loop(self):
        """Main loop for Jarvis, always run"""
        text_thread = Thread(target=self.handle_text_input, daemon=True)
        audio_thread = Thread(target=self.handle_audio_input, daemon=True)
        process_thread = Thread(target=self.process_inputs, daemon=True)

        text_thread.start()
        audio_thread.start()
        process_thread.start()
        while True:
            time.sleep(0.5)
        

phil = PHIL()
phil.main_loop()
"""
    ideas:
    - take the input from text or voice
    - send it to GPT for a response
    - between saying something, send the input to an Intent analyser to figure out if a command needs to be executed
    - use yapper to say the response, and also export this response to audio
    - use speech to text to generate the text of the response
    - print both """

"""
NEXT STEPS
DONE 1. Ready queue of tasks to execute, if I write something and say something at the same time, or have multiple commands, to handle that
2. Voice to text, so I can speak to the model and it speaks back
DONE 3. Parallel processing, so that it can process while I talk to it
4. Intent recognition. Have a set of commands that can easily be expanded and then functions to be executed
5. Allow for chained commands, ie, I say do this and that and it parses into "this" and "that"
"""