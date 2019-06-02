"""
This file is responsable to be the main controller for IBLT,
and is responsable for:

1. Enhancing the provided images
2. Isolating the text to translate
3. translating the text
4. stiching the translated text back onto the image

while also saving the images at each step to demonstrate the
functionality for project demos

dependancies:
Pillow (PIL)
googletrans

TO DO:
4. stitch the translated text to the enhanced image

MAYBES:
5. the final product might look better if we downscale the final
    image by the same factor used to enhance the image at the beginning
6. we'll need to figure out how to determine the language
    (user input was stated in the proposal), and if we want a simple GUI
"""

from IBLT import image_enhancer, image_fryer, text_ioslator, \
    translator, languages

image_path = 'images/Swedish.PNG'

# Enhance the image and show it
enhanced_image, enhanced_image_path = image_enhancer.enhance_image(
    image_path, 5.0)

# isolate the text from the image
raw_text = text_ioslator.ioslate_text(enhanced_image_path)

# get language input from user and retrieve the corresponding langcode
langcode = languages.get_lang_code(input("Enter language: ").lower())
# TO DO: this should be done via GUI later

# translate the text
translated_text = translator.text_translator(raw_text, langcode)

# stitch the text back onto the image
# TO DO

print(translated_text)
