import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

url = "https://example.com"
print(f"Shortened URL: {shorten_url(url)}")
