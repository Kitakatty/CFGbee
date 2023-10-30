# REGEX exercises and examples

import re

# EXAMPLE 1 --- re.match

# matches the regex pattern starting from the beginning of the sentence 
# and returns the matched substring. 
# If something is found, then it returns a re.Match object; 
# if not, it returns None


my_str = "Nano Degree is fun"

nano_re = "Nano"
whitespace_re = r"\s"
multi_alpha_re = r"\w+"
regex = r"Nano\s\w+\s"  # 👍
regex2 = nano_re + whitespace_re + multi_alpha_re + whitespace_re  # 👎

matched = re.match(regex, my_str)
# print(matched)


#####################################################

# EXAMPLE 2 --- re.search


# matches the regex pattern within the entire input sentence and returns 
# the first occurrence of the matched substring. 
# The difference between re.search and re.match is 
# that the matched substring of re.search does not have to start 
# from the beginning of the input string.

my_str = "Software and Data Science 777 are fun"

# Science 777
regex = r"Sci[\w\s]+\d+"
matched = re.search(regex, my_str)
print(matched)
print(matched.span())
print(matched.group())

# EXAMPLE 3 --- re.finditer


# matches all of the regex patterns in the input string and 
# returns an iterator containing all the re.Match 
# objects of the matched substrings.


my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

# [data science, data analysis]

regex = r"data\s\w+"
result = re.finditer(regex, my_str)
print(list(result))

# EXAMPLE 4 --- re.findall


# matches all of the regex patterns in the input string and returns a 
# list containing all the matched substrings. The only difference between 
# re.findall and re.finditer is that re.findall returns a list 
# instead of an iterator and contains matched substrings 
# instead of re.Match objects.


my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

# [data science, data analysis]

regex = r"data\s\w+"
result = re.findall(regex, my_str)
print(result)

# EXAMPLE 5 --- re.sub


# matches all of the regex patterns in the input string 
# and substitutes them with the new_text provided.


my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = r"data\s\w+"
replacement_str = "cats"

result = re.sub(regex, replacement_str, my_str)
print(result)

# EXAMPLE 6 --- GROUPING


# Sometimes we might want to match a regex pattern but only capture a 
# portion (or group) of it. Regex provides a simple way of doing this 
# by using the parenthesis (). We can define the group we want to capture 
# by surrounding it with () within the regex pattern.


my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

# ["data science, data analysis"]
# ["science, analysis"]

regex = r"data\s(\w+)"
result = re.findall(regex, my_str)
print(result)

# EXAMPLE 7 --- COMPILING


# SO FAR, we have mainly used module-level functions provided by re directly. 
# Another way to perform regex pattern matching is to *compile* the pattern first
# and then call the functions on the compiled object. 
# 
# In general, we can use the compiled approach if we are going to use 
# the pattern MULTIPLE times; otherwise, it’s simpler to use the module-level
# (non-compiled) functions.


my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = r"data\s(\w+)"
pattern = re.compile(regex)

# result = re.findall(regex,my_str)
result = pattern.findall(my_str)
print(result)

# EXAMPLE 8 --- PRACTICAL EXAMPLE


# We have a list of mock trade ids that need to be processed, so that we
# extract the date string from each id


trade_ids = [
    "ghjd-gfjv-20220615-12345",
    "vbfd-dusi-20181103-11111",
    "pomm-xxsa-20041222-22222",
]
# ideal output:
# ['20220615', '20181103', '20041222']

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = r"\w{4}-\w{4}-(\d{8})-\d+"

# match the whole pattern, but only return the group
# group(1)
result = [re.search(regex, _id).group(1) for _id in trade_ids]
print(result)
