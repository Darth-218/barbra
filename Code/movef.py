#!barb/bin/python3.11
import os
import shutil


class change:

    def checkdefs(self) -> None:

        try:

            with open("shelf.txt", "r") as settings:

                if not len(settings.readlines()):

                    with open("shelf.txt", "w") as settings:

                        settings.writelines(["0\n", "0\n", "0\n", "0\n"])

            self.writedefs()

        except:

            with open("shelf.txt", "w"):

                pass

            self.checkdefs()

    def writedefs(self):

        with open("shelf.txt", "r") as settings:

            paths_ = ["Default", "Audio", "Video", "Documents"]

            editted_ = settings.readlines()

            for x in range(len(editted_)):

                if editted_[x].strip() == "0":

                    editted_[x] = input(f"Add a path for {paths_[x]}: ") + "\n"

            print("Those are the new paths", editted_)

            with open("shelf.txt", "w") as settings:

                settings.writelines(editted_)


    def mv(self, target, destination):

        shutil.move(target, destination)


if __name__ == "__main__":

    ch = change()

    ch.checkdefs()
