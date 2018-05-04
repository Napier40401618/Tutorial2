import urllib2,json,base64

accesstoken = "EQV9HNYF1QXG9CULFRCB"
institution = "10007772"
page = 0
course = "U56119"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
    institution,
    course,
    )
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)
a = data[6]["Details"]
b = a[8]["Value"]
print b

c = data[6]["Details"]
d = a[5]["Value"]
print d

e = data[5]["Details"]
f = a[0]["Value"]
print f

