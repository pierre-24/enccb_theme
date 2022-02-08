import svgwrite
import random

WIDTH = 2000
HEIGHT = 500
NPOINTS = 7
NLAYERS = 5
DOT_RADIUS = 3
EXTRA_CONNEXION = 5
BORDER = 100

STYLES = ''
color= '#ccc';

for i in range(NLAYERS):
    STYLES += '#layer{i} {{fill:{c}; stroke:{c}; }}'.format(i=i, c=color)

points = []

dw = svgwrite.Drawing('header-bg.svg', (WIDTH, HEIGHT))
dw.defs.add(dw.style(STYLES))


# create a random set of points
for layer in range(NLAYERS):
    points.append([])
    for p in range(NPOINTS):
        points[layer].append((random.random() * (WIDTH + 2 * BORDER) - BORDER, random.random() * (HEIGHT + 2 * BORDER) - BORDER))

for layer in range(NLAYERS):
    # layer
    layer_ = dw.add(dw.g(id='layer{}'.format(layer)))
    
    if layer != NLAYERS - 1:
        # define gaussian blur
        filtr_name = 'fltr{}'.format(layer)
        filtr = dw.defs.add(dw.filter(id=filtr_name, start=(0,0)))
        filtr.feGaussianBlur('SourceGraphic', stdDeviation=(1.5*(NLAYERS-layer-1)))
        layer_.attribs['filter'] = 'url(#{})'.format(filtr_name)
    for x, y in points[layer]:
        layer_.add(dw.circle((x, y), r=DOT_RADIUS))
        e = random.randint(0, NPOINTS - 1)
        layer_.add(dw.line(start=(x,y), end=points[layer][e]))
    if layer != NLAYERS - 1:
        for i in range(EXTRA_CONNEXION):
            s, e = random.randint(0, NPOINTS - 1), random.randint(0, NPOINTS - 1)
            layer_.add(dw.line(start=points[layer][s], end=points[layer+1][e]))
            

dw.save()
