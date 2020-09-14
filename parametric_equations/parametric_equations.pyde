def setup():
    size(800, 800)
    background('#004477')
    strokeWeight(3)
    
def parabola(x):
    y = x * x
    return y

def circle_(t):
    x = cos(t)
    y = sin(t)
    return [x, y]

def ellipse_(t, w, h):
    x = cos(t) * w
    y = sin(t) * h
    return [x, y]

def lissajous(t, a, b, kx, ky):
    x = a * cos(kx*t)
    y = b * sin(ky*t)
    return [x, y]

x = -300.0
y = 0.0
t = 0.0
h = 0

def draw():
    global x, y, t, h
    t += 0.005
    translate(width/2, height/2)
    #stroke('#0099FF')
    #line(width/2*-1, 0, width/2, 0)
    #line(0, height/2*-1, 0, height/2)
    
    stroke('#FFFFFF')
    '''
    y = parabola(x)
    x += 1
    point(x, y)
    '''
    '''
    xy = ellipse_(t, 200, 100)
    t += 0.01
    point(xy[0], xy[1])
    '''
    
    fill(0x22000000)
    rect(-width/2, -height/2, width, height)
    xy1 = lissajous(t, 200, 100, 5, 4)
    xy2 = lissajous(t, 300, 50, 3, 1)
    xy3 = lissajous(t, 400, 150, 1, 3)
    
    xy4 = lissajous(t, 250, 150, 3, 2)
    xy5 = lissajous(t, 350, 100, 4, 7)
    xy6 = lissajous(t, 450, 200, 2, 3)
    
    colorMode(HSB, 360, 100, 100)
    stroke(h, 100, 100)
    h += 1
    if h > 360:
        h = 0
        
    triangle(xy1[0], xy1[1], xy2[0], xy2[1], xy3[0], xy3[1])
    stroke(h+180%360, 100, 100)
    triangle(xy4[0], xy1[1], xy5[0], xy2[1], xy6[0], xy3[1])
    
    
    
