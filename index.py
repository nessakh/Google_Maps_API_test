#!/usr/bin/python

import argparse
import urllib2
import json
from key import key
def Main():
	radius = 0
	categorie = 0
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--radius", action='store',
    dest='radius_value', help='Store a radius value')
	parser.add_argument("-c", "--categorie", action='store',
	dest='categorie_value', help="Store a categorie value ")
	args = parser.parse_args()
	if args.radius_value:
		radius = args.radius_value
		print("radius : ", args.radius_value)
	else:
		radius = 1000
		print("radius : ", radius)

	if args.categorie_value:
		categorie = args.categorie_value
		print("categorie : ", args.categorie_value)
	else:
		categorie = 'food'
		print("categorie : ", categorie)
	location_search(radius, categorie)


def location_search(radius, categorie):
	url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location=48.859294,2.347589'
	final_url = url + "&radius=" + str(radius) + '&type=' + categorie + '&key=' + key
	print final_url
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)
	for item in data['results']:
		print item['place_id']
		# print item ['reference']
		get_name(item['place_id'])
		print ('**************************************************************')

def get_name(placeid):
	url = 'https://maps.googleapis.com/maps/api/place/details/json?'
	final_url = url + 'placeid=' + placeid + '&key=' + key
	print final_url
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)
	print data["result"]["name"] 
Main()
