import sys, os
import json
import csv
import subprocess

pathname = os.path.dirname(sys.argv[0])

proc = subprocess.Popen(["speedtest-cli --json"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

stats = json.loads(out)
#print(stats)
#{'download': 46794573.21491837, 'upload': 21733575.159537446, 'ping': 37.285, 'server': {'url': 'http://speedtest.imedia.ie:8080/speedtest/upload.php', 'lat': '52.6652', 'lon': '-8.6238', 'name': 'Limerick', 'country': 'Ireland', 'cc': 'IE', 'sponsor': 'Integrated Media Solutions', 'id': '7517', 'host': 'speedtest.imedia.ie:8080', 'd': 73.08486064764851, 'latency': 37.285}, 'timestamp': '2021-03-12T17:01:55.109911Z', 'bytes_sent': 28852224, 'bytes_received': 58685475, 'share': None, 'client': {'ip': '37.228.254.243', 'lat': '53.2702', 'lon': '-9.0503', 'isp': 'Virgin Media Ireland', 'isprating': '3.7', 'rating': '0', 'ispdlavg': '0', 'ispulavg': '0', 'loggedin': '0', 'country': 'IE'}}

with open(os.path.abspath(pathname)+"/bradband_stats.csv", "a") as outfile:
    f = csv.writer(outfile)
    f.writerow([stats["timestamp"],stats["download"]/1000000, stats["upload"]/1000000, stats["ping"], stats["client"]["isp"]])