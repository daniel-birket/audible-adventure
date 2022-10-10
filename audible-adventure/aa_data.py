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
    keyword_dict = dict()  #: Intern all Keywords in the class's dictionary
    synonym_xref = dict()  #: Cross-reference synonyms to keywords

    # Static methods

    @staticmethod
    def normalize_word(word: str) -> str:
        """Remove leading/trailing spaces and make lowercase."""
        return (word.strip().lower())

    # Class methods

    @classmethod
    def is_keyword(cls, word: str) -> bool:
        """Is word a keyword?"""
        return (word in cls.keyword_dict)

    @classmethod
    def is_synonym(cls, word: str) -> bool:
        """Is word a synonym?"""
        return (word in cls.synonym_xref)

    @classmethod
    def get_keyword(cls, word: str) -> str:
        """Return keyword cooresponding to synonym
        or None if word is not a synonym"""
        return (cls.synonym_xref).get(word, None)

    @classmethod
    def refresh_xref(cls) -> None:
        """Refresh the synonym_xref from the keyword_dict."""
        cls.synonym_xref = dict()  # Erase the old xref
        for keyw in cls.keyword_dict:
            cls.xref_keyword(keyw, cls.keyword_dict[keyw].synonyms)

    @classmethod
    def yaml_load_file(cls, filename: str) -> None:
        """Load keywords from a YAML file."""
        with open(filename, 'r') as keyword_doc:
            cls.keyword_dict = yaml.load(keyword_doc, Loader=yaml.SafeLoader)
            cls.refresh_xref()

    @classmethod
    def yaml_dump_file(cls, filename: str) -> None:
        """Dump keywords to a YAML file."""
        with open(filename, 'w') as keyword_doc:
            keyword_doc.write('---\n')
            yaml.dump(cls.keyword_dict, keyword_doc)
            keyword_doc.write('...\n')

    # Instance methods

    def intern_keyword(self, keyw: str):
        """Intern the keyword and its synonyms in the keyword dictionary."""
        cls = type(self)  #: class of self, to access class vars

        if cls.is_keyword(keyw):  # duplicate keyword?
            old_syn = cls.keyword_dict[keyw].synonyms
            new_syn = list(set(old_syn.extend(self.synonyms)))
            cls.keyword_dict[keyw].synonyms = new_syn
        else:
            cls.keyword_dict[keyw] = self  # Intern Keyword object

    def xref_keyword(self, keyw: str):
        """Add the keyword's synonyms to the cross-reference"""
        cls = type(self)  #: class of self, to access class vars

        cls.synonym_xref[keyw] = keyw  # keyword is its own synonym
        for syn in self.synonyms:
            if cls.is_synonym(syn):  # duplicate synonym?
                print(
                    f"Warning: synonym '{syn}' "
                    f"in keyword '{cls.synonym_xref[syn]}' "
                    f"overwritten by keyword '{keyw}'.\n"
                )
            cls.synonym_xref[syn] = keyw

    def __init__(self, keyword: str, synonyms: list):
        """Initialize the Keyword class instance attributes,
        intern the new keyword in the class's 'keywords' dictionary and
        crossreference its synonyms in the class's 'synonyms' dictionary.

        'synonyms' is a list of unique words."""

        keyw = Keyword.normalize_word(keyword)  # Normalize the word
        self.synonyms = [Keyword.normalize_word(s) for s in synonyms]
        self.synonyms = list(set(self.synonyms))  #: list of unique synonyms

        self.intern_keyword(keyw)  # add to the keyword dictionary
        self.xref_keyword(keyw)  # add to the crossreference

    def __repr__(self) -> str:
        """Create a python representation of the instance."""
        return (
            f"{type(self).__name__}("
            f"synonyms = {self.synonyms!r})"
        )

    def __str__(self) -> str:
        """Create a string of the keywords synonyms"""
        return (' '.join(self.synonyms))


def main() -> int:
    """TBD main routine returns an integer shell exit code. 0 = ok"""

    print("in main()")
    return 0


# Execute this module as a script
if __name__ == '__main__':
    sys.exit(main())
