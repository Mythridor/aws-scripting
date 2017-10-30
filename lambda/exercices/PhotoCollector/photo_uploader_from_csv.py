#! /usr/local/bin/Python3.5

import urllib.request

with open("images.csv", 'r') as csv:
    i = 0
    for line in csv:
        line = line.split(',')
        if line[1] != '' and line[1] != "\n":
            urllib.request.urlretrieve(line[1].encode('utf-8'), ("img_" + str(i) + ".jpg").encode('utf-8'))
            print("Image saved".encode('utf-8'))
        i += 1

print("No result")
