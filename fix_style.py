content = open(r'c:\xampp\htdocs\canva\index.html', encoding='utf-8').read()
s = content.find('<style>')
e = content.find('</style>') + len('</style>')
link_tag = '<link rel="stylesheet" href="style.css">'
result = content[:s] + link_tag + content[e:]
open(r'c:\xampp\htdocs\canva\index.html', 'w', encoding='utf-8').write(result)
print('Done. Total lines:', result.count('\n'))
