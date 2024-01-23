#!barb/bin/python3.11
import os


class readfolder:

    def __init__(self, default, audio, video, doc) -> None:

        self.default, self.audio, self.video, self.doc = default, audio, video, doc
        self.defs = [self.default, self.audio, self.video, self.doc]

    def conf(self) -> None:

        if not os.path.isfile("shelf.txt"):

            with open("shelf.txt", "w") as settings:

                settings.writelines(self.defs)

    def checkifdir(self, dirpath: str) -> bool:

        return os.path.isdir(dirpath)

    def prepfiles(self) -> None:

        for x in self.default:

            match x.split(".")[-1]:

                case ".mp3" | ".wav":

                    print("This is audio and goes in:", self.audio)


if __name__ == "__main__":

    pass
