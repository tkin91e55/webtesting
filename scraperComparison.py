FIELDS = ('area', 'population', 'iso', 'country', 'capital',
          'continent', 'tld', 'currency_code', 'currency_name', 'phone',
          'postal_code_format', 'postal_code_regex', 'languages',
          'neighbours')

import re
def re_scraper(html):
    results = {}
    for field in FIELDS:
        results[field] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
    return results

from bs4 import BeautifulSoup
def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_%s__row' % field).find('td', class_='w2p_fw').text
    return results

import lxml.html
def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()
    return results

import time
from download import download
if __name__ == '__main__':
    NUM_ITERATIONS = 1000  # number of times to test each scraper
    html = download('http://example.webscraping.com/places/view/United-Kingdom-239')

    for name, scraper in [('Regular expressions', re_scraper),
                          ('BeautifulSoup', bs_scraper),
                          ('Lxml', lxml_scraper)]:
        # record start time of scrape
        start = time.time()
        for i in range(NUM_ITERATIONS):
            if scraper == re_scraper:
                re.purge()
            result = scraper(html)
            # check scraped result is as expected
            assert (result['area'] == '244,820 square kilometres')
        # record end time of scrape and output the total
        end = time.time()
        print '%s: %.2f seconds' % (name, end - start)
