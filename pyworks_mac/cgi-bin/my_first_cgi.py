#!/usr/bin/env python

html_body = '''<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>CGI</title>
  </head>
  <body>
    CGI 시작하기
  </body>
</html>'''

print('Content-type: text/html')
print('')
print(html_body)