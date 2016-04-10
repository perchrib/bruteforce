# coding=utf-8

def get_data():
	file = open('byer.txt','r')
	data = [line.strip() for line in file]
	data = [line.split() for line in data]
	return data
