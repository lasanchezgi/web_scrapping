import re

def is_web_url(url):
    pattern = re.compile(

    )

    return pattern.match(url) is not None