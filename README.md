# StrangeLang
Compiler for a new Programming Language called "StrangeLang"

## Execution

To execute, just run `main.py` with the source file path as an argument and the `-f` flag, eg:

```sh
python main.py -f source_file.sl
```

`.sl` is just a mock extension, it will make no difference in execution.

## Language Rules

+ Variable names must start with at least one upper or lower case letter or underscore `_`, and can consist of lower and upper case letters, numbers or underscores.
+ Strings can consist of any character sequence between `"` `"`. Empty strings are also valid.
+ Numbers are all stored equally (both floating points and integers), they must have at least one digit, can be followed by a dot `.` and any number of digits after. For example, `0.` is a valid number, `.2` is not.
+ Lines must end with a ` ;`, note that there must be a space before the ` ;`.
+ There is no way to make comments as of this version.
+ Everything has to be separated by spaces, if you do something such as `var n1=2`, it will not work.

## Tokenizing Process

The lexical analyser will separate the whole text by spaces, then attempt to match it to defined patterns. If no pattern matches, it will raise an `invalid token exception`. If multiple patterns match, the one with highest priority will be used. Priorities are defined as follows:

1. keywords
2. separators
3. operators
4. numbers
5. strings
6. variable names

The complete list of each item can be seen in the `tokens.json` file, inside the [Configs](https://www.github.com/LRAbbade/StrangeLang/tree/master/Configs) folder.

## Testing

There's a predefined test script in `Tests/test.sl`, to run it:

```sh
python main.py --test
```

## Requirements

* Python 3+

---
