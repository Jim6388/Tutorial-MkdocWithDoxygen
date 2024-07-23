import xml.etree.ElementTree as ET
import os
import re
import argparse

def clean_text(text):
    if text is None:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def parse_param(param):
    param_name = param.find('declname')
    param_type = param.find('type')
    param_desc = param.find('parameterdescription/para')
    
    name = clean_text(param_name.text) if param_name is not None else ""
    type_ = clean_text(param_type.text) if param_type is not None else ""
    desc = clean_text(param_desc.text) if param_desc is not None else ""
    
    return f"- `{type_} {name}`: {desc}"

def parse_function(member):
    definition = clean_text(member.find('definition').text) if member.find('definition') is not None else ""
    argsstring = clean_text(member.find('argsstring').text) if member.find('argsstring') is not None else ""
    full_function_name = f"{definition}{argsstring}"
    
    brief = clean_text(member.find('briefdescription/para').text) if member.find('briefdescription/para') is not None else ""
    
    params = []
    for param_item in member.findall('.//parameteritem'):
        name_elem = param_item.find('.//parametername')
        desc_elem = param_item.find('.//parameterdescription/para')
        
        name = clean_text(name_elem.text) if name_elem is not None else ""
        desc = clean_text(desc_elem.text) if desc_elem is not None else ""
        
        type_ = ""
        for param in member.findall('.//param'):
            if param.find('declname').text == name:
                type_ = clean_text(param.find('type').text)
                break
        
        params.append(f"- `{type_} {name}`: {desc}")
    
    return_type = clean_text(member.find('type').text)
    return_desc = clean_text(member.find('.//simplesect[@kind="return"]/para').text) if member.find('.//simplesect[@kind="return"]/para') is not None else ""
    
    #markdown = f"## `{full_function_name}`\n\n"
    markdown = f"> **`{full_function_name}`**\n\n"
    if brief:
        markdown += f"{brief}\n\n"
    if params:
        markdown += "**Parameters:**\n\n"
        markdown += "\n".join(params) + "\n\n"
    markdown += f"**Return:** `{return_type}`"
    if return_desc:
        markdown += f" - {return_desc}"
    markdown += "\n\n"
    
    return markdown


def parse_file_info(compound):
    brief = clean_text(compound.find('briefdescription/para').text) if compound.find('briefdescription/para') is not None else ""
    return brief

def parse_doxygen_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    compound = root.find('compounddef')
    if compound is None or compound.get('kind') != 'file':
        return None
    
    filename = compound.find('compoundname').text
    file_info = parse_file_info(compound)
    functions = []
    
    for member in compound.findall('sectiondef/memberdef[@kind="function"]'):
        functions.append(parse_function(member))
    
    return filename, file_info, functions

def generate_markdown(filename, file_info, functions, output_file):
    with open(output_file, 'w') as f:
        f.write(f"# {filename}\n\n")
        if file_info:
            f.write(f"{file_info}\n\n")
        for func in functions:
            f.write(func)
            f.write("---\n\n")

def main(source_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    
    for filename in os.listdir(source_dir):
        if filename.endswith('.xml'):
            xml_file = os.path.join(source_dir, filename)
            parsed_data = parse_doxygen_xml(xml_file)
            if parsed_data:
                output_filename, file_info, functions = parsed_data
                output_file = os.path.join(dest_dir, output_filename.replace('.', '_') + '.md')
                generate_markdown(output_filename, file_info, functions, output_file)
                print(f"Generated: {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Doxygen XML to Markdown for MkDocs')
    parser.add_argument('source_dir', help='Directory containing Doxygen XML files')
    parser.add_argument('dest_dir', help='Directory to output Markdown files')
    args = parser.parse_args()

    main(args.source_dir, args.dest_dir)