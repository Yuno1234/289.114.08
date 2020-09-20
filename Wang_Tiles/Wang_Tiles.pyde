size(600, 600)
background('#004477')
noFill()
noStroke()

tiles = loadImage('00.gif')
tiles.resize(width/20, width/20)

col = 0
row = 0

for i in range(400):
    image(tiles, col, row)
    
    col += width/20
    
    if col >= width:
        col = 0
        row += height/20
