import os
import re


def remove(s):
    return s[:s.rfind('\n')]


master = open('master.tex', mode='w')
print(os.listdir())
for d in os.listdir():
    try:
        s_master=open(d+'/master.tex')
        cont = s_master.read()
        #print(re.findall(r"\\begin\{document\}", cont))
        parsed = re.split(r'\\begin\{document\}', cont)[1]
        #parsed = re.split(r'\\end\{document\}', parsed)[0]
        print(parsed)
        parsed="\\begin{document}\n"+parsed
        parsed_master =open(d+'/parsed_master.tex', mode='w')
        parsed_master.write(parsed)
        parsed_master.close()
        s_master.close()
    except Exception as e:
        print(e)

master.close()

master = open('master.tex', mode='r')
print(master.read())



