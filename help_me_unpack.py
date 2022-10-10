#!/usr/bin/env python3

import base64
import struct

from utils import hackattic


def run():
    problem = hackattic.Problem("help_me_unpack")

    data = problem.fetch()

    print(type(data))
    print("\n")
    print(data)


if __name__ == '__main__':
    run()
