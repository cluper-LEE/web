import os, cgi, view
def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
          listStr += '<li><a href="index.py?id={name}">{name}</a></li>\n'.format(name=item)
    return listStr

def pageId():
    form = cgi.FieldStorage()
    if 'id' in form:
        pageId = form.getvalue('id')
    else:
        pageId='Welcome'
    return pageId

def description():
    form = cgi.FieldStorage()
    pageId = view.pageId()
    if 'id' in form:
        description = open('C:/Bitnami/wampstack-7.4.12-0/apache2/htdocs/data/'+pageId, 'r', encoding='utf-8').read()
    else:
        description = 'Hello Semiconductor'
    if '–' in description:
        description = description.replace('–', '-')
    return description

def update_action():
    form = cgi.FieldStorage()
    pageId = view.pageId()
    if 'id' in form:
        update_action = '<a href="update.py?id={}">update</a>'.format(pageId)
    else:
        update_action = ''
    return update_action

def delete_action():
    form = cgi.FieldStorage()
    pageId = view.pageId()
    if 'id' in form:
        delete_action = '''
        <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{title}">
        <input type="submit" value="delete  {title}">
        </form>
        '''.format(title=pageId)
    else:
        delete_action = ''
    return delete_action


def image():
    pageId = view.pageId()
    image = ''
    if pageId in image_sources:
        if pageId in image_links:
            image = '<a href="{link}" target=_blank><img src="image/{source}"></a>'.format(link=image_links[pageId], source=image_sources[pageId])
        else:
            image = '<img src="{source}">'.format(source=image_sources[pageId])
    elif pageId in image_sources:
        image = '<a href="{}" target=_blank>{}</a>'.format(image_links[pageId])
    return image

def encodeUTF8():     
    import sys
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    print("content-type: text/html; charset=utf-8\n")


def createForm():
    createForm='''
    <form action = process_create.py method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="30" cols="50" name="description" placeholder="description"></textarea></p>
        <p><input type="submit" value="create"></p>
    </form>'''
    return createForm

def updateForm():
    updateForm='''
    <form action = "process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="30" cols="50" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit" value='update'></p>
    </form>'''.format(form_default_title=view.pageId(), form_default_description=view.description())
    return updateForm


strStart = '''
<!doctype html>
<html>
<head>
  <title>Semiconductor</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href='index.py'>Semiconductor</h1>
'''
strCreate = '<a href="create.py">create</a>'


image_sources = {'MOSCAP':'metalstack.gif', 'MOSFET':'mosfet.png', 'CMOS':'cmos.png', 'MOS Structure':'mos.png', 'SIO2':'sio2.png'}
image_links = {'MOSCAP':'https://www.naver.com', 'MOSFET':'https://en.wikipedia.org/wiki/MOSFET', 'MOS Structure':'https://en.wikipedia.org/wiki/MOSFET', 'SIO2':'https://en.wikipedia.org/wiki/Silicon_dioxide'}