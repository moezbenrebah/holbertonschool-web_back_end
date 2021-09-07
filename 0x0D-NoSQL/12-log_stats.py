#!/usr/bin/env python3
"""Nginx logs in MongoDB module"""

from pymongo import MongoClient


def log_infos():
    """print nginx logs in mongodb"""

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nglogs = client.logs.nginx

     print(
        "{} logs".format(
            nglogs.count_documents({})
        )
    )

    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method, nglogs.count_documents({'method': method})
            )
        )

    print(
        "{} status check".format(
            nglogs.count_documents({'method': 'GET', 'path': '/status'})
        )
    )


if __name__ == '__main__':
    log_infos()
