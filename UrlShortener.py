import hashlib

class UrlShortener:
    # Defining class variables
    def __init__(self):
        self.url_mapping = {}
        self.base_url = 'https://mytiny.url/'

    def shorten_url(self, original_url):
        # Use SHA-256 hashing function to hash original url
        # Trunkate the first 6 characters
        # Append those characters to self.base_url
        # Map shortened url to og url

        # Hashing functions in the hashlib library return the binary representation of the hash (a sequence of bytes).

        # Why: URLs can contain special characters (like ?, &, =, /) or even spaces. 
        # If you don't encode the URL before hashing,
        # different forms of the same URL could result in different hashes.
        # For example, URLs with spaces could be represented as actual spaces, %20, or +, 
        # leading to different hash values for what is essentially the same URL.
        # How: By URL encoding the URL, you standardize it into a consistent format that eliminates ambiguities. 
        # This ensures that the same logical URL will always produce the same hash.
        hash_val = hashlib.sha256(original_url.encode()).hexdigest()[:6]
        short_url = self.base_url + hash_val
        self.url_mapping[short_url] = original_url
        return short_url

    def expand_url(self, short_url):
        original_url = self.url_mapping[short_url]
        return original_url



# script region

url_shortener = UrlShortener()

original_url = input('Enter the url you want to shorten: ')
short_url = url_shortener.shorten_url(original_url)

print('Your shortened url is: ' + short_url)
print('The orginal url was: ' + url_shortener.expand_url(short_url))
