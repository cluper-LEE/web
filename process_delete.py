#!python
import cgi, os
form = cgi.FieldStorage()
pageId = form.getvalue('pageId')

os.remove('data/'+pageId)

print("Location: index.py")
print()
