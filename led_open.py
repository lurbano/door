import board
import neopixel

nPix = 20
pixels = neopixel.NeoPixel(board.D21, 20)

for i in range(nPix):
    pixels[i] = (0,100,0)