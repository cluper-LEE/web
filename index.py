#!python
import view
view.encodeUTF8()

print(
  view.strStart+
  '<div id="grid">'+
    '<ol>'+view.getList()+'</ol>'+
    '<div id="article">'+
      view.strCreate+
      '\t'+
      view.update_action()+
      view.delete_action()+ 
      '<h2>'+view.pageId()+'</h2>'+
      view.image()+
      '<p>'+view.description()+'</p>'+
    '</div>'+
  '</div>'+
  '''
  </body>
  </html>
  ''')
