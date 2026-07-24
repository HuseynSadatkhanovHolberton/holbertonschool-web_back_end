#!/usr/bin/env python3
"""Module for inserting a document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The fields of the document to insert.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
