import streamlit as st
from midwitGPT import *

st.title("AI Image Generation")

prompt = st.text_input("Prompt:", value="")

if st.button("Generate"):
  if not prompt:
      st.error("Please enter a prompt!")
  else:
      image = generate_meme_image(prompt)
      if image is not None:
          st.image(image)
      else:
          st.error("Image generation failed!")