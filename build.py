import markdown
from markdown.extensions import Extension

class BridgeExtension(Extension):
    pass


def concatenate_file_path_array_to_string(file_path_ary):
    content = '[TOC]\n\n'
    for file_name in file_path_ary:
        file = open(file_name)
        content += file.read() + '\n'
    return content

def markdown_to_html(md_string):
    return markdown.markdown(md_string, 
                             extensions=['extra', 'toc'], 
                             output_format='html5')

def html_to_pdf(html_string):
    pass

if __name__ == '__main__':
    CONSTRUCTIVE_SYSTEM = ['constructive/opening.md']
    DEFENSIVE_SYSTEM = [] #['defensive/*.md']

    content = concatenate_file_path_array_to_string(CONSTRUCTIVE_SYSTEM)
    html = markdown_to_html(content)
    file = open('constructive_bidding_system.html', 'w')
    file.write(html)
