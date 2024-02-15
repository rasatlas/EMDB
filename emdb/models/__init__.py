#!/usr/bin/python3
""" Create an instance of StoregeEngine and import all modesls,
    so, database is ready at system startup.
"""

from models.engine.storageengine import StorageEngine


storage = StorageEngine()
storage.reload()
