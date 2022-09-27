#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Class Module to describe a scene of the game"""

import yaml


class Scene(yaml.YAMLObject):
    """Describe a scene of the game: a place or a state, like 'dead'."""
    yaml_tag = "!Scene"  #: Use class name as YAML type
    yaml_loader = yaml.loader.SafeLoader  #: This type is safe to load
    dictionary = dict()  #: Keep all Scenes in the class's dictionary

    def __init__(self, key, description, summary, ambient, audio):
        """Initialize the Scene class instance attributes."""
        self.description = description  #: Text description of scene.
        self.summary = summary  #: Text summary of scene, or empty.
        self.ambient = ambient  #: Filename of ambient sound, or empty.
        self.audio = audio  #: Filename of audio scene description, or empty.
        self.dictionary[key] = self  # intern the Scene in the dictionary

    def __repr__(self):
        """Create a python reprensentation of the instance."""
        return (
            f"{self.__class__.__name__}("
            f"description={self.description!r}, "
            f"summary={self.summary!r}, "
            f"ambient={self.ambient!r}, "
            f"audio={self.audio!r})"
        )
