import streamlit as st
st.set_page_config(page_title="Product Catalog", layout="wide")
products = [
   {"name": "Wireless Headphones", "price": "$299.99", "img": "https://picsum.photos"},
   {"name": "Smart Watch", "price": "$199.99", "img": "https://picsum.photos"},
   {"name": "Mechanical Keyboard", "price": "$129.99", "img": "https://picsum.photos"},
   {"name": "Ergonomic Mouse", "price": "$79.99", "img": "https://picsum.photos"},
   {"name": "4K Monitor", "price": "$449.99", "img": "https://picsum.photos"},
   {"name": "HD Webcam", "price": "$89.99", "img": "https://picsum.photos"},
]
st.title("Ninja Product Catalog")
st.markdown("---")
NUM_COLS = 3
for i in range(0, len(products), NUM_COLS):
   row_products = products[i:i + NUM_COLS]
   cols = st.columns(NUM_COLS)
   for col, prod in zip(cols, row_products):
       with col:
           st.image(prod["img"], use_container_width=True)
           st.subheader(prod["name"])
           st.write(f"**Price:** {prod['price']}")
           if st.button("View Details", key=prod["name"]):
               st.info(f"You selected {prod['name']}")

   st.markdown("---")