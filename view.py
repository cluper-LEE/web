import os, cgi, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

def getList():
    files = os.listdir('data')
    listStr = ''
    pageId=view.pageId()
    for item in files:
        item = sanitizer.sanitize(item)
        if pageId == item:
            listStr += f'<li><a href="index.py?id={item}" class="thisPage">{item}</a></li>\n'
        else:
            listStr += f'<li><a href="index.py?id={item}">{item}</a></li>\n'
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
        description = sanitizer.sanitize(description);
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
            image = '<img src="image/{source}">'.format(source=image_sources[pageId])
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
  <style>
    .thisPage {
      color:blue;
      text-decoration: none;
    }
    a {
      color:black;
      text-decoration: none;
    }
    h1 {
      font-size: 60px;
      text-align: center;
      border-bottom: 1px solid gray;
      padding: 30px;
      margin:0px;
      display:block;
      margin-left:auto;
      margin-right:auto;
      
    }
    #grid ol {
      border-right:1px solid gray;
      width:150px;
      padding-left:32px;
      margin:30px;
    }
    #grid {
      display: grid;
      grid-template-columns: 0px 220px 1fr;
    }
    #article{
      margin:30px;
    }
    
  </style>
</head>
<body>
  <h1><a href='index.py'>Semiconductor</h1>
'''
strCreate = '<a href="create.py">create</a>'



image_sources = {'MOSCAP':'metalstack.gif', 'MOSFET':'mosfet.png', 'CMOS':'cmos.png', 'MOS Structure':'mos.png', 'SIO2':'sio2.png'}
image_links = {'MOSCAP':'https://www.naver.com', 'MOSFET':'https://en.wikipedia.org/wiki/MOSFET', 'MOS Structure':'https://en.wikipedia.org/wiki/MOSFET', 'SIO2':'https://en.wikipedia.org/wiki/Silicon_dioxide'}
