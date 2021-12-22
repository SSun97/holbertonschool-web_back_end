#!/usr/bin/env python3
""" Write a Python function that returns the 
list of school having a specific topic: """


def schools_by_topic(mongo_collection, topic):
    """Returns a list of dictionaries that return a topic"""
    return [doc for doc in mongo_collection.find({'topic': topic})]
