""" This file is for  Inheritance """
class One:
    '''class Three'''
    def one(self):
        '''class Three'''
        print('C class m1 method')

class Two(One):
    """class Five"""
    def one(self):
        '''method-one'''
        super(Two, self).one()
        print("method overiding form one to two class")

OBJ = Two()
OBJ.one()
