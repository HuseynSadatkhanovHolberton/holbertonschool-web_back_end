#!/usr/bin/env python3
"""Module that lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """
    List all documents in a collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of all documents in the collection.
        Returns an empty list if the collection is empty.
    """
    return list(mongo_collection.find())
