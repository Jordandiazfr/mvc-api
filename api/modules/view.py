# ---- View -----
class View:
    def __init__(self) -> None:
        self.user_input = ""

    def get_input(self):
        self.user_input = input("Please write something... ")
        if self.user_input == "":
            return 0
        return self.user_input

    def show_file_content(self):
        f = open("output.txt", "r")
        lines = f.readlines()
        print(" ## --- output.txt ---- ## ")
        for line in lines:
            print(line.strip())