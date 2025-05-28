import re

"""pattern = r'[aeiouAEIOU]'
string = "I am learning regular expressions"

matches = re.findall(pattern, string)
print(matches)"""

#Exercise 1:  Extracting Phone Numbers 
def extract_phone_number_info(text):
    pattern = r'\((\d{3})\) (\d{3} \d{4})|(\d{3} \d{3} \d{4})'
    matches = re.findall(pattern, text)
    
    results = []
    for match in matches:
        area_code = match[0] if match[0] else match[2][:3]  # Check which group matched for area code
        phone_number = match[1] if match[1] else match[2][4:]  # Check which group matched for phone number
        results.append((area_code, phone_number))
    
    return results

# Test cases
test_strings = [
    "My phone number is (123) 456 7890",
    "You can reach me at 083 123 4567"
]

for string in test_strings:
    info = extract_phone_number_info(string)
    print(f"Input: {string}")
    print(f"Extracted info: {info}")
    print()



#Activity 1: Validating Dates
from datetime import datetime

def validate_date(date_string):
    pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19|20)\d{2}$'
    if not re.match(pattern, date_string):
        return False
    
    # Extra calendar validation
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

# Test cases
dates = [
    "15-05-2022",  # valid
    "31-12-2023",  # valid
    "30-02-2024",  # invalid
    "01-01-1899"   # invalid
]

for date in dates:
    print(f"{date}: {'Valid' if validate_date(date) else 'Invalid'}")

#Activity 2: Credit Card Number Validation

import re

pattern = r'^(\d{4})([- ])\d{4}\2\d{4}\2\d{4}$'

test_cases = [
    "1234-5678-9012-3456",  # valid
    "1234 5678 9012 3456",  # valid
    "1234567890123456",     # invalid
    "1234-5678-9012-345"    # invalid
]

for number in test_cases:
    result = "Valid" if re.fullmatch(pattern, number) else "Invalid"
    print(f"{number}: {result}")
