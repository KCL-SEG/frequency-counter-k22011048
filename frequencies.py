"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections

def frequencies(items):
    frequencies = {}
    itemList = []
    for i in items:
        i=str(i)
        itemList.append(i)
    counter = collections.Counter(itemList)
    frequencies = dict(counter)
    return frequencies
