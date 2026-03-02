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

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"

body_content = f"<body>\n    <h1>{h1}</h1>\n    <h2>{h2}</h2>\n    <h3>{h3}</h3>\n</body>"
html_split = html.split("<body>\n</body>")

html = html_split[0] + body_content + html_split[1]

print(html)