import os

path = '/Users/ll/21世纪中国小说/'
# file = os.listdir(path)
# for f in file:
#     os.rename(path+f,path+f[1:])

Filelist = []
for home, dirs, files in os.walk(path):
    # print(home)
    
    for filename in files:
        # 文件名列表，包含完整路径
        Filelist.append(os.path.join(home, filename))
        # # 文件名列表，只包含文件名
        newfilename = filename.replace('?','').replace('|','').replace('"','“').replace(':','：').replace('丨','').replace('｜','')
        os.rename(os.path.join(home, filename),os.path.join(home, newfilename))
        # Filelist.append(filename)
        print(newfilename)