# models/markdown_parser.py
import markdown
import tempfile
import webbrowser

def convert_markdown_to_html(md_text: str) -> str:
    html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite', 'tables'])
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    body {{
        font-family: sans-serif;
        padding: 1rem;
        max-width: 800px;
        margin: auto;
        line-height: 1.6;
    }}
    pre {{
        background: #f0f0f0;
        padding: 1em;
        overflow: auto;
    }}
    code {{
        background: #eee;
        padding: 0.2em;
    }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

def preview_markdown(md_text: str):
    html = convert_markdown_to_html(md_text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8") as f:
        f.write(html)
        webbrowser.open(f"file://{f.name}")
