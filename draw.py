from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    #Rt = (-P0 + 3P1 - 3P2 + P3)t^3 + (3P0 - 6P1 + 3P2)t^2 + (-3P0 + 3P1)t + P0
    #x =  at3 + bt2 + ct + d
    #   d + t(c + t(b + ta))
    if curve_type == 'bezier':
        ax = -1*x0 + 3*x1 - 3*x2 + x3
        ay = -1*y0 + 3*y1 - 3*y2 + y3
        bx = 3*x0 - 6*x1 + 3*x2
        by = 3*y0 - 6*y1 + 3*y2
        cx = -3*x0 + 3*x1
        cy = -3*y0 + 3*y1
        dx = x0
        dy = y0
        t = 0
        while t <= 1:
            xcoord = dx + t*(cx + t*(bx + t*ax))
            ycoord = dy + t*(cy + t*(by + t*ay))
            add_point(points, xcoord, ycoord)
            t += step
    #2P0-2P1+R0+R1
    #-3P0+3P1-2R0-R1
    #R0 = c
    #P0
    #f(t) = at3 + bt2 + ct + d : POINTS ON CURVE
    #f1(t) = 3at2 + 2bt + c : RATES OF CHANGE
    elif curve_type == 'hermite':
        ax = 2*x0 - 2*x1 + x2 + x3
        ay = 2*y0 - 2*y1 + y2 + y3
        bx = -3*x0 + 3*x1 - 2*x2 - x3
        by = -3*y0 + 3*y1 - 2*y2 - y3
        cx = x2
        cy = y2
        dx = x0
        dy = y0
        t = 0
        while t <= 1:
            xcoord = dx + t*(cx + t*(bx + t*ax))
            ycoord = dy + t*(cy + t*(by + t*ay))
            add_point(points, xcoord, ycoord)
            t += step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
