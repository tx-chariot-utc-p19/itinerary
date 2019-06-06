#!/bin/sh
pip3 install networkx matplotlib
DEBIAN_FRONTEND=noninteractive \
        apt-get install \
                -o Dpkg::Options::="--force-confnew" \
                --force-yes \
                -fuy \
		python3-tk
