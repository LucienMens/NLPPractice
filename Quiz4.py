# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:04:42 2020

@author: Christiana
"""
import os
import shutil
from os import path
from requests import get
from textract import process
from chardet import detect
from pypandoc import convert_text
from os import remove

'''as of right now, textract doesn't work on my computer, so I cannot test the epub and pdf versions. it'll probably be broken :/ '''
def textExtract():
    url = input("Enter url: ") 
    name = input("Enter name: ")
    exten = input("Enter extention: ")
#a tuple that will be iterated over
#filetype = [txt,epub,pdf]
    soonFile = [url,name,exten]
    for val in soonFile:
        if exten == 'txt':
            response = get(url)
            print(f'{response.headers}')
            rawText = response.text
#this takes the user information and saves it to the file
            with open(name+'.'+exten,'w',encoding="utf-8") as textWrapper:
                textWrapper.write(rawText)
                print("Nice. It's a txt file.")
#this should take a pdf file and save it. currently not working because textract is not working
        elif exten == 'pdf':
            response = get(url)
            response.content[:150]
            fileName = name+'.'+exten
            with open(name+'.'+exten, 'wb') as textWrapper:
                textWrapper.write(response.content)
                byteText = process(fileName)
                type(byteText)
                byteText[:150]
                detected = detect(byteText)
                encoding = detected['encoding']
                text = byteText.decode(encoding)
                file = fileName.replace('pdf', 'txt')
                with open(file, 'w') as textWrapper:
                    textWrapper.write(text)
                remove(name+'.'+'pdf')
                print("Yay! Pdf to txt file!")
#textract doesn't want to work here either....
        elif exten == 'epub':
            response = get(url)
            response.content[:150]
            fileName = name+'.'+exten
            with open(name+'.'+exten, 'wb') as textWrapper:
                textWrapper.write(response.content)
                byteText = process(fileName)
                type(byteText)
                byteText[:150]
                detected = detect(byteText)
                encoding = detected['encoding']
                text = byteText.decode(encoding)
                file = fileName.replace('pdf', 'txt')
                with open(file, 'w') as textWrapper:
                    textWrapper.write(text)
                remove(name+'.'+'epub')
                print("Success! Epub to txt file!")
                return
textExtract()