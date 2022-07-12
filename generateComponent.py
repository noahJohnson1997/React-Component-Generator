import os
# path = input("Please enter the full path to your component: ")
print("1: JavaScript \n2: TypeScript")
projectType = input("Is this a JavaScript or TypeScript project?...")
if projectType == '1':
    testExt = '.js'
    ext = '.js'
elif projectType == '2':
    testExt = '.ts'
    ext = '.tsx'

print("1: Component \n2: Page")
selectType = input("Component or Page?... ")
if selectType == '1':
    folderType = 'Component'
elif selectType == '2':
    folderType = 'Page'
else:
    print("INVALID INPUT")
    exit()
path = os.path.dirname(os.path.abspath(__file__)) + "/src/"+folderType+"s/"
comName = input(folderType + " Name: ")

if path[-1] != "/":
    path = path + "/"
if comName[0] == "/":
    comName = comName.replace("/", "")

os.mkdir(path + comName)
projectFile = open(path+comName+'/'+comName+ext, 'w')
componentTemplate = """
//"""+comName+"""
import React from "react";

export default function """+comName+"""() {
    return(
        <div></div>
    )
}
"""
projectFile.write(componentTemplate)
projectFile.close

scssFile = open(path+comName+'/'+comName+'.scss', 'x')
scssFile.close

testFile = open(path+comName+'/'+comName+'.test'+testExt, 'x')
testFile.close