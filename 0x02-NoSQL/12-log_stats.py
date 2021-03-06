#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    print(logs.count_documents({}), 'logs')
    print('Methods:')
    method = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for req in method:
        print(f'\tmethod {req}:', logs.count_documents({'method': req}))
    print(logs.count_documents(
        {'method': 'GET', 'path': '/status'}), 'status check')
