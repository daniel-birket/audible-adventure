#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Sandbox toy to try writing YAML data."""

import sys
import yaml
from scene import Scene


def main() -> int:
    """do main program and return an integer exit code. 0 = ok"""
    Scene("01.EndRoad",
          "You are standing at the end of a road before a small brick "
          "building.  Around you is a forest.  A small stream flows out "
          "of the building and down a gully.",
          "at end of road.",
          "", "")
    Scene("02.HillRoad",
          "You have walked up a hill, still in the forest.  The road "
          "now slopes back down the other side of the hill.  There is a "
          "building in the distance.",
          "at hill in road.",
          "", "")
    Scene("03.WellHouse",
          "You are inside a building, a well house for a large spring.",
          "inside building.",
          "", "")
    Scene("04.ValleyStream",
          "You are in a valley in the forest beside a stream tumbling "
          "along a rocky bed.",
          "in a valley.",
          "", "")
    Scene("05.ForestValley",
          "You are in open forest, with a deep valley to one side.",
          "in the forest",
          "", "")
    Scene("06.ForestValleyRoad",
          "You are in open forest near both a valley and a road.",
          "in the forest",
          "", "")
    Scene("07.SlitStream",
          "At your feet all the water of the stream splashes into a "
          "2 inch slit in the rock. Downstream the streambed is bare rock.",
          "at slit in streambed",
          "", "")
    Scene("08.OutsideGrate",
          "You are in a 20 foot depression floored with bare dirt. Set into "
          "the dirt is a strong steel grate mounted in concrete. A dry "
          "streambed leads into the depression.",
          "outside the grate.",
          "", "")
    Scene("09.BelowGrate",
          "You are in a small chamber beneath a 3x3 steel grate to the "
          "surface. A low crawl over cobbles leads inward to the west.",
          "below the grate.",
          "", "")
    Scene("10.CobbleCrawl",
          "You are crawling over cobbles in a low passage. There is a "
          "dim light at the east end of the passage.",
          "in cobble crawl.",
          "", "")

    print(Scene.dictionary)

    with open('Scenes.yaml', 'w') as scene_doc:
        yaml.dump(Scene.dictionary, scene_doc)

    return 0


# Execute this script
if __name__ == '__main__':
    sys.exit(main())
