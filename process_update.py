#!python

import cgi, os
form = cgi.FieldStorage()
title = form.getvalue('title')
pageId =form.getvalue('pageId')
description = form.getvalue('description')

if '–' in description:
    description = description.replace('–', '-')

openedfile = open('data/'+pageId,'w')
openedfile.write(description)
openedfile.close()

os.rename('data/'+pageId, 'data/'+title)

print("Location: index.py?id="+title)
print()
