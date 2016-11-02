from Throttle import Throttle
from download import download

url = 'http://hk.yahoo.com'
delay = 10
throttle = Throttle(delay)

print 'log 1'
throttle.wait(url)
print 'log 2'
result = download(url)

print 'log 3'
throttle.wait(url)
print 'log 4'
result = download(url)

print 'log 5'
throttle.wait(url)
print 'log 6'
result = download(url)
