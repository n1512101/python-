class CPU():
    pass
class Disk():
    pass

class Computer():
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk
        

cpu = CPU()
disk = Disk()

com = Computer(cpu, disk)
com1 = com
print(com, com.cpu, com.disk)
print(com1, com1.cpu, com1.disk)

print('-'*30)
# 浅いコピー
import copy 
com2 = copy.copy(com)
print(com,com.cpu,com.disk)
print(com2, com2.cpu, com2.disk)

print('-'*30)
# 深いコピー
com3 = copy.deepcopy(com)
print(com,com.cpu,com.disk)
print(com3, com3.cpu, com3.disk)
