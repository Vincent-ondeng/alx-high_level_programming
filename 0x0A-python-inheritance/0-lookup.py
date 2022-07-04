#!/usr/bin/python3
"""Defines an objects attribute lookup function."""


def lookup(obj):
    """Return a list of an objects available attributes."""
    return (dir(obj))
