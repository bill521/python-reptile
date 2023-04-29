import re


def valid_data_website(url):
    pattern = r'^https?://(?:www\.)?douyin\.com/\S+$'
    return re.match(pattern, url)
