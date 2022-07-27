import os
from zipfile import ZipFile

dir_name = os.chdir("/media/suman/649EF25A9EF223E8/NodeJS - The Complete Guide (MVC, REST APIs, GraphQL, Deno) Updated 8-2021/02 Optional_ JavaScript - A Quick Refresher[TutFlix.ORG]/")
# list_dir = os.listdir()
# print(list_dir)

for file in os.listdir(dir_name):
    if file.endswith(".zip"):
    #     ZipFile.extract(file)
        file_name = os.path.abspath(file)
        zip_ref = ZipFile(file_name)
        zip_ref.extractall(dir_name)
        zip_ref.close()
        os.remove(file_name)
        print(file)

    # print(file)

