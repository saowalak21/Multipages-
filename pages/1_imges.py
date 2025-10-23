# ในไฟล์ 1_Imges.py
import os
import streamlit as st

st.title("Images")

images = ["1.jpg", "2.jpg", "3.jpg"] 
caption = ["วิวแม่น้ำเจ้าพระยา", "น้ำตก", "ทะเล"] 

cols = st.columns(len(images))

for col, img_path, img_caption in zip(cols, images, caption):
    if os.path.exists(img_path):
        
        col.image(img_path, caption=img_caption, use_container_width=True) 
    else:
        col.warning(f"Image not found: {img_path}")