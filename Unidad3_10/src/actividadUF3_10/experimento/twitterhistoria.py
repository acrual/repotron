import urllib.request
import re

user = input("Dime el usuario :")
keyword = input("Dime el keyword : ")
ano_inicial = input("Dime año inicial : ")
ano_final = input("Dime año final : ")
url = "https://twitter.com/search?q=from%3A" + user + "%20" + keyword + "%20since%3A" + ano_inicial + "-01-01%20until%3A" + ano_final + "-12-31&src=typd"
page = urllib.request.urlopen(url).read().decode('utf-8')
start = 'js-tweet-text tweet-text" lang="en" data-aria-label-part="0">'
end = '</p>'
print(page)
results = re.findall('tweet-text', page)
contador = 0
print(results)
for result in results:
    print(result)
    print("")
    contador = contador + 1
print("Contador es ", contador)
