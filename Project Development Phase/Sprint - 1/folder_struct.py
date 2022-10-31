import os

folder = "E:/dataset_creation/videos"
contents = os.listdir(folder)
for content in contents:
    path = folder+'/'+content
    files = os.listdir(path)
    for filename in files:
        dst = f"{filename}"
        res = ''.join([i for i in dst if not i.isdigit() if not i == '.' if not i == ' ']).lower()
        
        src =f"{folder}/{content}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{content}/{res}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
