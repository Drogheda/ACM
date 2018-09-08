import re
import hashlib
import requests
from urllib import request, parse

RE_MOVIE_URLS = r'<td valign="top">[\d\D]*?<a href="(.*?)"  class="">'
RE_MOVIE_NAME = r'<span property="v:itemreviewed">(.*?)</span>'
RE_MOVIE_GENRE = r'<span property="v:genre">(.*?)</span>';
RE_MOVIE_SCORE = r'<strong class="ll rating_num" property="v:average">(.*?)</strong>';
RE_MOVIE_DESC = r'<span property="v:summary" class="">([\d\D]*?)</span>'
RE_DESC_REPLACE = r'<.*?>|\s';

def getOr(array, index = 0, default = ''):
    return array[index] if len(array) > index else default

def get_html(url):
    try:
        return requests.get(url).text
    except:
        return ''

def match_movie_urls(html):
    return re.findall(RE_MOVIE_URLS, html)

def match_movie_info(html):
    print('please wait...')
    name = getOr(re.findall(RE_MOVIE_NAME, html))
    genre = '/'.join(re.findall(RE_MOVIE_GENRE, html))
    score = getOr(re.findall(RE_MOVIE_SCORE, html))
    descHtml = getOr(re.findall(RE_MOVIE_DESC, html))
    desc = re.sub(RE_DESC_REPLACE, '', descHtml)

    return {
        '名称': name,
        '类型': genre,
        '评分': score,
        '简介': desc
    }

homeUrl = 'https://movie.douban.com/chart'
movieUrls = re.findall(RE_MOVIE_URLS, requests.get(homeUrl).text)
print(list(movieUrls))
composed = lambda x: match_movie_info(get_html(x))
movies = list(map(composed, movieUrls))
		
# print(movies)




# print('Login to weibo.cn...')
# email = input('Email:')
# password = input('Password:')
# login_data = parse.urlencode([
	# ('username', email),
   # ('password', password),
   # ('entry', 'mweibo'),
   # ('client_id', ''),
   # ('savestate', '1'),
   # ('ec', ''),
   # ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req, data = login_data.encode('utf-8')) as f:
	# print('Status:', f.status, f.reason)
	# for k, v in f.getheaders():
		# print('%s: %s' % (k, v))
	# print('Data:', f.read().decode('utf-8'))


# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
    # print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
        # print('%s: %s' % (k, v))
    # print('Data:', f.read().decode('utf-8'))
	
	
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	# data = f.read()
	# print('Status', f.status, f.reason)
	# for k, v in f.getheaders():
		# print('%s:%s' % (k, v))
	# print('Data:', data.decode('utf-8'))
# db = {
    # 'michael': 'e10adc3949ba59abbe56e057f20f883e',
    # 'bob': '878ef96e86145580c38c87f0410ad153',
    # 'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# md5_1 = hashlib.md5()
# md5_2 = hashlib.md5()
# md5_3 = hashlib.md5()

# md5_1.update('123456'.encode('utf-8'))
# print(md5_1.hexdigest())
# md5_2.update('abc999'.encode('utf-8'))
# print(md5_2.hexdigest())
# md5_3.update('alice2008'.encode('utf-8'))
# print(md5_3.hexdigest())

# key = r'mat cat hat pat'
# p1 = r'[^p]at'#这代表除了p以外都匹配
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))

# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

# print(re.split(r'\s+', 'a b  c'))
# print(re.split(r'[\s\,]+', 'a,b  c'))

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# t = '19:05:30'
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# m.group()

# print(re.match(r'^\w+@\w+.\w+$','someone@gmail.com'))

