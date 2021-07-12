#Create a module lengthconversion.py that stores functions for various lengths conversion.

#lengthConversion.py
"""Conversion functions between miles and kilometers"""
"""Conversion functions between inches and feet"""

#Constants
oneMileInKm = 1.609344
oneFeetInInchs = 12

#Functions

def milesToKM(distance):
    """Returns: distance converted to KM"""
    return distance * oneMileInKm


def kmToMiles(distance):
    """Returns: distance converted to Miles"""
    return distance / oneMileInKm


def feetToInches(measure):
    """Returns: measure converted to Inches"""
    return measure * oneFeetInInchs


def inchesToFeet(measure):
    """Returns: measure converted to Feet"""
    return measure / oneFeetInInchs

