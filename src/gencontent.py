from block_md import markdown_to_blocks, markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            h1 = block[2:]
            return h1
    else:
        raise Exception("No h1 heading detected")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating content from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        md_content = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(md_content)
    html_str = html_node.to_html() 

    title = extract_title(md_content)

    template = template.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", html_str)

    path = Path(dest_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template)


