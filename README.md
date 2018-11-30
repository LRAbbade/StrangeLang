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
+ Printing does not require `(` `)`, but you can only print one number, string or variable at a time.
+ Every variable declaration must have a initialization value, but it is not required to specify the variable type.
+ A function body should be an expression, and it does not take `;`.

## Lexical Analysis

The lexical analyser will separate the whole text by spaces, then attempt to match it to defined patterns. If no pattern matches, it will raise an `invalid token exception`. If multiple patterns match, the one with highest priority will be used. Priorities are defined as follows:

1. keywords
2. separators
3. operators
4. numbers
5. strings
6. variable names

The complete list of each item can be seen in the `tokens.json` file, inside the [Configs](https://www.github.com/LRAbbade/StrangeLang/tree/master/Configs) folder.

## Syntax Analysis

After the raw text has been separated into valid tokens, the syntax analyzer will build a syntax tree and attempt to find a suitable combination of tokens. The analizer used is a recursive backtracking analyzer.

If it's not able to rebuild the sentence, a syntax error is thrown.

The complete Syntax rules can be seen in the [Docs](https://www.github.com/LRAbbade/StrangeLang/tree/master/Docs) folder.

## Testing

There's a predefined test script in `Tests/test.sl`, to run it:

```sh
python main.py --test
```

## Requirements

* Python 3+

---
