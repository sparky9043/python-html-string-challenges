html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""

page_title = "My Awesome Portfolio"
page_lang = "fr"

html = html.replace("<title>My Page</title>", f"<title>{page_title}</title>")
html = html.replace('<html lang="en">', f'<html lang="{page_lang}">')

print(html)

# .replace() has a third argument which can limit how many occurrences it replaces.
# This can be useful when you do not intend to change every single occurrence of the old string with the new