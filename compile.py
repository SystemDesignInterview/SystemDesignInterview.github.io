import os
import markdown
import pdfkit

# Paths
input_file = "README.md"
output_dir = "_site"
output_html = os.path.join(output_dir, "index.html")
output_pdf = os.path.join(output_dir, "index.pdf")

def compile_markdown_to_pdf(input_path, output_html_path, output_pdf_path):
    # Check if the input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found.")
    
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
    
    # Read the Markdown file
    with open(input_path, "r", encoding="utf-8") as md_file:
        markdown_content = md_file.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    
    # Write HTML to file
    with open(output_html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    
    # Convert HTML to PDF
    pdfkit.from_file(output_html_path, output_pdf_path)
    print(f"Markdown compiled to PDF: {output_pdf_path}")

if __name__ == "__main__":
    compile_markdown_to_pdf(input_file, output_html, output_pdf)
