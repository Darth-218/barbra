#!barb/bin/python3.11
from pathlib import Path
import os
import movef

mf = movef.change()

class readfolder:

    def __init__(self) -> None:

        try:

            with open("shelf.txt", "r") as settings:

                    self.paths = settings.readlines()

        except:

            mf.freshconfig()

        self.default = self.paths[0].strip()
        self.audio = self.paths[1].strip()
        self.video = self.paths[2].strip()
        self.docs = self.paths[3].strip()
        self.other = self.paths[4].strip()

    def checkifdir(self, dirpath: str) -> bool:

        return Path(dirpath).is_dir()

    def prepfiles(self) -> None:

        for x in os.listdir(self.default):

            match x.split(".")[-1]:

                case "mp3" | "wav":

                    print(x, "is an audio and goes in:", self.audio)

                case "mp4":

                    print(x, "is a video and goes in:", self.video)

                case "pdf" | "docx":

                    print(x, "is a document and goes in:", self.docs)

                case _:

                    print(x, "is something and goes in:", self.other)
