#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Game data classes for audible adventure."""

import sys
import yaml

class Keyword(yaml.YAMLObject):
    """Assocate a list of synonyms with keywords."""

    # Class variables

    yaml_tag = "!Keyword"  #: Use class name as YAML type
    yaml_loader = yaml.loader.SafeLoader  #: This type is safe to load
    keywords = dict()  #: Intern all Keywords in the class's dictionary
    synonyms = dict()  #: Cross-reference synonyms to keywords

    # Class methods

    @classmethod
    def is_keyword(cls, word: str) -> bool:
        """Is word a keyword?"""
        return (word in cls.keywords)

    @classmethod
    def is_synonym(cls, word: str) -> bool:
        """Is word a synonym?"""
        return (word in cls.synonyms)

    @classmethod
    def get_keyword(cls, word: str) -> str:
        """Return keyword cooresponding to synonym
        or None if word is not a synonym"""
        return (cls.synonyms).get(word, None)

    # Instance methods

    def __init__(self, keyword: str, synonyms: str):
        """Initialize the Keyword class instance attributes,
        intern the new keyword in the class's 'keywords' dictionary and
        crossreference its synonyms in the class's 'synonyms' dictionary."""
        cls = type(self)  #: class of self, to access class dicts
        keyword = keyword.strip()  # Clean up the keyword
        self.synonyms = set(synonyms.split(' '))  #: Set of unique synonyms

        if cls.is_keyword(keyword):  # have we seen this keyword before?
            cls.keywords[keyword].synonyms.update(self.synonyms)  # update it
        else:
            cls.keywords[keyword] = self  # Intern set of synonyms

        cls.synonyms[keyword] = keyword  # a keyword is its own synonym

        for synonym in cls.keywords[keyword]:
            if cls.is_synonym(synonym):
                print(
                    f"Warning: Synonym '{synonym}' "
                    f"overwrites keyword '{cls.synonyms[synonym]}' "
                    f"with keyword '{keyword}'.\n"
                )
            cls.synonyms[synonym] = keyword

    def __repr__(self) -> str:
        """Create a python representation of the instance."""
        return (
            f"{type(self).__name__}("
            f"synonyms={self.synonyms!r})"
        )


def main() -> int:
    """TBD main routine returns an integer shell exit code. 0 = ok"""

    print("in main()")
    return 0


# Execute this module as a script
if __name__ == '__main__':
    sys.exit(main())
