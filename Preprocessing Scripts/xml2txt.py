import os
import xml.etree.ElementTree as ET
import string
str1=""
str2=""
xmin=""
ymin=""
xmax=""
yamx=""
final=""
path = "/home/amrit/Desktop/Nymble/detector/labels/val_xml/"
for files in os.listdir(path):
    na=path+files
    tree=ET.parse(na)
    root=tree.getroot()
    for elem in root:
        if elem.tag=="filename":
            str1=elem.text
        if elem.tag=="object":
            for elem2 in elem:
                if elem2.tag=="name":
                    str3=elem2.text
                    print str3
                if elem2.tag=="bndbox":
                    for elem3 in elem2:
                        if elem3.tag=="xmin":
                            xmin=elem3.text
                        if elem3.tag=="ymin":
                            ymin=elem3.text
                        if elem3.tag=="xmax":
                            xmax=elem3.text
                        if elem3.tag=="ymax":
                            ymax=elem3.text    
            str2=files.replace(".xml",".txt")
            final=str1+" "+str3+" "+xmin+" "+ymin+" "+xmax+" "+ymax
            f=open(str2,"w+")
            f.write(final)
            f.close() 
    str1="" 
    str2="" 
    xmin=""
    ymin=""
    xmax=""
    yamx=""
    final=""       
