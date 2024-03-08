import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key="AIzaSyCQOxN3zpxQJYcn0dZlhqKMiVHfyVWyDcY")

model = genai.GenerativeModel('gemini-pro')

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


with open('arc_wiki_input/arc_query.txt', 'r') as file:
    query = file.read()

with open('arc_wiki_input/arc_knowledge_base', 'r') as file:
    context = file.read()

# Write the combined content to combined_context.txt
with open('arc_wiki_input/combined_context.txt', 'w') as file:  # Use 'w' for writing
    file.write('Prompt:' + query+'\n')
    file.write(context)

# The part below seems unnecessary if you're just creating combined_content.txt
with open('arc_wiki_input/combined_content.txt', 'r') as file:
    gemini_pass = file.read()  # opens query prompt for reading

submit = gemini_pass

response = model.generate_content(submit)

print(response.text)
