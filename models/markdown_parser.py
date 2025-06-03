import markdown


def convert_markdown_to_html(md_text: str) -> str:
    """Convert Markdown text to HTML using python-markdown."""
    md_extensions = [
    'fenced_code',
    'codehilite',
    'nl2br',
    'tables',
    'sane_lists',
    'smarty',
    'toc',
    'footnotes',
    'abbr',
    'def_list',
    'attr_list',
    'meta',
    'admonition'
]
    html = markdown.markdown(md_text, extensions=md_extensions)
    return html
