# Repeated Substring Checker

## Description

This function determines if a given string `s` consists of one repeated substring.

- If the string is made up of a repeated substring, the function returns the substring.
- If there are multiple possible answers, the function returns the longest one.
- If the string does not consist of a repeated substring, the function returns an empty string.

## Definition of Repeated Substring

A "repeated substring" refers to a pattern of characters that reoccurs throughout the full string with no leftover characters.

### Examples

- `"abababab"` → Repeated substrings: `"ab"`, `"abab"`. The function should return `"abab"` (longest substring).
- `"abcabcab"` → No repeated substring as the final characters `"ab"` do not complete the repeating pattern of `"abc"`.
