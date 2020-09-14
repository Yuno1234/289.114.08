def sayHello(name, surname):
    print('hello ' + name + ' ' + surname)
    print('how are you doing?')
    
sayHello('Sam', 'Smith')

size(300, 300)
background('#004477')

def drawFace(x, y, eyecolor, smilefrown):
    noFill()
    stroke('#FFFFFF')
    pushMatrix()
    translate(x, y)
    circle(0, 0, 40)
    fill(eyecolor)
    square(-10, -10, 5)
    square(5, -10, 5)
    noFill()
    
    if smilefrown == 'smile':
        arc(0, 5, 20, 20, 0, PI, PIE)
    if smilefrown == 'frown':
        arc(0, 10, 20, 20, PIE, TAU, PIE)
    
    popMatrix()
    
drawFace(50, 50, '#FF0000', 'smile')
drawFace(150, 80, '#FFFF00', 'frown')
drawFace(200, 130, '#FFFF00', 'frown')
drawFace(60, 200, '#FFFF00', 'smile')
