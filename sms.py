import requests
import time
message = "Dear {0}, Your RO is about to go dry for {1} at {2}. You are requested to place indent immediately to avoid dryout please . More info visit {3}. IOCL SALEM- MUNIYAPPAN".format("Muniyappan M",308946313,"Credit block",'www.ioslsalem.com')
# message="Dear {0}, Your SO no:{1} cannot be processed due to {2}. More information visit {3}. IOCL SALEM Terminal- MUNIYAPPAN".format("Muniyappan M",308946313,"Credit block",'www.ioslsalem.com')
# message="Dear {#var#}, Your RO is about to go dry for {#var#} at {#var#}.You are requested to place indent immediately to avoid dryout please . More info visit {#var#}. IOCL SALEM- MUNIYAPPAN"
# message="Dear 6787, Your RO is about to go dry for 65767 at 6789. You are requested to place indent immediately to avoid dryout please . More info visit 5768. IOCL SALEM- MUNIYAPPAN"
mobileno= '918870887201'
sender = 'MUNIMM'
apikey = '1025ci03w5o077767a02l983n405q4620ne'

baseurl = 'https://instantalerts.co/api/web/send/?apikey='+apikey

print(baseurl)
url= baseurl+'&sender='+sender+'&to='+mobileno+'&message='+message+'&format=json'
print(url)
for i in range(1):
    response = requests.get(url)
    time.sleep(2)
print(response.json())
# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response, 'Problem with the request.')
exit()