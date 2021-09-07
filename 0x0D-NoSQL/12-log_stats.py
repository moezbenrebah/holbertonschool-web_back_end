#!/usr/bin/env python3
"""Nginx logs in MongoDB module"""

from pymongo import MongoClient


def log_infos() -> None:
    """print nginx logs in mongodb"""

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nglogs = client.logs.nginx

    print(f'{nglogs.count_documents({})} logs')

    print("Methods:")

    for method in methods:
        print(f'\tmethod {method}:
              {nglogs.count_documents({"method": method})}')

    print(f'{nglogs.count_documents({"method": "GET",
                                     "path": "/status"})} status check')


if __name__ == '__main__':
    log_infos()
