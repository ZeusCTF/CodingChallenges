"""
535. Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/
Difficulty: Medium  Topic: Hash Map, String

Design a URL shortener: encode(longUrl) → short URL, decode(shortUrl) → original.

Approach: Assign a sequential integer key per URL; store both mappings.
"""

class Codec:
    def __init__(self):
        self._encode_map: dict = {}
        self._decode_map: dict = {}
        self._base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self._encode_map:
            key = str(len(self._encode_map) + 1)
            self._encode_map[longUrl] = self._base + key
            self._decode_map[key] = longUrl
        return self._encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.replace(self._base, "")
        return self._decode_map[key]
