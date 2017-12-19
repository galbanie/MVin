import os
from clize import run
from mvin import *
from pprint import pprint

VERSION = "0.1"

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()


# print(cwd)

# Change directory
# os.chdir("/path/to/your/folder")

# List all files and directories in current directory
# os.listdir('.')


def decode(*vin):
    """
    Decode Mercedes Vin

    :param vin:
    :return:
    """
    return vin


def get(**params):
    """
    Get Vin Mercedes

    :param mfr:
    :param year:
    :return:
    """
    return pprint(params)


def populate(json_file):
    """
    Populate Database with excel file

    :param json_file:
    :return:
    """
    return


def generate():
    """
    Generate json file for help user to config

    :return:
    """
    return


def version(): return "MVin version {0}".format(VERSION)


if __name__ == '__main__':
    run(
        decode,
        get,
        populate,
        generate,
        alt={
            "version": version
        }
    )
