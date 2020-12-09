#!python
import view
view.encodeUTF8()


print(
  view.strStart+
  '<ol>'+view.getList()+'</ol>'+
  view.createForm()+
  '''
  </body>
  </html>
  ''')