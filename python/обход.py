import os 

path =  'C:\\art'

def tree(path, level=1):
    print('Level=',level,'Content', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('\t'+ path)
            tree(path+'\\'+i, level+1)
            print('Возвращаемся в', path)
tree(path)