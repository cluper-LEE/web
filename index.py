#!python
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("content-type: text/html; charset=utf-8\n")
import cgi
form = cgi.FieldStorage()
pageId = form.getvalue('id')

print('''
<!doctype html>
<html>
<head>
  <title>MOS Structures</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.py?id=MOS Structure">MOS Structure</a></h1>
  <ol>
    <li><a href="index.py?id=MOSCAP">MOSCAP</a></li>
    <li><a href="index.py?id=MOSFET">MOSFET</a></li>
    <li><a href="index.py?id=CMOS">CMOS</a></li>
  </ol>
  <h2>{title}</h2>
  <a href="https://en.wikipedia.org/wiki/MOSFET#Metal%E2%80%93oxide%E2%80%93semiconductor_structure" target=_blank><img src="mos.png"></a>
  <p>
    The traditional metal–oxide–semiconductor (MOS) structure is obtained by growing a
    layer of silicon dioxide (SiO2) on top of a silicon substrate, commonly by thermal
    oxidation and depositing a
    layer of metal or polycrystalline silicon (the latter is commonly used).
    As the silicon dioxide is a dielectric material, its structure is equivalent to a
    planar capacitor, with one of the electrodes replaced by a semiconductor.
  </p>
</body>
</html>
'''.format(title=pageId))