#!/user/bin/python

import socket
import sys
import re
import json
from urllib2 import urlopen

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print "Number of wrong arguments!"
    sys.exit()
elif sys.argv[1] != "--myip":
    address = sys.argv[1]
    try: 
        socket.inet_aton(address)
        url = 'http://ip-api.com/json/' + address
        response = urlopen(url)
        data = json.load(response)
        print "IP: " + data['query']
        print "ORG: " + data['as']
        print "ISP: " + data['isp']
        print "Country: " + data['country'] + " - " + data['countryCode']
        print "Region: " + data['regionName'] + " - " + data['region']
        print "City: " + data['city']
        print "Latitude: " + str(data['lat'])
        print "Lontitude: " + str(data['lon'])
        print "Timezone: " + data['timezone']
        print "Zip code: " + data['zip']
    except socket.error:
        print "Invalid IP address!"
else:
     url = 'http://ip-api.com/json/'
     response = urlopen(url)
     data = json.load(response)
     print "IP: " + data['query']
     print "ORG: " + data['as']
     print "ISP: " + data['isp']
     print "Country: " + data['country'] + " - " + data['countryCode']
     print "Region: " + data['regionName'] + " - " + data['region']
     print "City: " + data['city']
     print "Latitude: " + str(data['lat'])
     print "Lontitude: " + str(data['lon'])
     print "Timezone: " + data['timezone']
     print "Zip code: " + data['zip']

