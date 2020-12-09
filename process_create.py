#!python
import cgi
form = cgi.FieldStorage()
title = form.getvalue('title')
description = form.getvalue('description')

if '–' in description:
    description = description.replace('–', '-')


openedfile = open('data/'+title,'w')
openedfile.write(description)
openedfile.close()

print("Location: index.py?id="+title)
print()
