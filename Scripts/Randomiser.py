import os
import pygame as pg
import random


class MusicPlayer:
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self._pause = False

        username = os.environ.get('USERNAME')
        base_folder = "C:\\Users\\" + username + "\\Music\\"
        print('Hi, ' + username, end='\n\n')

        self._musicList = [os.path.join(base_folder, f) for f in os.listdir(base_folder)
                           if f.endswith(('.mp3', '.ogg', '.wav'))]
        random.shuffle(self._musicList)

        self._index = -1

        self._currentMusicPath = None

        self.Play()

    def Play(self):
        self._index += 1
        try:
            self._currentMusicPath = self._musicList[self._index]
        except IndexError:
            random.shuffle(self._musicList)
            self._index = 0
            self._currentMusicPath = self._musicList[0]

        pg.mixer.music.load(self._currentMusicPath)
        pg.mixer.music.play()

    def PlayNext(self):
        pg.mixer.music.stop()

        if self._pause:
            self.Pause()

        self.Play()

    def Pause(self):
        if not self._pause:
            pg.mixer.music.pause()
        else:
            pg.mixer.music.unpause()

        self._pause = not self._pause

    def Update(self):
        if not pg.mixer.music.get_busy() and not self._pause:
            self.Play()

    def GetMusicName(self):
        return self._currentMusicPath.split('\\')[len(self._currentMusicPath.split('\\')) - 1]

    def SetVolume(self, volume: float):
        if volume > 100:
            volume = 100
        elif volume < 0:
            volume = 1

        pg.mixer.music.set_volume(volume / 100)

    def GetVolume(self):
        return pg.mixer.music.get_volume() * 100
