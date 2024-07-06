from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import re
import anvil.media

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_transliterated_text.visible = False
    self.label_transliterated_text.foreground = 'grey'
    
  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    def trim_flag(selected_value):
        # Identify the position of the first regional indicator symbol
        flag_start = None
        for idx, char in enumerate(selected_value):
            if '\U0001F1E6' <= char <= '\U0001F1FF':
                flag_start = idx
                break
    
        # If a flag was found, return the part of the string before the flag starts
        if flag_start is not None:
            return selected_value[:flag_start].strip()
        else:
            return selected_value.strip()
    
    self.label_output.text = ''
    # Retrieve the text from the input TextArea
    input_text = self.text_area_input.text
    selected_value = self.language_dropdown.selected_value
    trimmed_value = trim_flag(selected_value)
    target_language = trimmed_value
    
    # Validate the input
    if not input_text:
        self.label_output.text = "Please enter text to translate."
        self.text_area_output.text = ""  # Clear the output TextArea
        return
    
    try:
        # Translate the text using the translation pipeline
        result = anvil.server.call('translate_text', input_text, target_language)
        # Display the translated text in the output TextArea
        self.text_area_output.text = result['translated_text']
        
        # Handle transliteration for Russian
        if target_language.lower() == 'russian' and result['transliterated_text']:
            self.label_transliterated_text.text = result['transliterated_text']
            self.label_transliterated_text.visible = True
        else:
            self.label_transliterated_text.visible = False
    except Exception as e:
        # Handle any errors and display a message to the user
        self.label_output.text = f"An error occurred: {e}"
        self.text_area_output.text = ""  # Clear the output TextArea in case of error

  def language_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.submit_button_click()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    new_url = "https://forms.gle/FMZ498g8uaUoFoc9A"
    self.link_1.url = new_url  # Set the URL of the link component

    # Optionally, open the URL in a new tab/window
    self.link_1.target = "_blank" 

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Toggle the visibility of rich text boxes
    self.rich_text_1.visible = not self.rich_text_1.visible
    self.rich_text_2.visible = not self.rich_text_2.visible
    # Toggle the visibility of the card
    self.card_2.visible = not self.card_2.visible

  def output_audio_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.text_area_output.text
    anvil.js.window.speakText(text)

  def button1_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.text_area_input.text
    anvil.js.window.speakText(text)




