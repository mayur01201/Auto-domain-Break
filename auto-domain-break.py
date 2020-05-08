#!/usr/bin/python
import sys
import subprocess
import os

file_name = sys.argv[1]
file = open(file_name, 'r')
file_content = file.read()
list = file_content.split('\n')
#print(list)
#print("-------")
for element in list:
	if element !="":
		new_list = element.split(".")
		if new_list[len(new_list)-2] + "." + new_list[len(new_list)-1] == sys.argv[2]:
			#print(new_list)
			domain = new_list[-2] + '.' + new_list[-1]
			#print(domain)
			#print("#########")
			try:
				lenght = 0
				while lenght != len(new_list):
					url_element = new_list[-3-lenght]
					domain = url_element + '.' + domain
					print(domain)
					lenght = lenght + 1
			except IndexError:
				continue

