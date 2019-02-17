import argparse
import urllib2
import csv
import datetime
import logging
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="Enter url you want to download csv")
    args = parser.parse_args()

    url = args.url
    #url = 'https://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    try:
        data = downloadData(url)
    except:
        print("Invaild URL")
        exit()
    else:
        processData(data)

def downloadData(url):
    url = urllib2.urlopen(url)
    return url

def processData(data):
    imgPath = re.compile('.{4}$')
    csvData = csv.reader(data)
    imgHits = 0
    total_row = 0
    percentage_wise = 0
    browser_dir = {'Firefox':0,'Chrome':0,'Internet Explorer':0,'Safari':0}

    for x in csvData:
        total_row += 1
        extension = imgPath.search(x[0]).group()
        if (re.search('Firefox',x[2]) or re.search('firefox',x[2])):
            browser_dir['Firefox'] += 1
        elif(re.search('Chrome',x[2]) or re.search('chrome',x[2])):
            browser_dir['Chrome'] += 1
        elif (re.search('Internet Explorer', x[2]) or re.search('internet explorer', x[2])):
            browser_dir['Internet Explorer'] += 1
        elif (re.search('Safari', x[2]) or re.search('safari', x[2])):
            browser_dir['Safari'] += 1
        if(extension=='.jpg' or extension=='.gif' or extension=='.png'):
            imgHits += 1

    top_brow = [max(zip(browser_dir.values(), browser_dir.keys()))]
    top_browser = top_brow[0][1]
    top_browser_hit = top_brow[0][0]
    percentage_wise = ((imgHits*1.0)/total_row)*100
    print('Image requests account for {:,} hits of all requests'.format(imgHits))
    print('Image requests account for {0} % of all requests'.format(percentage_wise))
    print("The most popular browser is {0} and {1} hits".format(top_browser,top_browser_hit))

main()