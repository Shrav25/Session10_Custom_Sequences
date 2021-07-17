#!/usr/bin/env python
# coding: utf-8

# In[57]:


from math import sin, cos, pi

class Polygon:
    
    '''This is a Polygon class which takes in number of edges and circumradius
    as input and gives out the other calculations for Polygon'''
    
    def __init__(self, edge:'int',circumradius:'int'):
        
        '''This is intiation function, which takes in two parameters'''
        #Params
        #Takes number of edges and the value of circumradius
        
        self.edge = edge
        self.circumradius = circumradius
        
    def __repr__(self):
        
        '''This is a special function which is a special method
        used to represent class object as string'''
        
        return (f'Polygon has {self.edge} sides and has Circumradius of {self.circumradius}')
    
    
    def interior_angle(self):
        
        '''This function calculates the interior angle of a Polygon
        The thumb rule is that the angle should not be more than 180deg'''
        
        #Params:
        #edge value
        
        int_ang = ((self.edge - 2) * (180/self.edge))
        return (f'The interior angle of the Polygon is: {int(int_ang)} deg')
    
    
    def edgelength(self):
        
        '''Using Circumradius as input parameter, edge lenght is calculated '''
        #params
        #Circumradius

        return (f'The Edgelength of the Polygon is: {int(2*self.circumradius*sin(pi/self.edge))}')
    
   
    def apothem(self):
        
        '''The defination of Apothem - 
        The apothem of a regular polygon is a line segment 
        from the center to the midpoint of one of its sides.'''
        
        #Params
        #Circumradius and Edge
        
        return (f'The Apothem of the Polygon is: {int((self.circumradius) * cos(pi/self.edge))}')
    
    
    def area(self):
        
        '''Calculates the area of the Polygon using the regular Formula
        '''
        apothem = (self.circumradius) * cos(pi/self.edge)
        edgelength = 2*self.circumradius*sin(pi/self.edge)
        area = (0.5 * self.edge * apothem * edgelength)
        return (f'The area of the Polygon is: {int(area)}sq meters')
    
   
    def perimeter(self):
        
        '''Calculates the Perimeter of the Polygon using the regular Formula
        '''
        edgelength = 2*self.circumradius*sin(pi/self.edge)
        perimeter = self.edge * edgelength
        return(f'The perimeter of the Polygon is: {int(perimeter)}meters')
    
    def __eq__(self, other):
        """
        This class is to check equality. It checks the self.edges and self.circumradius with the ones
        of the other passed in as argument
        """
        if not isinstance(other,Polygon):
            raise ValueError('Polygons must be compared with polygons and not with something else')
        return ((self.edge == other.edge) and (self.circumradius == other.circumradius))

    def __gt__(self, other):
        """
        This class is to check greater than. It checks the self.edges and self.circumradius with the ones
        of the other passed in as argument
        """
        if not isinstance(other,Polygon):
            raise ValueError('Polygons must be compared with polygons and not with something else')
        return self.edge > other.edge


# In[65]:


print(f"No of Vertices: {p1.edge},\nLength of Circumradius: {p1.circumradius},\nInterior Angle: {p1.interior_angle()},\nApothem: {p1.apothem()},\nArea: {p1.area()},\nPerimeter: {p1.perimeter()}")


# In[61]:


p2 = Polygon(5,10)
print(p1.__eq__(p2),p1==p2)
print(p1.__gt__(p2),p1>p2)
print(p2.__gt__(p1),p2>p1)


# In[62]:



p2 = Polygon(4,10)
print(p1.__eq__(p2),p1==p2)
print(p1.__gt__(p2),p1>p2)
print(p2.__gt__(p1),p2>p1)


# In[63]:


p2 = Polygon(3,10)
print(p1.__eq__(p2),p1==p2)
print(p1.__gt__(p2),p1>p2)
print(p2.__gt__(p1),p2>p1)


# In[ ]:




