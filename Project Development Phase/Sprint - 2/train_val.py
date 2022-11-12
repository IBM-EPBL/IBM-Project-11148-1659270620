#pip install split-folders

import os
import splitfolders

dataset = 'E:/IBM/Code/ActionDetectionforSignLanguage/Test/dataset/'
model = 'E:/IBM/Code/ActionDetectionforSignLanguage/Test/training/'
root = 'E:/IBM/Code/ActionDetectionforSignLanguage/Test/'

def main():
    files = os.listdir(dataset)
    for fname in files:
        splitfolders.ratio(dataset+fname+'/',output=root,seed=1337, ratio=(.8, .2), group_prefix=None, move=False)
        cmd = 'mkdir E:\IBM\Code\ActionDetectionforSignLanguage\Test\training\train\\'+fname
        os.system(cmd)
        path = root+'train/'
        train_files = os.listdir(path)
        for train_file in train_files:
            shutil.move(root+'train/',model+'train/fname/')
        os.rmdir(root+'train')
        cmd = 'mkdir E:\IBM\Code\ActionDetectionforSignLanguage\Test\training\val\\'+fname
        os.system(cmd)
        path = root+'val/'
        val_files = os.listdir(path)
        for val_file in val_files:
            shutil.move(root+'val/',model+'val/fname/')
        os.rmdir(root+'val')

if __name__ == "__main__":
    main()