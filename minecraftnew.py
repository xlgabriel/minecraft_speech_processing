from threading import Thread
from cv2 import line
from pygments import highlight
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import librosa
import speech_recognition as sr
import matplotlib.pyplot as plt
import cv2
import keras
import h5py
import numpy as np

# Variables---------------------

grass_texture = 'assets/grass_block.png'
stone_texture = 'assets/stone_block.png'
brick_texture = 'assets/brick_block.png'
dirt_texture  = 'assets/dirt_block.png'
sky_texture   = 'assets/skybox.png'
sky_texture   = 'assets/skybox.png'
arm_texture   = 'assets/arm_texture.png'
palabras_texture = 'assets/palabras.png'

IDtextura = 0
Scale = 0.5
Model = 'assets/block'
Color = color.rgb(255, 255, 255)
texturas = [grass_texture,stone_texture,brick_texture,dirt_texture,brick_texture]

# Predictor---------------------

def predictor():
    
    def espectro(audio):
        wav_data = sr.AudioData.get_wav_data(audio)
        with open("audio.wav","wb")as f:
            f.write(wav_data)
        x,Fs = librosa.load('audio.wav',mono=True,sr=16000)
        plt.specgram(x,NFFT=512,Fs=Fs,Fc=0,noverlap=64,cmap=plt.cm.jet,scale='dB')
        plt.axis('off')
        plt.savefig('spec.png')

    def predictor(img):
        imag = cv2.imread(img)
        imag = cv2.resize(imag, (150,150))
        prediction = model.predict(imag.reshape(1,150,150,3))
        return prediction


    model = keras.models.load_model('modeloCNNDef.h5')
    etiquetas =["Blanco","Naranja","Octavo","Siete","Viernes"]
    r = sr.Recognizer()
    r.dynamic_energy_treshold = False
    r.energy_treshhold = 300


    def listener():
        global IDtextura 
        global Scale 
        global Model
        global Color
        try:
            with sr.Microphone () as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("\nEscuchando")
                audio = r.listen(source,phrase_time_limit = 2)
                print("Google analizando")
                text = r.recognize_google(audio,language='es-MX')
                if text == 'blanco' or text == 'naranja' or text == 'octavo' or text == 'viernes' or text == 'siete' or text == '7':
                    print("\nUsted dijo: {}".format(text))        
                    espectro(audio)
                    resultado = predictor('spec.png')
                    #print("Nuestro predictor: {}".format(etiquetas[(np.argmax(resultado))]))
                    
                    if text == 'blanco':
                        IDtextura = 0
                        Color = color.rgb(255,255,255)
                        print("Nuestro predictor: {}".format(etiquetas[0]))
                    if text == 'naranja':
                        IDtextura = 1
                        Color = color.rgb(255,255,255)
                        print("Nuestro predictor: {}".format(etiquetas[1]))
                    if text == 'octavo':
                        IDtextura = 2
                        Color = color.rgb(255,255,255)
                        print("Nuestro predictor: {}".format(etiquetas[2]))
                    if text == '7':
                        IDtextura = 3
                        Color = color.rgb(255,255,255)
                        print("Nuestro predictor: {}".format(etiquetas[3]))
                    if text== 'viernes':
                        IDtextura = 4
                        Color = color.rgb(150,150,150)
                        print("Nuestro predictor: {}".format(etiquetas[4]))
                else:
                    listener()
                
        except:
            print("volviendo a escuchar... espere un momento")
            listener()
        
        listener()

    listener()


# Juego---------------------

app = Ursina(position=(200, -5))

def update():
    
	if held_keys['left mouse'] or held_keys['right mouse']:

		hand.active()
		
	else:
		hand.passive()
	
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = Model,
            origin_y =0.5,
            texture = texturas[IDtextura],
            color = Color,
            scale = Scale,
            highlight_color = color.lime
            )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                    voxel = Voxel(position = self.position + mouse.normal)
            
            if key == "right mouse down":
                    destroy(self)
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True)
            
class Hand(Entity):
    def __init__(self):
            super().__init__(
                    parent = camera.ui,
                    model = Model,
                    texture = texturas[IDtextura],
                    scale = Scale * 0.4,
                    color = Color,
                    rotation = Vec3(-10,-10,0),
                    position = Vec2(0.4,-0.6))

    def active(self):
	    self.position = Vec2(0.3,-0.5)
	    self.texture = texturas[IDtextura]
	    self.color = Color

    def passive(self):
	    self.position = Vec2(0.4,-0.6)
	    self.texture = texturas[IDtextura]
	    self.color = Color
            

class UI(Entity):
    def __init__(self):
            super().__init__(
                    parent = camera.ui,
                    model = 'cube',
                    texture = palabras_texture,
                    scale = 0.2,
                    color = Color,
                    rotation = Vec3(0,0,0),
                    position = Vec2(-0.75,0.38))
    
chunkSize = 20

for z in range(chunkSize):
    for x in range (chunkSize):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()
ui = UI()



if __name__ == "__main__":
    Play1 = Thread(target=predictor).start()
    app.run()


