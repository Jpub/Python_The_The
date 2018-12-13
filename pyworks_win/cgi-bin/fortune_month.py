#!/usr/bin/env python

import datetime
import cgi
import cgitb
cgitb.enable()

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')

http_body = '''<html>
<head>
<meta charset="UTF-8">
<title>오늘의 운세</title>
</head>
<body>
{month}월생인 당신의 오늘 운세는 {fortune} 이다.
</body>
</html>'''

# URL의 파라미터로부터 month를 얻는다. 문자열형이므로 정수로 변환.
param_data = cgi.FieldStorage()
month = int(param_data.getvalue('month'))

# datetime을 이용해서 현재 일시 얻기
today = datetime.date.today()
contents = {}
contents['month'] = month
contents['fortune'] = ['대길(大吉)', '중길(中吉)', '길(吉)', '말길 (末吉)', '흉(凶)', '대흉(大凶)'][today.day * month % 6]

print('Content-type: text/html')
print('')
print(http_body.format(**contents))