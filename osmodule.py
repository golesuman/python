import os
os.chdir('/media/suman/649EF25A9EF223E8/OOP/')
print(os.getcwd()) #get the currrent directory

print(os.listdir()) #get the list of directories 
print(os.listdir())
os.rename('Psychopath','Psycopath1') # rename the file name

print(os.listdir())
os.makedirs('PyschoSuman/SumanGole') #make directories 
os.removedirs('PyschoSuman/SumanGole') #remove the directories
for dirpath,dirnames,filenames in os.walk('/media/suman/649EF25A9EF223E8'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()