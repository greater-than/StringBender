# StringBender
Sub-class of Python `str` that adds case conversion functions. They are especiially useful for tranforming data model field names,  ex: REST (camelCase) to Python (snake_case).

### Table of Contents

* [Installation](#installation)
* [Convenvience Methods](#convenience-methods)
* [The String Class](#the-string-class)
<br><br>

## Installation

From the command line:
```sh
pip install stringbender
```

## Convenience Methods

StringBender provides helper methods for converting the case of a specified string:
* [`stringbender.camel`](#camel)
* [`stringbender.kebob`](#kebob)
* [`stringbender.pascal`](#pascal)
* [`stringbender.snake`](#snake)

The return type of each method is [`stringbender.String`](#stringbender-string).

These helper methods call a corresponding method in the `stringbender.String` class.

The `stringbender.String` class derives from `str`. Every base method in str has been overridden to return an instance of `stringbender.String` resulting in a fluent object.

### Usage:
```python
from stringbender import camel, kebob, pascal, snake, String


# ================================================================================
# EXAMPLES                           # OUTPUT

s = "Hasta la vista baby"
print(camel(s))                      # hastaLaVistaBaby
print(kebob(s)                       # hasta-la-vista-baby
print(pascal(s))                     # HastaLaVistaBaby
print(snake(s))                      # hasta_la_vista_baby

# ================================================================================
# Chaining functions

print(pascal(s).swapcase())          # hASTAlAvISTAbABY
print(pascal(s).swapcase().snake())  # h_ast_alv_ist_ab_aby

# ================================================================================
# Using a StringBender function with a built-in function

# Create an instance of stringbender.String:
s = String("vote*for*pedro")

# Check the default output:
print(s.camel())                     # vote*For*Pedro (hmm... this isn't right)

# Pass in a custom delimiter:
print(s.replace("*", " ").camel()    # voteForPedro (Much better!)

# ================================================================================
# Using a list of delimiters
s = snake("Careful man, there’s a beverage here!", delimiters=[",", "’", "!"])
print(snake(s)                       # careful_man_there_s_a_beverage_here

```

## The String Class

### `stringbender.String`
<br>

***Methods***<br>
_Optional argument definitions [below](#optional-method-arguments)_

#### __`camel()`__ (String) :<br>
Combines all words and he first letter of the first word is lower case, while the first letter of every subsequent word is uppercase.

#### __`kebob()`__ (String)<br>
Creates a hyphen delimited lower-case string.

#### __`pascal()`__ (String)<br>
Combines all words, and capitalizes the first letter of each word.

#### __`snake()`__ (String)<br>
Creates an underscore delimited lower-case string.
<br><br>


#### ***Constants***

`DEFAULT_DELIMITERS: List[str] = [" ", ".", "-", "_", ":", "\\"]`
<br><br>


#### ___Optional Method Arguments___

`delimiters: List[str] = DEFAULT_DELIMITERS`<br>
Used to split the string into words.

`split_on_first_upper: bool`<br>
Splits on the first occurence of a capital letter following a lowercase letter.

`title_case: bool`<br>
For character-delimited strings (kebob, snake), This will capitalize the first letter of each word.
