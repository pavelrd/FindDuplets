# -*- coding: utf-8 -*-
import re

inputFilename  = "inputfile.txt" # Имя входного файла с текстом
outputFilename = "outputfile.txt" # Имя выходного файла с текстом

excludeSymbols = "Ё"             # Буквы, которые нужно исключить

# Чтение файла и запись его содержимого в виде строки в переменную inputString

inputFile = open( inputFilename, mode="r", encoding="utf-8" )

inputString = inputFile.read()

inputFile.close()

# Формирование строки outputString содержащей все символы, кроме тех которые в excludeSymbols

outputString = ""

for symbol in inputString:
    if not ( symbol in excludeSymbols ):
        outputString += symbol

# Запись в выходной файл текста, за исключением букв в excludeSymbols

outputFile = open( outputFilename, "w" )

outputFile.write(outputString)

outputFile.close()

# Далее идет поиск триплетов и дуплетов и вывод из позиций на экран

# Поиск триплетов, последовательностей из трех символов, которые встречаются более одного раза

triplets = []

for i in range(len(outputString)-3):

    buf = ""
    buf += outputString[i]
    buf += outputString[i+1]
    buf += outputString[i+2]
        
    if( ( len( re.findall( buf, outputString[i+2:] ) ) > 0 ) and ( not buf in triplets ) ):
        triplets.append( buf )

# Вывод на экран всех найденных триплетов

print("Найденные триплеты:")

for triplet in triplets:
    print(triplet)

# Поиск дуплетов, включая дуплеты входящие в состав триплетов

print("Найденные дуплеты, включая дуплеты входящие в состав триплетов:")

duplets = []

for i in range(len(outputString)-2):

    buf = ""
    buf += outputString[i]
    buf += outputString[i+1]
        
    if( ( len( re.findall( buf, outputString[i+1:] ) ) > 0 ) and ( not buf in duplets ) ):
        duplets.append( buf )

# Вывод на экран всех найденных дуплетов

for duplet in duplets:
    print(duplet)

# Поиск начальных позиций дуплетов

print("Начальные позиции дуплетов:")

for duplet in duplets:
    i = 0
    print( duplet, " : ", end=" ")
    while True:
        i = outputString.find(duplet, i)
        if i < 0:
            break
        print(i, end = " ")
        i += 3
    print("") # Печать перевода строки

# Поиск начальных позиций триплетов

print("Начальные позиции триплетов:")

for triplet in triplets:
    i = 0
    print( triplet, " : ", end=" ")
    while True:
        i = outputString.find(triplet, i)
        if i < 0:
            break
        print(i, end = " ")
        i += 3
    print("") # Печать перевода строки