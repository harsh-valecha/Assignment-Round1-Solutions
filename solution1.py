import re

text_to_search ='''
2124567890
212-456-7890
(212)456-7890
(212)-456-7890
212.456.7890
212 456 7890
+12124567890
+12124567890
+1 212.456.7890
+212-456-7890
1-212-456-7890
'''

# The standard format is - [+][country code][area code][local phone number]
pattern = re.compile(r'\+?[0-9]{0,3}[-]?[0-9]{3}[-\.\s]?[0-9]{3}[-\.\s]?[0-9]{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

