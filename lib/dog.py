#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed=None):
        self.name = name
        if breed:
            self.breed = breed
        else:
            self.breed = "Mutt"