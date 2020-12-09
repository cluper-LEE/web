#!python
import view
view.encodeUTF8()

print(
    view.strStart+
    '<ol>'+view.getList()+'</ol>'+
    view.strCreate+
    view.updateForm()+
    '''
</body>
</html>
''')
