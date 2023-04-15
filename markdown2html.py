#!/usr/bin/python3
'''
This is python  script that codes markdown to HTML
'''
import sys
import os
import re


def convert_md_to_html(input_file, output_file):
    """
    Convert Markdown file to HTML file.
    Args:
        input_file (str): Input file path.
        output_file (str): Output file path.
    """
    if not os.path.exists(input_file) or not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist or is not a file.")
        sys.exit(1)

    html_content = []
    unordered_list_started = False

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()

            # Handle headings
            heading = re.split(r"#{1,6} ", line)
            if len(heading) > 1:
                h_level = len(line[: line.find(heading[1]) - 1])
                html_content.append(f"<h{h_level}>{heading[1]}</h{h_level}>\n")

            # Handle unordered lists
            else:
                list_item = re.split(r"- ", line)
                if len(list_item) > 1:
                    html_content.append(f"<li>{list_item[1]}</li>\n")
                    if not unordered_list_started:
                        html_content.append("<ul>\n")
                        unordered_list_started = True
                else:
                    if unordered_list_started:
                        html_content.append("</ul>\n")
                        unordered_list_started = False
                    html_content.append(line)

        if unordered_list_started:
            html_content.append("</ul>\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(html_content)


if __name__ == "__main__":
    if len(sys.argv[1:]) != 2:
        print("Usage: ./markdown2html.py <input-file> <output-file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_md_to_html(input_file, output_file)