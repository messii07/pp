import geometry
def pointyShapeVolume(x,h,square):
    if square:
        base=geometry.squareArea(x)
    else:
        base=geometry.circleArea(x)
    return h*base/3.0
print dir(geometry)
print pointyShapeVolume(4, 2.6, True)
print pointyShapeVolume(4, 2.6, False)

