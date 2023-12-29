class Fish():
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def swim(self):
        print("泳いでいる")

    # デストラクタ
    def __del__(self):
        print("破棄されました。")

fish = Fish("red", "tiechui")
print(fish.color, fish.name)