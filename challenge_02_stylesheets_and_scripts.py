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

stylesheet = "main.min.css"
script_file  = "bundle.js"

# replacing stylesheet
original_stylesheet = '"styles.css"'
length_of_stylesheet = len(original_stylesheet)
index_of_stylesheet = html.find(original_stylesheet)

first_part_stylesheet = f'{html[:index_of_stylesheet]}"'
last_part_stylesheet = f'"{html[index_of_stylesheet + length_of_stylesheet:]}'
html = f"{first_part_stylesheet + stylesheet + last_part_stylesheet}"

# replacing script file
original_script = '"app.js"'
length_of_script = len(original_script)
index_of_script = html.find(original_script)

first_part_script = f'{html[:index_of_script]}"'
last_part_script = f'"{html[index_of_script + length_of_script:]}'
html = f"{first_part_script + script_file + last_part_script}"

print(html)