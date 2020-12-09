#!python
import view
view.encodeUTF8()

print(
  view.strStart+
  '<ol>'+view.getList()+'</ol>'+
  view.strCreate+
  '\t'+
  view.update_action()+
  view.delete_action()+
  '<h2>'+view.pageId()+'</h2>'+
  view.image()+
  '<p>'+view.description()+'</p>'+
  '''
  </body>
  </html>
  ''')
