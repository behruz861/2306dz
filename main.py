import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def extract_numbers(text):
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    return numbers

def is_valid_url(url):
    pattern = r'^(https?://)?[\w.-]+\.[a-zA-Z]{2,}(\/\S*)?$'
    return re.match(pattern, url) is not None

def extract_capitalized_words(text):
    pattern = r'\b[A-Z][a-zA-Z]+\b'
    words = re.findall(pattern, text)#
    return words

def contains_only_digits(text):
    pattern = r'^\d+$'
    return re.match(pattern, text) is not None

def extract_hashtags(text):
    pattern = r'#(\w+)'
    hashtags = re.findall(pattern, text)
    return hashtags

def is_valid_ip_address(ip):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

def extract_dates(text):
    pattern = r'\b(\d{1,2})\/(\d{1,2})\/(\d{4})\b'
    dates = re.findall(pattern, text)
    return dates is not None

def is_valid_phone_number(number):
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, number) is not None

def extract_links(html):
    pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"[^>]*>(.*?)</a>'
    links = re.findall(pattern, html)
    return links


# Тестирование 1 функции
text1 = 'My email is behruz861@yandex.com.'
emails = find_emails(text1)
print(emails)

text2 = 'Contact us at something@gmail.com or anything@mail.uz for asking questions.'
emails2 = find_emails(text2)
print(emails2)

# Тестирование 2 функции
test3 = 'There are 10 apples and 5 banana.'
numbers3 = extract_numbers(test3)
print(numbers3)

test4 = 'The price is $99.99 and quantity is 50.'
numbers4 = extract_numbers(test4)
print(numbers4)

# Тестирование 3 функции
url1 = 'https://ipakyulibank.uz/'
print(is_valid_url(url1))

url2 = 'https://example.com'
print(is_valid_url(url2))

# Тестирование 4 функции
text5 = 'Please Come to Event on Monday'
words5 = extract_capitalized_words(text5)
print(words5)

text6 = 'The Big Brown Bear was in Spring Sleep.'
words6 = extract_capitalized_words(text6)
print(words6)

# Тестирование 5 функции
text7 = '12345'
print(contains_only_digits(text7))

text8 = '1234a'
print(contains_only_digits(text8))

# Тестирование 6 функции
text9 = 'I love #programming and #python'
hashtags1 = extract_hashtags(text9)
print(hashtags1)

text10 = '#Monday is hard day.'
hashtags2 = extract_hashtags(text10)
print(hashtags2)

# Тестирование 7 функции
ip1 = '192.168.0.1'
print(is_valid_ip_address(ip1))

ip2 = '223.421.1.1'
print(is_valid_ip_address(ip2))

# Тестирование 8 функции
text11 = 'This event will take place on 25 October. Don\'t miss'
dates1 = extract_dates(text11)
print(dates1)

text12 = 'The deadline for submission is 15 November.'
dates2 = extract_dates(text12)
print(dates2)

# Тестирование 9 функции
number1 = '+12345678'
print(is_valid_phone_number(number1))

number2 = '+098765434'
print(is_valid_phone_number(number2))

# Тестирование 10 функции
html1 = '<a href="itstep.uz">Example site</a>'
link1 = extract_links(html1)
print(link1)

html2 = '<a href="example.com">Example website</a>'