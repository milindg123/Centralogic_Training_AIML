import re

pattern = r'\D*'  # Matches one or more digits

text = "There are 50 apples and 175 oranges."

# Search for the first occurrence
match = re.search(pattern, text)
if match:
    print(f"Found a match: {match.group()}")

# Match only at the beginning
match = re.match(pattern, text)
if match:
    print(f"Found a match at the beginning: {match.group()}")
else:
    print("No match at the beginning.") 

# Find all occurrences
matches = re.findall(pattern, text)
print(f"All matches: {matches}") 

# Iterate over all matches
for match in re.finditer(pattern, text):
    print(f"Match found: {match.group()} at position {match.start()} to {match.end()}")

pattern = r'\d+'
replacement = '#'

# Replace all matches
result = re.sub(pattern, replacement, text)
print(result) 

