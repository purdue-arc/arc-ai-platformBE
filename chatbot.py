import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key= "AIzaSyCQOxN3zpxQJYcn0dZlhqKMiVHfyVWyDcY")


model = genai.GenerativeModel('gemini-pro')

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

response = model.generate_content("What is the meaning of life?")

print(response.text)




