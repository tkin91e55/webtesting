"""
Supporting proxies with
urllib2 is not as easy as it could be (for a more user-friendly Python HTTP module,
try requests , documented at http://docs.python-requests.org/ ). Here is how
to support a proxy with urllib2 :

proxy = ...
opener = urllib2.build_opener()
proxy_params = {urlparse.urlparse(url).scheme: proxy}
opener.add_handler(urllib2.ProxyHandler(proxy_params))
response = opener.open(request)
"""