# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isoceles','4,4,5 is a Isoceles triangle')

    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(5,4,4),'Isoceles','5,4,4 is a Isoceles triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(6,2,5),'Scalene','6,2,5 is a Scalene triangle')

    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(6,2,180),'NotATriangle','6,2,180 is NotATriangle')

    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(6,0,5),'InvalidInput','6,0,5 is a InvalidInput triangle')    

    def testInvalidTriangleC(self): 
        self.assertEqual(classifyTriangle(6.2,2,6),'InvalidInput','6.2,2,6 is a InvalidInput triangle')

    def testInvalidTriangleD(self): 
        self.assertEqual(classifyTriangle(1,2,210),'InvalidInput','Input should be less than 200')

    def testInvalidTriangleE(self): 
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','Input should be int')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

