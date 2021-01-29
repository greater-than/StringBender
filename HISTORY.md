# 0.2.0 - 1/28/2021
- adds `String.as_str()` to return `str` type

BREAKING CHANGES:<br>
These changes were made to placate static type-checkers without having to convert the output to `str`
- static methods return `str` type.
- removed override of `__str__` method so that output will not be of type `stringbender.String`

# 0.1.0 - 1/6/2021
- Case-conversion methods:
  - camel
  - kebob
  - pascal
  - snake
- Overrides most super-class functions to return a type of `stringbender.String`


