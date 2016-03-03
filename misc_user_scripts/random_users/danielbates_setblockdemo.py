#!/usr/bin/env python
#
from math import sin, cos, radians
import danielbates_minecraft_basic as mc
#import pygame.image # comment this out if not using images - it's slow to import.  If you uncomment, uncomment the image reference below.
import random
import server

# TODO: use numpy matrices/vectors instead of my own ones.
class coordinate3d:
  """Class used to represent a point in 3D space."""
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    return coordinate3d(self.x+other.x, self.y+other.y, self.z+other.z)

class transformation:
  """Representation of homogeneous matrices used to apply transformations to
coordinates - using a 4x4 matrix allows shifts as well as scales/rotations.
Transformations can be combined by multiplying them together."""
  def __init__(self, matrix):
    self.matrix = matrix

  def __mul__(self, other):
    if isinstance(other, transformation):
      return self.compose(other)
    elif isinstance(other, coordinate3d):
      return self.apply(other)
    else:
      print "Can't multiply transformation by {0}".format(type(other))

  def compose(self, other):
    """Compose this transformation with another, returning a new transformation."""
    newmatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
      for j in range(4):
        for k in range(4):
          newmatrix[i][k] += self.matrix[i][j]*other.matrix[j][k]
    return transformation(newmatrix)

  def apply(self, point):
    """Apply this transformation to a coordinate, returning a new coordinate."""
    return coordinate3d(
      self.matrix[0][0]*point.x + self.matrix[0][1]*point.y + self.matrix[0][2]*point.z + self.matrix[0][3],
      self.matrix[1][0]*point.x + self.matrix[1][1]*point.y + self.matrix[1][2]*point.z + self.matrix[1][3],
      self.matrix[2][0]*point.x + self.matrix[2][1]*point.y + self.matrix[2][2]*point.z + self.matrix[2][3])
  
## Shape functions

def cuboid(dx,dy,dz):
  for x in range(dx):
    for y in range(dy):
      for z in range(dz):
        yield coordinate3d(x,y,z)

def floor(dx,dz):
  return cuboid(dx,1,dz)

def hollowcuboid(dx,dy,dz):
  # Iterating through the six faces would be more efficient, but I'm lazy.
  for x in range(dx):
    for y in range(dy):
      for z in range(dz):
        if x==0 or x==(dx-1) or y==0 or y==(dy-1) or z==0 or z==(dz-1):
          yield coordinate3d(x,y,z)

def sphere(r):
  for x in range(-r,r):
    for y in range(-r,r):
      for z in range(-r,r):
        if x**2 + y**2 + z**2 < r**2:
          yield coordinate3d(x,y,z)

def pyramid(h):
  for level in range(h):
    for point in floor(2*(h-level),2*(h-level)):
      yield point + coordinate3d(level,level,level)

def cylinder(r,h):
  for x in range(-int(r),int(r)):
    for z in range(-int(r),int(r)):
      if x**2 + z**2 < r**2:
        for y in range(h):
          yield coordinate3d(x,y,z)

def cone(r,h):
  for level in range(h):
    for point in cylinder((float(h-level)/h)*r,1):
      yield point + coordinate3d(0,level,0)

def line(x0,y0,z0,x1,y1,z1):
  """Draw a line using a 3D adaptation of Bressenham's algorithm.
  http://www.cobrabytes.com/index.php?topic=1150.0"""
  
  # Check for steep xy line
  swap_xy = abs(y1-y0) > abs(x1-x0)
  if swap_xy:
    x0,y0 = y0,x0
    x1,y1 = y1,x1

  # Check for steep xz line
  swap_xz = abs(z1-z0) > abs(x1-x0)
  if swap_xz:
    x0,z0 = z0,x0
    x1,z1 = z1,x1

  # Lengths in each direction
  delta_x = abs(x1-x0)
  delta_y = abs(y1-y0)
  delta_z = abs(z1-z0)

  # Drift tells us when to take a step in a direction
  drift_xy = delta_x/2
  drift_xz = delta_x/2

  # Direction of line
  step_x = 1
  if x0 > x1: step_x = -1
  step_y = 1
  if y0 > y1: step_y = -1
  step_z = 1
  if z0 > z1: step_z = -1

  # Starting point
  y = y0
  z = z0

  for x in range(x0,x1,step_x):
    cx,cy,cz = x,y,z

    # Perform any necessary unswaps
    if swap_xz: cx,cz = cz,cx
    if swap_xy: cx,cy = cy,cx

    # Place a block
    yield coordinate3d(cx,cy,cz)

    # Update progress
    drift_xy -= delta_y
    drift_xz -= delta_z

    # Step in y direction
    if drift_xy < 0:
      y += step_y
      drift_xy += delta_x

    # Step in z direction
    if drift_xz < 0:
      z += step_z
      drift_xz += delta_x
  
  # Final block
  yield coordinate3d(x1,y1,z1)

def text(data):
  # Not implemented yet - create an image from the text, and search for coloured
  # pixels.
  pass

def mengersponge(depth):
  """3D cube-based fractal."""
  if depth == 0:
    yield coordinate3d(0,0,0)
  else:
    scale = 3**(depth-1) # size of each sub-cube
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if not(x==1 and y==1 or x==1 and z==1 or y==1 and z==1):
            for block in mengersponge(depth-1):
              yield block + coordinate3d(x*scale,y*scale,z*scale)
        

def building(width, height, depth):
  """All dimensions are specified in the number of windows."""
  for point in hollowcuboid(width*5-1, height*5+1, depth*5-1):
    # Shift the building down by 1 so the floor is the right height.
    yield point + coordinate3d(0,-1,0)

def revolvingdoor():
  # A couple of shifts we need to get the doors to cross.
  # This does work, but it was a bit too jerky to show off in the video.
  xshift = shift(-2,0,0)
  zshift = shift(0,0,-2)
  for point in cuboid(1,3,5):
    yield zshift*point
  for point in cuboid(5,3,1):
    yield xshift*point

def maze(width, depth):
  """Credit to autophil! http://jsfiddle.net/q7DSY/4/"""
  
  # Ensure width and depth are odd so we get outer walls
  if width%2==0: width += 1
  if depth%2==0: depth += 1
  
  maze.location = (1,1)
  history = []
  
  # Initialise 2d grid: 0 = wall; 1 = passageway.
  grid = [depth*[0] for x in range(width)]  

  grid[maze.location[0]][maze.location[1]] = 1
  history.append(maze.location)

  def randomiseDirections():
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    random.shuffle(directions)
    return directions

  # Work out where to go next - don't want to leave the maze or go somewhere
  # we've already been.
  def nextDirection():
    for direction in randomiseDirections():
      x = maze.location[0] + 2*direction[0]
      z = maze.location[1] + 2*direction[1]
      if 0<x<width and 0<z<depth and grid[x][z]==0:
        return direction

  # Dig two squares or backtrack
  def dig():
    direction = nextDirection()
    if direction:
      for i in range(2):
        maze.location = (maze.location[0] + direction[0], maze.location[1] + direction[1])
        grid[maze.location[0]][maze.location[1]] = 1
      history.append(maze.location)
      return True
    elif history:
      maze.location = history.pop()
      return maze.location
    else:
      return None

  # Keep digging out the maze until we can't dig any more.
  while dig():
    pass

  # Finally, start returning the blocks to draw.
  for x in range(width):
    for z in range(depth):
      if grid[x][z] == 0:
        yield coordinate3d(x,0,z)
        yield coordinate3d(x,1,z)
        yield coordinate3d(x,2,z)
        

arrow = [coordinate3d(0,0,0), coordinate3d(0,1,0), coordinate3d(0,2,0),
         coordinate3d(0,3,0), coordinate3d(0,4,0), coordinate3d(-2,2,0),
         coordinate3d(-1,3,0), coordinate3d(1,3,0), coordinate3d(2,2,0)]

## Fill functions

def solid(material):
  """All one material."""
  def f(point):
    return material
  return f

def randomfill(materials):
  """Choose a random material from those listed. A material may be repeated to
  increase its chance of being chosen."""
  def f(point):
    return random.choice(materials)
  return f

def chequers(material1, material2):
  """Alternate between materials (in all directions)."""
  def f(point):
    if (point.x+point.y+point.z) % 2 == 0:
      return material1
    else:
      return material2
  return f

def officeblock(wallmaterial):
  """Create a repeating pattern of 2x2 windows."""
  def f(point):
    goodx = (point.x%5 == 1) or (point.x%5 == 2)
    goody = (point.y%5 == 1) or (point.y%5 == 2)
    goodz = (point.z%5 == 1) or (point.z%5 == 2)
    if (goodx and goody) or (goodz and goody):
      return mc.GLASS
    else:
      return wallmaterial
  return f

def image(path, w, h):
  """Scale the image to the given size."""
  img = pygame.image.load(path)
  width = img.get_width()
  height = img.get_height()
  scale_x = width/w
  scale_y = height/h

  def f(point):
    x = int(scale_x/2) + scale_x*point.x
    y = height - int(scale_y/2) - scale_y*point.y
    material = None
    # Anti-aliasing means that some pixels are a mix of colours.
    # Keep trying until we get one we can deal with.
    while material == None:
      r,g,b,a = img.get_at((x,y))
      material = tomaterial(r,g,b)
      x += 1
    return material
  return f

def tomaterial(r,g,b):
  # Just a quick hack for now - could of course add more colours
  # and a way of finding the nearest supported colour.
  if (r,g,b) == (255,255,255):  # white
    return mc.AIR
  elif (r,g,b) == (0,0,0):  # black
    return mc.OBSIDIAN
  elif (r,g,b) == (188,17,66):  # pink
    return mc.REDSTONE_ORE
  elif (r,g,b) == (117,169,40):  # green
    return mc.MELON
  else:
    return None

## Transformation functions

def identity():
  return transformation([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,0],
                         [0,0,0,1]])

def shift(x,y,z):
  """Move by a given offset."""
  return transformation([[1,0,0,x],
                         [0,1,0,y],
                         [0,0,1,z],
                         [0,0,0,1]])

def rotationx(angle):
  """Rotate about the x axis by the given number of degrees."""
  angle = radians(angle)
  return transformation([[1,           0,          0, 0],
                         [0,  cos(angle), sin(angle), 0],
                         [0, -sin(angle), cos(angle), 0],
                         [0,           0,          0, 1]])

def rotationy(angle):
  """Rotate about the y axis by the given number of degrees."""
  angle = radians(angle)
  return transformation([[ cos(angle), 0, sin(angle), 0],
                         [          0, 1,          0, 0],
                         [-sin(angle), 0, cos(angle), 0],
                         [          0, 0,          0, 1]])

def rotationz(angle):
  """Rotate about the z axis by the given number of degrees."""
  angle = radians(angle)
  return transformation([[ cos(angle), sin(angle), 0, 0],
                         [-sin(angle), cos(angle), 0, 0],
                         [          0,          0, 1, 0],
                         [          0,          0, 0, 1]])

## Other functions

def fillshape(shape, transform=identity(), material=None,fillfunc=None):
  """Build a shape in the Minecraft world.
  shape must be iterable: it can be a list, tuple, etc., or a generator function.
  transform is of type transformation - multiple transformations can be combined
by multiplying them together.
  material or fillfunc specify which material(s) to build the shape out of."""
  if fillfunc == None:
    fillfunc = solid(material)
  for point in shape:
    point2 = transform * point
    mc.setblock(int(point2.x), int(point2.y), int(point2.z), fillfunc(point))

def clear(shape, transform=identity()):
  """Remove any non-air blocks in the given shape."""
  fillshape(shape,transform,mc.AIR)

def main():
  """Function used to build my demo world. Extra clearing may be required for
hilly worlds."""
  mc.connect(server.address)
  
  # Create a large empty space with a neat, grassy floor. Takes a long time!
  clear(cuboid(100,10,120))
  fillshape(floor(100,120), shift(0,-1,0), material=mc.GRASS)

  # Introduce basic shapes/transformations/fill functions.
  fillshape(arrow, material=mc.STONE)
  fillshape(arrow, shift(6,0,0), mc.STONE)
  fillshape(arrow, shift(12,0,0)*rotationx(90), mc.STONE)
  fillshape(arrow, shift(18,0,0)*rotationx(45), mc.STONE)
  fillshape(arrow, shift(24,0,0), fillfunc=chequers(mc.WOOD, mc.STONE))

  # Introduce generator functions.
  fillshape(cuboid(4,4,4), shift(30,0,0), mc.STONE)
  fillshape(cuboid(3,8,2), shift(36,0,0), mc.STONE)

  # Show other simple shapes.
  fillshape(sphere(5), shift(45,5,0), mc.STONE)
  fillshape(pyramid(5), shift(50,0,0), mc.STONE)
  fillshape(cylinder(5,4), shift(65,0,0), mc.STONE)
  fillshape(cone(5,5), shift(75,0,0), mc.STONE)
  
  # Show some fill functions.
  fillshape(cuboid(4,4,4), shift(80,0,5), fillfunc=chequers(mc.GOLD, mc.IRON))
  fillshape(pyramid(5), shift(80,0,10), fillfunc=randomfill([mc.SAND, mc.SANDSTONE]))
  fillshape(hollowcuboid(4,6,4), shift(80,0,22), mc.WOOD_PLANK)
  fillshape(building(2,6,2), shift(80,0,30), fillfunc=officeblock(mc.COBBLESTONE))

  # Line drawing.
  fillshape(line(80,0,40,85,5,45), material=mc.WOOL)
  fillshape(line(80,0,40,80,2,50), material=mc.WOOL)
  fillshape(line(80,2,50,85,5,45), material=mc.WOOL)
  
  # Fun lava sphere.
  fillshape(sphere(10), shift(80,10,60), mc.GLASS)
  fillshape(sphere(9), shift(80,10,60), mc.LAVA)

  # Fractals - far easier to code than to build by hand.
  fillshape(mengersponge(0), shift(70,0,75), mc.IRON)
  fillshape(mengersponge(1), shift(66,0,75), mc.IRON)
  fillshape(mengersponge(2), shift(56,0,75), mc.IRON)
  fillshape(mengersponge(3), shift(28,0,75), mc.IRON)

  # Maze.
  fillshape(maze(25,25), shift(0,0,75), mc.STONE)

  # Picture - can use the same technique to draw text.
#  fillshape(cuboid(24,30,1), shift(0,0,30), fillfunc=image("pi.png",24,30))



if __name__ == "__main__":
  main()