import sys
import xmltodict
from gzip import GzipFile
from os import mkdir, rmdir
from shutil import rmtree
import json
import os

# sourceFile = str(sys.argv[2])
itemType = str(sys.argv[1])
index = 0
group = 0
chunkSize = 10000
fileName = itemType + '/' + itemType + str(group) + '.json'
file = None

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv[1]))


def create_dir():
    print("create_dir")
    global itemType
    if os.path.isdir(itemType):
        rmtree(itemType)
    mkdir(itemType)


def create_file_name():
    print("create_file_name")
    global chunkSize
    global fileName
    global group
    fileName = itemType + '/' + itemType + str(group) + '.json'
    group = group + chunkSize


def create_file():
    print("create_file")
    global file
    global fileName
    if (file):
        # file.write('\n')
        file.close()
    create_file_name()
    file = open(fileName, 'a')


def make_header_row(index):
    return json.dumps({"index": {"_index": itemType, "_type": "_doc", "_id": str(index)}})


def writeFile(index, data):
    global itemType
    global fileName
    global chunkSize
    global group
    global file
    # print('write file', index, group)
    if (index == group):
        create_file()
    dcdata = json.dumps(data) + "\n"
    file.write(make_header_row(data['id']) + "\n")
    file.write(dcdata.replace('@', ''))


def handle_row(_, row):
    global index
    group = index % chunkSize
    writeFile(index, row)
    index = index+1
    return True


create_dir()
# create_file_name()
# create_file()
xmltodict.parse(GzipFile('./source/'+itemType+'.xml.gz'),
                item_depth=2, item_callback=handle_row)
print("parsing done")
