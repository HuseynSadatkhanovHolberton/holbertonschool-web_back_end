#!/usr/bin/env python3
"""Module for updating the topics of school documents."""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of all school documents with the given name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): The new list of topics.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
