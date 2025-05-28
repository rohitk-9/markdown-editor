import markdown


def convert_markdown_to_html(md_text: str) -> str:
    """Convert Markdown text to HTML using python-markdown."""
    html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite', 'tables'])
    return html
