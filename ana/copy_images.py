import os
import shutil


for dire in os.listdir():
    try:
        path='./'+dire+'/figures'
        for f in os.listdir(path):
            if(f[-7:]=='pdf_tex'):
                original = r'./'+dire+'/figures/'+f
                target = r'./figures/'+f
                shutil.copyfile(original, target)
                print("COPIATO")
            elif(f[-3:]=='pdf'):
                original = r'./'+dire+'/figures/'+f
                target = r'./figures/'+f
                shutil.copyfile(original, target)
                print("COPIATO")
    except:
        print('Not a directory')
