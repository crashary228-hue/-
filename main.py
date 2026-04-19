import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random

duration = 5
sample_rate = 44100
score = 0
errors = 0

#Уровни

words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}
#Выбор уровня

print('Приветствую вас в игре (Говори анг)')
print('Выбор уровня:easy, medium, hard')
level = input('').lower()



#Ошибка ввода уровня

while level not in words_by_level:
    print('ЛИбо вы напиали не правильно или такого уровня нет!')
    print('Выбор уровня:easy, medium, hard')
    level = input('').lower()

#Сортировка слов в уросне

words_list = words_by_level[level]
random.shuffle(words_list)

print('Вы выброли уровень', level.lower())
print('Вы увидите  слова на русском языке, а его надо произвести на английском языке, за 1 правильный ответ вы получите 1 балл,игра до 3 ошибок +_+')

#Слово которое надо назвать на английском

for word  in words_list:
    print('Слово', word)

    print("Говори...")
    recording = sd.rec(
    int(duration * sample_rate), # длительность записи в сэмплах
    samplerate=sample_rate,      # частота дискретизации
    channels=1,                  # 1 — это моно
    dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи

    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-En")
        print(f"Ты сказал: {text}")
        if text == translated:
            score = score + 1
            print('Плюс один балл')
        translator = Translator()
        translated = translator.translate(text, dest='en')  # здесь 'en' — это английский
        print("🌍 Перевод на английский:", translated.text)
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")