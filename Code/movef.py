#!barb/bin/python3.11
import shutil

import Code

rf = Code.readext.readfolder()

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

        except:

            with open("shelf.txt", "w"):

                pass

            self.checkdefs()

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


    def mv(self, target, destination):

        shutil.move(target, destination)


if __name__ == "__main__":

    ch = change()

    ch.checkdefs()
