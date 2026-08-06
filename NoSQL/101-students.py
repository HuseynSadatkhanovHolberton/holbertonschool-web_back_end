#!/usr/bin/env python3
"""Module for listing students sorted by average score."""


def top_students(mongo_collection):
    """Return all students sorted by their average score."""
    students = mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])

    return list(students)
