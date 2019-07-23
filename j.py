import httplib
conn = httplib.HTTPConnection("google.com")
res = conn.getresponse()
res.getheaders()


# import http.client
# conn = http.client.HTTPConnection("google.com")
# res = conn.getresponse()
# res.getheaders()


# from httpclient import HttpClient
#
# http_client = HttpClient()
# page = http_client.get("http://www.google.com")
#
# print(page.content_as_string)


# import socket
# a=socket.gethostbyaddr("69.59.196.211")
# print a[0]
