import hashlib


class UrlShortener:
    # Defining class variables
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "https://mytiny.url/"

    def shorten_url(self, original_url):
        hash_val = hashlib.sha256(original_url.encode()).hexdigest()[:6]
        short_url = self.base_url + hash_val
        self.url_mapping[short_url] = original_url
        return short_url

    def expand_url(self, short_url):
        original_url = self.url_mapping[short_url]
        return original_url


# script region
url_shortener = UrlShortener()

original_url = input("Enter the url you want to shorten: ")
short_url = url_shortener.shorten_url(original_url)

print("Your shortened url is: " + short_url)
print("The orginal url was: " + url_shortener.expand_url(short_url))
