#!/usr/bin/python3

import sys
import importlib.util
import io

def handler():
	print("Beginning rss handler")
	#change this to your path
	url_list = open("E:/mudit/Documents/RSS_Royal_Road/royalroad_urls.txt", "r")

	rssr = importlib.util.spec_from_file_location("rss_royalroad", "E:/mudit/Documents/RSS_Royal_Road/rss_royalroad.py")
	rssr_module = importlib.util.module_from_spec(rssr)
	rssr.loader.exec_module(rssr_module)

	for line in url_list:
		arr = line.split(",")
		print("Title: " + arr[0] + " URL: " + arr[1])
		title = "E:/mudit/Documents/RSS_Royal_Road/rss_feeds/" + arr[0] + ".rss"
		temp_out = io.open(title, "w", encoding='utf-8')
		temp_xml = rssr_module.parse_url(arr[1]).decode('utf-8')
		temp_xml = temp_xml.replace("“", '"')
		temp_xml = temp_xml.replace("”", '"')
		temp_xml = temp_xml.replace("’", "'")
		temp_xml = temp_xml.replace("‘", "'")
		temp_xml = temp_xml.replace("🗑️", "")

		#temp_xml = temp_xml.replace("&gt;", ">")
		temp_out.write(temp_xml)
		temp_out.close()
	exit(0)

handler()

