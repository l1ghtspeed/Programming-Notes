import random
import string

class URLShortener:
    def __init__(self):
        self.short_to_url = {}
        self.url_to_short = {}

    def _generate_short(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def _generate_unused_short(self):
        t = self._generate_short()
        while t in self.short_to_url:
            t = self._generate_short()
        return t

    def shorten(self, url):
        short = self._generate_unused_short()
        if url in self.url_to_short:
            return self.url_to_short[url]
        self.short_to_url[short] = url
        self.url_to_short[url] = short
        return short

    def restore(self, short):
        return self.short_to_url.get(short, None)