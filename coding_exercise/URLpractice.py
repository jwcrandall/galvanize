

def parse_shortened_url(url_list):
    clean_list = []
    shortend_list = []
    # Compare url with known url shortener
    known_url_shortener = ['rebrandly',
                            'bitly',
                            'tinyurl',
                            'tiny.cc',
                            'lc.chat',
                            'is.gd',
                            'soo.gd',
                            's2c.co']
    # Use regex to identify classifiers

    return clean_list

def unmask_shortend_url(masked_url_list):
    session = requests.Session()  # so connections are recycled
    UNmasked_url_list = session.head(masked_url_list, allow_redirects = True)
    return UNmasked_url_list.url

    response = urllib.requests.urlopen(masked_url_list)
    final_url = response.geturl()
    # response_code will be 302 for redirects
    response_code = response.getcode() #return the HTTP status code of the response.

    if response_code == 302:
        # redirected so this may be ßa short url
    else:
        # this is not a short url
