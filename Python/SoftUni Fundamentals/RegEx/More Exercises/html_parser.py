import re

text = input()
title_pattern = r'<title>([a-zA-Z\d\s]+)</title>'
title_regex = re.findall(title_pattern, text)
title = "".join(title_regex)
content_pattern = r'<body>.+</body>'
body_content = re.findall(content_pattern, text)
pattern_content = re.findall(r'>([^<>]*)', "".join(body_content))
content = ""
for element in pattern_content:
    content += element
content = content.replace('\\n', '')
print(f"Title: {title}\nContent: {content}")
