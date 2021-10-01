from IPython.display import HTML, display

def maxHeight(parent):
  if len(parent.children) == 0:
    return parent.height 
  max = 0
  for child in parent.children:
    m = maxHeight(child)
    if m> max:
      max = m
  return max
  
def drawBlockchain(parent, level, html, parentLevel, childN = 0, total = 0):
  color = "#AEF751"
  if parentLevel!=-1:
    color = parent.color
  parent.children.sort(key=lambda x: (maxHeight(x)), reverse=True)
  xx = childN
  level += childN
  html += '<g>'
  html += '<rect x="'+str(30+ 100*parent.height)+'" y="'+str(30+ 100*level)+'" width="60" height="60" stroke="black" stroke-width="1" fill="'+color+'" />'
  html += '<text x="'+str((60+ 100*parent.height))+'" y="'+str((60+ 100*level))+'" dominant-baseline="middle" text-anchor="middle" font-family="Verdana" font-size="10" font-weight="bold" fill="black">'+str(parent.creator.name)+'</text>'
  if parentLevel != -1:
    if (parent.previous.children.index(parent)) == 0:
      html += '<line stroke-width="1px" stroke="#000000"  x1='+str(30+ 100*parent.height)+' y1="'+str(60+ 100*level)+'" x2="'+str(95+ 100*parent.previous.height)+'" y2="'+str(60+ 100*parentLevel)+'" style="marker-end: url(#markerArrow)"/>'
    else:
      html += '<line stroke-width="1px" stroke="#000000"  x1='+str(30+ 100*parent.height)+' y1="'+str(60+ 100*level)+'" x2="'+str(65+ 100*parent.previous.height)+'" y2="'+str(95+ 100*parentLevel)+'" style="marker-end: url(#markerArrow)"/>'
  html += '</g>'
  l = level
  childN = 0
  for child in parent.children:
    html,n, t = drawBlockchain(child, l, html, level, childN, total)
    if n > 0:
      childN += n
    if t > 0:
      total += t
    l = l+1
  return html, childN+ len(parent.children)-1, total+ len(parent.children)-1


def show(bc):
  htmll = ""
  html = ""
  htmll, n, t = drawBlockchain(bc.chain[0], 0, html, -1)
  html = '<svg height="'+str(115*(n+1))+'" width="'+str(115*maxHeight(bc.chain[0]))+'">'
  html += '<defs><marker id="markerArrow" markerWidth="10" markerHeight="10" refX="2" refY="6" orient="auto"><path d="M2,2 L2,11 L10,6 L2,2" style="fill: #000000;" /> </marker> </defs>'
  html += htmll
  html += '</svg>'
  display(HTML(html))