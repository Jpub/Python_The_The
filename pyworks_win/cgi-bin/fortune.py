#!/usr/bin/env python

import random
import cgitb
cgitb.enable()

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')

html_body = '''<html>
<head>
<meta charset="UTF-8">
<title>오늘의 운세</title>
</head>
<body>
오늘 당신의 운세는 {} 이다.
</body>
</html>'''

todays_fortune = random.choice(['대길(大吉)', '중길(中吉)', '길(吉)', '말길 (末吉)', '흉(凶)', '대흉(大凶)'])

print('Content-type: text/html')
print('')
print(html_body.format(todays_fortune))