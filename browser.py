
import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
 
# WILL NEED TO PUT THIS STUFF BACK IN FOR THE DIRECTORY STUFF TO WORK.
# # write your code here
# args = sys.argv
#
# # Create directory
# dirName = args[1]
#
# try:
#     # Create target Directory
#     os.mkdir(dirName)
# except FileExistsError:
#     print('')
 
dirName = "tb_tabs"
 
try:
    # Create target Directory
    os.mkdir(dirName)
except FileExistsError:
    print('')
 
 
def get_data(url):
    return requests.get('https://' + url).content
 
tags = ["a","p"]
 
def has_class_and_href(tag):
    return tag.has_attr('class') and tag.has_attr('href') and tag.get_text() != ("NoneType")
 
 
while True:
    address_bar = input()
    if address_bar == 'exit':
        break
    # elif address_bar.replace('.', '_') not in web_list:
    #     print("Error: Incorrect URL")
    elif '.' in address_bar:
        contents = BeautifulSoup(get_data(address_bar), 'html.parser')
        final_address = address_bar.replace('.', '')
        file_name = dirName + '/' + final_address + '.txt'
        with open(file_name, 'a+') as f:
            for x in range(len(contents.findAll('a'))):
                f.write(Fore.BLUE + contents.findAll('a')[x].get_text() + '\n')
                # print(contents.findAll('a')[x].get_text())
        with open(file_name, 'r') as d:
            print(d.read())
    else:
        print("Error: Incorrect URLs")
