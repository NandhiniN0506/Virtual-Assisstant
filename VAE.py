#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install openai


# In[4]:


get_ipython().system('pip install pyttsx3')


# In[5]:


pip install SpeechRecognition


# In[16]:


pip install pyaudio


# In[4]:


import openai
import speech_recognition as sr
import pyttsx3


# In[5]:


openai.api_key = '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'
engine = pyttsx3.init()


# In[6]:


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Unknown Error")
        


# In[7]:


def generate_response(prompt):
    response = openai.Completion.create(
    engine = "",
    prompt = prompt,
    max_taken = 4000,
    n = 1,
    stop = None,
    temperature = 0.5)
    return response["Choices"][0]["text"]


# In[9]:


def speak_text(text):
    engine.say(text)
    engine.RunAndWait()


# In[10]:


def main():
    while True:
        print('Say Hello to start your conversation')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower == "hello":
                    filename = "input.wav"
                    print('Say your Query')
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.path_threshold = 1
                        audio = recognizer.listen(source)
                        with open(filename,'wb') as f:
                            f.write(audio.get_wav_data())
                    
                    text = transcibe_audio_to_text(filename)
                    if text:
                        print(f'You said {text}')
                        response = generate_response(text)
                        print(response)
                        speak_text(response)
            except Exception as e:
                print(f"An Error occured : {e}")
                
                            


# In[11]:


main()

