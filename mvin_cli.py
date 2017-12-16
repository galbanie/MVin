from clize import run
from mvin import *

VERSION = "0.1"


def decode(*vin):
    """
    Decode Mercedes Vin

    :param vin:
    :return:
    """
    return vin


def get(mfr, year):
    """
    Get Vin Mercedes

    :param mfr:
    :param year:
    :return:
    """
    return mfr + year


def version(): return "MVin version {0}".format(VERSION)


if __name__ == '__main__':
    run(decode, get, alt={
        "version": version
    })
