import pygame as pg
import os

pg.init()

font1 = pg.font.Font('assets/mainfont.ttf', 30)

class SOUND:
    def __init__(self, path_to_sound, path_to_photo):
        self.sound = pg.mixer.Sound('music/' + path_to_sound)
        self.photo = pg.image.load('assets/sound_images/' + path_to_photo)
        self.is_playing = True

    def placePhoto(self):
        self.photo = pg.transform.scale(self.photo, (300, 300))
        screen.blit(BACKGROUND, (0, 0))
        screen.blit(self.photo, (250, 120))
        screen.blit(self.sounds_n, (250, 437))

    def renderFont(self, sounds_name):
        self.sounds_n = font1.render(sounds_name, 1, (0, 0, 0))

path_to_sound = os.listdir('music/')
path_to_photo = os.listdir('assets/sound_images/')
sounds_names  = open('sounds.txt', 'r').read().split(',')
path_to_sound.sort()
path_to_photo.sort()

sounds = []

for i in zip(path_to_photo, path_to_sound):
    print(i)
    print(i[0])
    sound = SOUND(path_to_photo=i[0], path_to_sound=i[1])
    sounds.append(sound)
cnt = 0
for i in range(len(sounds_names)):
    sounds[i].renderFont(sounds_names[i])

screen = pg.display.set_mode((800, 600))

BACKGROUND = pg.image.load('assets/bg.png').convert()
screen.blit(BACKGROUND, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if pg.mouse.get_pressed()[0]:
            if 500 <= pg.mouse.get_pos()[1] <= 567 and 367 <= pg.mouse.get_pos()[0] <= 433:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 73 <= pg.mouse.get_pos()[0] <= 139 and 500 <= pg.mouse.get_pos()[1] <= 567:
                pg.mixer.stop()
                sound_index -= 1
                sounds[sound_index + 1].is_playing = True
                if(sound_index == -1):
                    sound_index = len(sounds) - 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto()
            elif 661 <= pg.mouse.get_pos()[0] <= 727 and 500 <= pg.mouse.get_pos()[1] <= 567:
                pg.mixer.stop()
                sound_index += 1
                sounds[sound_index - 1].is_playing = True
                if(sound_index == len(sounds)):
                    sound_index = 0
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto()
    pg.display.flip()