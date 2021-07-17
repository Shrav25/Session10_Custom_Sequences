# session-10-assignment-Shrav25
session-10-assignment-Shrav25 created by GitHub Classroom

####
Name - Shravan C R

####
Email - shravan.ramakrishna@gmail.com

A regular strictly convex polygon is a polygon that has the following characteristics:
all interior angles are less than 180 degree.
all sides have equal length.

For a regular strictly convex polygon with:
n edges (=n vertices)
R circumradius
interiorAngle=(n−2)⋅180/n
edgeLength,s=2*R*Sin(pi/n)
apothem,a=R*Cos(pi/n)
area=1/2 * n * s * a
perimeter=n*s

Objective 1
Create a Polygon Class:
A. Where initializer takes in:
	1. number of edges/vertices
	2. circumradius
B. That can provide these properties:
	1. Number of edges
	2.	Number of vertices
	3.	Interior angle
	4. Edge length
	5.	Apothem
	6.	Area
	7.	Perimeter
That has these functionalities:
	1. A proper __repr__ function
	2. Implements equality (==) based on # vertices and circumradius (__eq__)
	3. Implements > based on number of vertices only (__gt__)


repr() compute the “official” string representation of an object (a representation that has all information about the object) and str() is used to compute the “informal” string representation of an object (a representation that is useful for printing the object).

__getitem__()The method __getitem__(self, key) defines behavior for when an item is accessed, using the notation self[key] . This is also part of both the mutable and immutable container protocols. Unlike some other languages, Python basically lets you pass any object into the indexer

__eq__Checks equal to between two objects. Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class. By default, Python uses the is operator if you don't provide a specific implementation for the __eq__ method.

__len__()Called to implement the built-in function len(). Should return the length of the object, an integer >= 0. Also, an object that doesn’t define a __bool__() method and whose __len__() method returns zero is considered to be false in a Boolean context.

Objective 2

Implement a Custom Polygon sequence type:
where initializer takes in:
	1. Number of vertices for largest polygon in the sequence
	2. Common circumradius for all polygons that can provide these properties:
		a.max efficiency polygon: returns the Polygon with the highest area: perimeter ratio that has these functionalities:
		b.functions as a sequence type (__getitem__)
		c. supports the len() function (__len__)
		d. has a proper representation (__repr__)
