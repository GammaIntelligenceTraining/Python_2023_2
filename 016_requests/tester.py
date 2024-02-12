import requests

# 200 - 299 Success
# 300 - 399 Redirect
# 400 - 499 Client error
# 500 - 599 Server error

r = requests.get('https://xkcd.com/353/', timeout=10)
print(r.ok)