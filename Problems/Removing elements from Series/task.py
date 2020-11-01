import pandas as pd


def drop_record(olympics):
    olympics.drop(labels=2020, inplace=True)
    return olympics
