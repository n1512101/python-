import os

list1 = ["dirA", "dirB", "dirC", "file.py"]

path = os.path.join(*list1)

print(path)