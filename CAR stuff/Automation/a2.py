import xmltodict
import pprint

# Open the file and read the contents
with open('YESHU.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()

# Use xmltodict to parse and convert
# the XML document
my_dict = xmltodict.parse(my_xml)

# Print the dictionary
# pprint.pprint(my_dict, indent=2)
print(my_dict['document']["page"])