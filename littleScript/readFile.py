# -*- coding:utf-8 -*-
import os
def read_file(file_path):
    content = []
    try:
        print os.path.isfile(file_path)
        file = open(file_path)
        content = file.readlines()
        print content
    except exception:
        print "exception"
        content = str(exception)
    finally:
        file.close()
        return content

def process_line(line):
    print "processing"
    params = line.split("|")
    result_str = "insert into hsc_global_config(" + "a" +")" + "values("
    for i in range(0,len(params)):
        result_str += params[i]
        if i <> len(params)-1:
            result_str += ","
        else:
            result_str += ");"
    return result_str

#def write_file(des_path,des_content):
 #   for line in des_content:


if __name__ == "__main__":
    #print os.listdir("~/Desktop/LearningNote/litte")
    src_content = read_file("/Users/flywhite/Desktop/LearningNote/littleScript/src.txt")
    des_content = []
    for line in src_content:
        str = process_line(line)
        des_content.append(str)
    print des_content

    #writeFile(des_content)
