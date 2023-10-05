import gtts

# make request to google to get synthesis
tts = gtts.gTTS("Hello world")

# save the audio file
tts.save("hello.mp3")


