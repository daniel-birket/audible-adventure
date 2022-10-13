breakpoint()
#: import necessary libraries
try:
    from sdl2 import *
    from sdl2.ext import Resources
    from sdl2.ext.compat import byteify
    from sdl2.sdlmixer import *
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Access the resources in SDL2
# RESOURCES = Resources(__file__, "assets")
#initialises the audio system.
if SDL_Init(SDL_INIT_AUDIO) != 0:
    raise RuntimeError("Cannot initialize audio system: {}".format(SDL_GetError()))
#Initialises the mixer API.
Mix_OpenAudio(44100, AUDIO_S16SYS, 2, 1024)
audiocheck=Mix_OpenAudio(44100, AUDIO_S16SYS, 2, 1024)
if audiocheck != 0:
    raise RuntimeError("Cannot open mixed audio: {}".format(Mix_GetError()))
    #Assigns a file to the variable sound_file.
sound_file ="/home/lawrence/Downloads/computer-keyboard-1.wav"
#Loads the wave file as a chunk into memmory, so the mixer can use it.
sample = Mix_LoadWAV(byteify(sound_file, "utf-8"))
#Checks if there is audio loaded into memmory.
if sample is None:
    raise RuntimeError("Cannot open audio file: {}".format(Mix_GetError()))
#Plays the loaded audio file on the first available channel.
channel = Mix_PlayChannel(-1, sample, 0)
#If there is an error playing the file, then print an error message.
if channel == -1:
    raise RuntimeError("Cannot play sample: {}".format(Mix_GetError()))
#While the audio file is playing, then wait for 100 MS, then close the file.
while Mix_Playing(channel):
    SDL_Delay(100)
#Closes all audio channels and quits the audio system.
Mix_CloseAudio()
SDL_Quit(SDL_INIT_AUDIO)
