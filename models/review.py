#!/usr/bin/python
""" class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the Review """
    place_id = ""
    user_id = ""
    text = ""
