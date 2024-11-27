from imports import *

# lessac = PiperSpeaker(
#     voice=PiperVoice.LESSAC,
#     quality=PiperQuality.HIGH
# )

# lessac.say("Hello world, its a beautiful day today")
yapper = Yapper(
    enhancer=DefaultEnhancer(persona=Persona.JARVIS))
yapper.yap("Good morning Mr Stark, what will you invent today")