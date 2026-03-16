import math
class Vec3:
    def __init__(self,x=0,y=0,z=0): self.x=x;self.y=y;self.z=z
    def __add__(s,o): return Vec3(s.x+o.x,s.y+o.y,s.z+o.z)
    def __sub__(s,o): return Vec3(s.x-o.x,s.y-o.y,s.z-o.z)
    def __mul__(s,t): return Vec3(s.x*t,s.y*t,s.z*t)
    def dot(s,o): return s.x*o.x+s.y*o.y+s.z*o.z
    def mag(s): return math.sqrt(s.dot(s))
    def norm(s): m=s.mag(); return Vec3(s.x/m,s.y/m,s.z/m) if m else Vec3()
class Sphere:
    def __init__(self,center,radius,color):
        self.c=center;self.r=radius;self.color=color
    def intersect(self,origin,direction):
        oc=origin-self.c; a=direction.dot(direction); b=2*oc.dot(direction); c=oc.dot(oc)-self.r**2
        disc=b*b-4*a*c
        if disc<0: return None
        t=(-b-math.sqrt(disc))/(2*a)
        return t if t>0.001 else None
def trace(origin,direction,spheres,light):
    closest=None; min_t=float('inf')
    for s in spheres:
        t=s.intersect(origin,direction)
        if t and t<min_t: min_t=t; closest=s
    if not closest: return (0,0,0)
    hit=origin+direction*min_t; normal=(hit-closest.c).norm()
    to_light=(light-hit).norm(); intensity=max(0,normal.dot(to_light))
    return tuple(min(255,int(c*intensity)) for c in closest.color)
def render(w,h):
    spheres=[Sphere(Vec3(0,0,5),1,(255,0,0)),Sphere(Vec3(2,0,6),1,(0,255,0)),Sphere(Vec3(-2,0,4),0.5,(0,0,255))]
    light=Vec3(5,5,0); pixels=[]
    for y in range(h):
        row=[]
        for x in range(w):
            dx=(x-w/2)/w; dy=(h/2-y)/h
            direction=Vec3(dx,dy,1).norm()
            row.append(trace(Vec3(),direction,spheres,light))
        pixels.append(row)
    return pixels
if __name__=="__main__":
    img=render(20,10)
    non_black=sum(1 for row in img for p in row if p!=(0,0,0))
    print(f"Ray traced 20x10: {non_black} non-black pixels")
    assert non_black>5
    print("All tests passed!")
