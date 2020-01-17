import json

with open('./templates/responses_templates/success_templates.json', 'r') as success_file:
    success_template = json.load(success_file)

with open('./templates/responses_templates/error_templates.json', 'r') as error_file:
    error_template = json.load(error_file)
