import requests
import sys	

token = "XXX"

headers = {
  'Authorization': 'Bearer ' + token, 
  "Accept": "application/json"
}

if len(sys.argv) != 2	:
	print("investigate_domains.py domain_file.txt")
	exit()

file1 = open(sys.argv[1], 'r')
for domain1 in file1:
    domain2=domain1.split("/")[0]
    domain=domain2.rstrip("\n")
    url = "https://investigate.api.umbrella.com/domains/categorization/"+domain+"?showLabels"
    response = requests.request("GET", url, headers=headers)
    print(response.text)
file1.close()
