#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Game data classes for audible adventure."""

import sys
import yaml

class Keyword(yaml.YAMLObject):
    """Assocate a list of synonyms with keywords."""
    yaml_tag = "!Keyword"  #: Use class name as YAML type
    yaml_loader = yaml.loader.SafeLoader  #: This type is safe to load
    keywords = dict()  #: Intern all Keywords in the class's dictionary
    synonyms = dict()  #: Cross-reference synonyms to keywords

    def __init__(self, keyword, synonyms):
        """Initialize the Keyword class instance attributes
        and intern the new instance in the class dictionary."""
        self.synonyms = synonyms  #: List of synonyms of keyword
        if keyword in type(self).keywords:
            type(self).keywords[keyword].update(synonyms)  # update set
        else:
            type(self).keywords[keyword] = set(synonyms)  # Intern the Keywords

    def __repr__(self) -> str:
        """Create a python representation of the instance."""
        return (
            f"{type(self).__name__}("
            f"synonyms={self.synonyms!r})"
        )

    @classmethod
    def make_xref(cls) -> None:
        """Make the synonyms dictionary from the keywords dictionary."""
        for keyword in cls.keywords:
            cls.synonyms[keyword] = keyword
            for synonym in cls.keywords[keyword]:
                if synonym in cls.synonyms:
                    print(
                        f"Warning: Synonym '{synonym}' "
                        f"overwriting keyword '{cls.synonyms[synonym]}'.'"
                        f"with keyword '{keyword}'\n"
                    )
                cls.synonyms[synonym] = keyword


def main() -> int:
    """TBD main routine returns an integer shell exit code. 0 = ok"""

    print("in main()")
    return 0


# Execute this module as a script
if __name__ == '__main__':
    sys.exit(main())
