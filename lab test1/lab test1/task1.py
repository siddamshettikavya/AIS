import re

def extract_urls(text):
    # Regex pattern for URLs (http, https, www)
    pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    return re.findall(pattern, text)

# Example usage
text = "Visit https://www.example.com or http://test.org for more info. Also check www.site.net."
print(extract_urls(text))