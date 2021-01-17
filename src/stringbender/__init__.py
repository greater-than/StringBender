from __future__ import annotations

import re
from typing import Callable, List, Tuple

DEFAULT_DELIMITERS: List[str] = [" ", ".", "-", "_", ":", "\\"]


class String(str):
    """
    Extends str
    """

    def __words__(self, delimiters: List[str] = DEFAULT_DELIMITERS, split_on_first_upper: bool = True) -> List[String]:
        """[summary]

        Args:
            delimiters (List[str], optional): [description]. Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): [description]. Defaults to True.

        Returns:
            :
        """

        if split_on_first_upper:
            s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", self)
            self = String(re.sub("([a-z0-9])([A-Z])", r"\1_\2", s))

        return [String(w) for w in re.split(String.__regex_delimiters(delimiters), self)]

    @staticmethod
    def __escape_delimiters(delimiters: List[str] = DEFAULT_DELIMITERS) -> List[str]:
        return [delim if delim not in "[](){}*+?|^$.\\" else "\\" + delim for delim in delimiters]

    @staticmethod
    def __regex_delimiters(delimiters: List[str] = DEFAULT_DELIMITERS) -> str:
        return "|".join(String.__escape_delimiters(delimiters))

    @staticmethod
    def build(words: List[String],
              delimiter: str = "",
              word_modifier: Callable = None,
              first_word: str = "",
              last_word: str = "",
              replace_chars: Tuple[str, str] = None,
              strip_chars: str = "") -> String:
        """
        Constructs a string based on the specified words

        Args:
            words (List[str]): A list of str
            delimiter (str, optional): [description]. Defaults to "".
            word_modifier (Callable, optional): [description]. Defaults to None.
            first_word (str, optional): [description]. Defaults to "".
            last_word (str, optional): [description]. Defaults to "".

        Returns:
            String: [description]
        """
        s = first_word + delimiter.join(word_modifier(w) if word_modifier else w for w in words) + last_word
        if replace_chars:
            s = s.replace(replace_chars[0], replace_chars[1])
        if strip_chars:
            s = s.strip(strip_chars)
        return String(s)

    def camel(self,
              delimiters: List[str] = DEFAULT_DELIMITERS,
              split_on_first_upper: bool = False) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): [description]. Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): [description]. Defaults to False.

        Returns:
            String: [description]
        """
        words = self.__words__(delimiters, split_on_first_upper)
        return String.build(
            words=words[1:],
            word_modifier=str.title,
            first_word=words[0],
            replace_chars=(" ", "")
        )

    def kebob(self,
              delimiters: List[str] = DEFAULT_DELIMITERS,
              split_on_first_upper: bool = False,
              title_case: bool = False) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): [description]. Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): [description]. Defaults to False.
            title_case (bool, optional): [description]. Defaults to False.

        Returns:
            String: [description]
        """
        return String.build(
            words=self.__words__(delimiters, split_on_first_upper),
            delimiter="-",
            word_modifier=str.title if title_case else str.lower,
            replace_chars=(" ", "-"),
            strip_chars="-"
        )

    def pascal(self,
               delimiters: List[str] = DEFAULT_DELIMITERS,
               split_on_first_upper: bool = True) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): [description]. Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): [description]. Defaults to True.

        Returns:
            String: [description]
        """
        return String.build(
            words=self.__words__(delimiters, split_on_first_upper),
            word_modifier=str.title,
            replace_chars=(" ", ""))

    def snake(self,
              delimiters: List[str] = DEFAULT_DELIMITERS,
              split_on_first_upper: bool = True,
              title_case: bool = False) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): [description]. Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): [description]. Defaults to True.
            title_case (bool, optional): [description]. Defaults to False.

        Returns:
            String: [description]
        """
        return String.build(
            words=self.__words__(delimiters, split_on_first_upper),
            delimiter="_",
            word_modifier=str.title if title_case else str.lower,
            replace_chars=(" ", "_"),
            strip_chars="-")
