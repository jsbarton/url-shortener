# url-shortener

URL Shortener built using Python

## About URL Hashing

- Hashing functions in the hashlib library return the binary representation of the hash (a sequence of bytes).

## Encoding urls

- URLs can contain special characters (like ?, &, =, /) or even spaces. If you don't encode the URL before hashing, different forms of the same URL could result in different hashes.
- For example, URLs with spaces could be represented as actual spaces, %20, or +, leading to different hash values for what is essentially the same URL.
- By URL encoding the URL, you standardize it into a consistent format that eliminates ambiguities. This ensures that the same logical URL will always produce the same hash.
