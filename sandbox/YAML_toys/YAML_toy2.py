#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Sandbox toy to try reading YAML data."""

import sys
import yaml
from scene import Scene


def main() -> int:
    with open('Scenes.yaml', 'r') as scene_doc:
        Scene.dictionary = yaml.load(scene_doc, Loader=yaml.SafeLoader)

        print(Scene.dictionary)

    return 0


# Execute this script
if __name__ == '__main__':
    sys.exit(main())
