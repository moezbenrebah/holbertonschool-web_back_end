#!/usr/bin/env python3
"""matches document based on attribute values"""


def schools_by_topic(mongo_collection, topic):
    """retrieve each document that contain a specific attribute value"""
    if mongo_collection:
        return mongo_collection.find({ "topics": topic })
