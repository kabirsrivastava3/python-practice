#Create a module MassConversion.py that stores function for mass conversion.

#massConversion.py
"""Conversion functions between kg and tonnes"""
"""Conversion functions between kg and pound"""

#Constants
oneKgInTonne = 0.001
oneKgInPound = 2.20462


#Functions

def kgToTonnes(weight):
    """Returns: weight converted to Tonnes"""
    return weight * oneKgInTonne


def tonnesToKG(weight):
    """Returns: weight converted to KG"""
    return weight / oneKgInTonne


def kgToPound(weight):
    """Returns: weight converted to Pound"""
    return weight * oneKgInPound


def poundToKg(weight):
    """Returns: weight converted to KG"""
    return weight / oneKgInPound