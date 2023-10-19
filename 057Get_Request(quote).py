# 057 urllib get request(quote method)
print(ord("a"))   # the output is 97
print(ord("A"))   # the output is 65
# according to ASCII encoding, a = 97, A = 65, 0 = 48
ascii_code = 48
character = chr(ascii_code)
print(character)

# customizing request object is a way to deal with antipython method
# unicode includes all the languages
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6 ( the last few stuff in this website is unicode)
import urllib.request
import urllib.parse
url = "https://www.baidu.com/s?wd=wd=%E5%91%A8%E6%9D%B0%E4%BC%A6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)

# I intend to convert chinese characters into unicode format
name = urllib.parse.quote("周杰伦")
print(name)
url = "https://www.baidu.com/s?wd="
url1 = url + name
print(url1)   # here we get https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# summarise: urllib.parse.quote() is a way to convert other characters into unicode way
