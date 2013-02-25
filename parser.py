import pefile
import os
import time

def dir_list2(dir_name, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if len(args) == 0:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
    return fileList
 
def sectionName (f):
    unknown = 0
    unknownName = 0
    normalName = 0
    pe = pefile.PE(f, fast_load=True)
    for section in pe.sections:
        name = section.Name
        if "text" in name:
            normalName = normalName + 1
        elif "bss" in name:
            normalName = normalName + 1
        elif "data" in name:
            normalName = normalName + 1
        elif "rsrc" in name:
            normalName = normalName + 1
        elif "debug" in name:
            normalName = normalName + 1
        elif "reloc" in name:
            normalName = normalName + 1
        elif "winzip" in name:
            normalName = normalName + 1
        elif "tls" in name:
            normalName = normalName + 1
        elif "UPX" in name:
            normalName = normalName + 1
        elif "boom" in name:
            normalName = normalName + 1
        elif "seau" in name:
            normalName = normalName + 1
        elif "code" in name:
            normalName = normalName + 1
        elif "Shared" in name:
            normalName = normalName + 1
        elif "gentee" in name:
            normalName = normalName + 1
        elif "CODE" in name:
            normalName = normalName + 1
        elif "DATA" in name:
            normalName = normalName + 1
        elif "BSS" in name:
            normalName = normalName + 1
        elif "CRT" in name:
            normalName = normalName + 1
        elif "PAGE" in name:
            normalName = normalName + 1
        elif "INIT" in name:
            normalName = normalName + 1
        elif "res" in name:
            normalName = normalName + 1
        elif "asp" in name:
            normalName = normalName + 1
        elif "tsu" in name:
            normalName = normalName + 1
        elif "TEXT" in name:
            normalName = normalName + 1
        else:
            print "Unknown Name: ", name
            unknownName = unknownName + 1    
    if unknownName > 0:        
        unknown = 1
        print f
        print ""    
    return unknown
    

if __name__ == '__main__':

    number = 0
    fileList = dir_list2('/Users/tigerlyb/Documents/CSCI8260Project/normal/')
    for f in fileList:
        if f != '/Users/tigerlyb/Documents/CSCI8260Project/normal/.DS_Store':
            if sectionName (f) == 1:
                number = number + 1
    print "Number of Files Containing Unknown Names: ", number
    
    #print pe.dump_info()
