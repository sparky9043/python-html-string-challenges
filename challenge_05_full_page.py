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

# Step 1 - Metadata using .replace()
html = html.replace("\"en\"", "\"es\"")
original_title = "My Page"
new_title = "Full Page Challenge"

html = html.replace(f"<title>{original_title}</title>", f"<title>{new_title}</title>")

# Step 2 - Assets using position-based slicing

# replace stylesheet
stylesheet = "app.min.css"
old_stylesheet = "styles.css"
old_stylesheet_position = html.find(old_stylesheet)

html = f"{html[:old_stylesheet_position] + stylesheet + html[old_stylesheet_position + len(old_stylesheet):]}"

# replace script file
script_file = "main.bundle.js"
old_script_file = "app.js"
old_script_file_position = html.find(old_script_file)
html = f"{html[:old_script_file_position] + script_file + html[old_script_file_position + len(old_script_file):]}"

# Inject an <h1>, <h2>, and <h3> into the body using .split("<body>", 1) and string concatenation
body_opening_tag = "<body>"
html_split = html.split(body_opening_tag, 1)

h1_text = "hello world"
h2_text = "this is a message for you"
h3_text  = "don't ever give up!"

h1_tag = f"<h1>{h1_text}</h1>"
h2_tag = f"<h2>{h2_text}</h2>"
h3_tag = f"<h3>{h3_text}</h3>"
four_spaces = "    "

html = f"{html_split[0] + body_opening_tag + "\n" + four_spaces + h1_tag + "\n" + four_spaces + h2_tag + "\n" + four_spaces + h3_tag + html_split[1]}"

# Step 5 Insert a <p> tag and an <img> tag after the last heading tag using .rfind() and position-based reconstruction

p_text = "I want to be really good at this!"
img_src = "image.png"
img_alt = "random alt for image"

p_tag = f"<p>{p_text}</p>"
img_tag = f"<img src=\"{img_src}\" alt=\"{img_alt}\">"

position_html_closing_tag = html.find("</html>")

h1_pos = html.rfind("</h1>", 0, position_html_closing_tag)
h2_pos = html.rfind("</h2>", 0, position_html_closing_tag)
h3_pos = html.rfind("</h3>", 0, position_html_closing_tag)
positions = [h1_pos, h2_pos, h3_pos]

last_position = 0
for position in positions:
    if position > last_position:
        last_position = position

html = f"{html[:last_position + len("</h3>")]}\n{four_spaces + p_tag}\n{four_spaces + img_tag}{html[last_position + len("</h3>"):]}"

# Step 6 - Use .find("</body>") to locate the closing body tag and insert a second <p> tag immediately before it — this <p> should contain a string that itself includes the <title> content, extracted dynamically from html using .find("<title>"), .find("</title>") and slicing

closing_body_tag = "</body>"
closing_body_tag_position = html.find(closing_body_tag)
extracted_title_text = html[html.find("<title>") + len("<title>"):html.find("</title>")]
second_p_tag = f"<p>The title of this document is \"{extracted_title_text}\"</p>"

html = f"{html[:closing_body_tag_position]}{four_spaces + second_p_tag}\n{html[closing_body_tag_position:]}"

def validate(html):
    print("--- Validation Report ---")
    if html.count(f"<title>{extracted_title_text}</title>") == 1:
        print("✅ <title> is correct")
    else:
        print("❌ <title> is correct")
    if html.count("<h1>") == html.count("<h2>") == html.count("<h3>") == 1:
        print("✅ <h1> found")
        print("✅ <h2> found")
        print("✅ <h3> found")
    else:
        print("❌ some <h1>, <h2>, <h3> tags are missing")
    if html.count("<img") == 1:
        print("✅ <img> appears exactly once")
    else:
        print("❌ <img> does not appear exactly once")
    if html.count("<p>") == 2:
        print("✅ <p> appears exactly twice")
    else:
        print("❌ <p> does not appear exactly twice")
    if html.startswith("<!DOCTYPE html>"):
        print("✅ Starts with <!DOCTYPE html>")
    else:
        print("❌ Does not start with <!DOCTYPE html>")
    if html.strip().endswith("</html>"):
        print("✅ Ends with </html>")
    else:
        print("❌ Does not end with </html>")

print(html)