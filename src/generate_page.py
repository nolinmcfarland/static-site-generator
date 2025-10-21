import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, destination_path):
    if destination_path.endswith("md"):
        destination_path = destination_path.replace(".md", ".html")

    print(f"Generating page from {from_path} to {destination_path} using {template_path}")

    with open(from_path) as file:
        content = file.read()

    with open(template_path) as file:
        template = file.read()

    html =  markdown_to_html_node(content).to_html()
    title = extract_title(content)
    generated_page = template.replace("{{ Title }}", title)
    generated_page = generated_page.replace("{{ Content }}", html)

    if not os.path.exists(destination_path):
        os.makedirs(
            os.path.dirname(destination_path),
            exist_ok=True
        )

    with open(destination_path, "w") as file:
        _ = file.write(generated_page)
        

def generate_pages(content_path, template_path, destination_path):
    if os.path.isfile(content_path):
        generate_page(content_path, template_path, destination_path)
    else:
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)
        for subpath in os.listdir(content_path):
            generate_pages(
                os.path.join(content_path, subpath),
                template_path,
                os.path.join(destination_path, subpath)
            )

            
    

