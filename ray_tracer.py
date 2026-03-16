#!/usr/bin/env python3
"""Basic ray tracer with spheres and lighting."""
import math
class Vec3:
    def __init__(self,x,y,z):self.x=x;self.y=y;self.z=z
    def dot(self,o):return self.x*o.x+self.y*o.y+self.z*o.z
    def sub(self,o):return Vec3(self.x-o.x,self.y-o.y,self.z-o.z)
    def length(self):return math.sqrt(self.dot(self))
class Ray:
    def __init__(self,origin,direction):self.origin=Vec3(*origin);self.dir=Vec3(*direction)
class Sphere:
    def __init__(self,center,radius,color):self.center=Vec3(*center);self.r=radius;self.color=color
    def intersect(self,ray):
        oc=ray.origin.sub(self.center);a=ray.dir.dot(ray.dir);b=2*oc.dot(ray.dir);c=oc.dot(oc)-self.r*self.r
        d=b*b-4*a*c
        if d<0:return None
        return(-b-math.sqrt(d))/(2*a)
