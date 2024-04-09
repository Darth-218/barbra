import os
import shutil
from pathlib import Path


class change:
    def createdefs(self) -> None:
        with open("shelf.txt", "r") as settings:
            if len(settings.readlines()) != 5:
                self.freshconfig()

    def freshconfig(self) -> None:
        with open("shelf.txt", "w") as settings:
            settings.writelines(["0\n", "0\n", "0\n", "0\n", "0\n"])

    def checkdefs(self) -> None:
        if input("Create a new config? [y/n] ") == "y":
            self.freshconfig()

            try:
                self.createdefs()
                self.writedefs()

            except:  # noqa: E722
                with open("shelf.txt", "w"):
                    pass

                self.checkdefs()

        else:
            with open("shelf.txt", "r") as settings:
                rf.prepfiles(settings.readlines())

    def writedefs(self):
        with open("shelf.txt", "r") as settings:
            paths_ = ["Default", "Audio", "Video", "Documents", "Others"]

            editted_ = settings.readlines()

            for x in range(len(editted_)):
                if editted_[x].strip() == "0":
                    temp = input(f"Add a path for {paths_[x]}: ")

                    if rf.checkifdir(temp):
                        editted_[x] = temp + "\n"

                    elif temp == "q":
                        quit()

                    else:
                        print(temp, "is not a valid path")

                        self.writedefs()

            print("Those are the new paths", editted_)

            with open("shelf.txt", "w") as settings:
                settings.writelines(editted_)
                rf.prepfiles(editted_)

    def mv(self, target, destination):
        shutil.move(target, destination)


ch = change()


class readfolder:
    def checkifdir(self, dirpath: str) -> bool:
        return Path(dirpath).is_dir()

    def prepfiles(self, dirs) -> None:
        for x in os.listdir(dirs[0]):
            match x.split(".")[-1]:
                case "mp3" | "wav":
                    print(x, "is an audio and goes in:", dirs[1])

                case "mp4":
                    print(x, "is a video and goes in:", dirs[2])

                case "pdf" | "docx" | "txt":
                    print(x, "is a document and goes in:", dirs[3])

                case _:
                    print(x, "is something and goes in:", dirs[4])


rf = readfolder()

if __name__ == "__main__":
    ch.checkdefs()
