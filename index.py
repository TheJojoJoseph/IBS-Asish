import gtts

# make request to google to get synthesis
tts = gtts.gTTS("Asish is awesome")

# save the audio file
tts.save("hello.mp3")


