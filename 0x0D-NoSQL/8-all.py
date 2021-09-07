#!/usr/bin/env python3

from pymongo import MongoClient
import pprint


def list_all(mongo_collection):
    """"""
    document = mongo_collection.find()

    if not document:
        return []
    return document
