"""
Create an abstract background image of linked dots
"""

__version__ = '0.1'

import svgwrite
import random
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    
    parser.add_argument('outfile', type=str, default='out.svg')
    
    parser.add_argument('-W', '--width', type=int, default=2000)
    parser.add_argument('-H', '--height', type=int, default=500)
    parser.add_argument('-B', '--border', type=int, default=50, help='Extra space')
    
    parser.add_argument('-c', '--color', type=str, default='#ccc', help='Color')
    parser.add_argument('-n', '--points-per-layer', type=int, default=5, help='Number of point in each layer')
    parser.add_argument('-r', '--point-radius', type=float, default=4.0, help='Radius of a point')
    parser.add_argument('-L', '--layers', type=int, default=5, help='Number of layer')
    parser.add_argument('-C', '--interlayer-connexions', type=int, default=2, help='Number of interlayer connexions')
    parser.add_argument('-f', '--fuzzing', type=float, default=1.25, help='Fuzzing factor between two layers')
    
    args = parser.parse_args()
    
    # create image
    dw = svgwrite.Drawing(args.outfile, (args.width, args.height))
    
    # add style
    STYLES = ''
    for i in range(args.layers):
        STYLES += '#layer{i} {{fill:{c}; stroke:{c}; }}'.format(i=i, c=args.color)
    
    dw.defs.add(dw.style(STYLES))

    # create a random set of points
    points = []
    for layer in range(args.layers):
        points.append([])
        for p in range(args.points_per_layer):
            points[layer].append((
                random.random() * (args.width + 2 * args.border) - args.border, 
                random.random() * (args.height + 2 * args.border) - args.border
            ))

    for layer in range(args.layers):
        layer_ = dw.add(dw.g(id='layer{}'.format(layer)))  # group
        
        # define gaussian blur
        if layer != args.layers - 1:
            filtr_name = 'fltr{}'.format(layer)
            filtr = dw.defs.add(dw.filter(id=filtr_name, start=(0,0)))
            filtr.feGaussianBlur('SourceGraphic', stdDeviation=(args.fuzzing * (args.layers - layer - 1)))
            layer_.attribs['filter'] = 'url(#{})'.format(filtr_name)
         
        # add points and a random connexion
        for i, (x, y) in enumerate(points[layer]):
            layer_.add(dw.circle((x, y), r=args.point_radius))
            e = i
            while e == i:
                e = random.randint(0, args.points_per_layer - 1)
            layer_.add(dw.line(start=(x,y), end=points[layer][e]))
        
        # add interlayer connexion
        if layer != args.layers - 1:
            for i in range(args.interlayer_connexions):
                s, e = random.randint(0, args.layers - 1), random.randint(0, args.layers - 1)
                layer_.add(dw.line(start=points[layer][s], end=points[layer+1][e]))
   
    # save
    dw.save()

if __name__ == '__main__':
    main()
  
