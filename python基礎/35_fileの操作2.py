def my_write(s):
    file = open('b.txt', 'a', encoding='utf-8')
    file.write(s)
    file.write('\n')
    file.close()
    
def my_write_lst(file, lst):
    f = open(file, 'a', encoding='utf-8')
    f.writelines(lst)
    f.close()
    
def my_read(filename):
    file=open(filename, 'w+', encoding='utf-8')
    file.write('hello')
    file.seek(0)
    # s=file.read()
    # s=file.read(2)
    # s=file.readline()
    # s=file.readline(2)
    s=file.readlines()
    print(type(s), s)
    file.close()
    
if __name__ == '__main__':
    # my_write('helloworld')
    # my_write('welcomt to tokyo')
    # lst = ["name\t", 'age\t',"score\n","cmm\t","20\t","98"]
    # my_write_lst('c.txt', lst)
    my_read("d.txt")