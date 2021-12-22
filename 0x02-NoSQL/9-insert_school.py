#!/usr/bin/env python3
""" insert a new document to a collection """


def insert_school(mongo_collection, **kwargs):
    """ insert a new document to a collection """
    return mongo_collection.insert_one(kwargs).inserted_id
