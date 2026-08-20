import streamlit as st
st.set_page_config(page_title="Product Catalog", layout="wide")

products = [
   {"name": "Math", "Time": "8:00 - 9:00", "img": "https://media.istockphoto.com/id/1265965042/vector/math-theory-mathematics-calculus-on-class-chalkboard-algebra-and-geometry-science.jpg?s=612x612&w=0&k=20&c=T97ylW_6ht1STS_MRw4YrDg0Kt3HuoXEOQI9vQFfin8= "},
   {"name": "English", "Time": "9:00 - 10:00", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFg5hyhAgNpNPh5kx5mGuzs36Lr1N2loittBAaODoEBw&s=10"},
   {"name": "History", "Time": "10:00 - 11:00", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5omlcnub7aMXSc0dH7x4KMgCpi_DuQDZpsNeif6Bn6w&s"},
   {"name": "biology", "Time": "11:00 - 12:00", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFbN7PVY6ZLMzZrLY8XvMsXKPpeTh51FPx4KhsD9__IwLH8S38YlH2MmE&s=10"},
   {"name": "Computer science", "Time": "12:00 - 13:00", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrdKFdXJ9wtmYXXrZeG-BNT5IrmFy1iwvwOqiajjCcBtHq90iJQQsM3eA&s=10"},
   {"name": "Music", "Time": "13:00-14:00", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZASMz8eyS02KUPcDo2ZCLVNRhdighUNtXz0ZUSuRciQ&s=10"},
]
st.title(" Extra Smart Classroom")
st.markdown("---")
NUM_COLS = 3

for i in range(0, len(products), NUM_COLS):
   row_products = products[i:i + NUM_COLS]
   cols = st.columns(NUM_COLS)
   for col, prod in zip(cols, row_products):
       with col:
           st.image(prod["img"], use_container_width=True)
           st.subheader(prod["name"])
           st.write(f"**Time:** {prod['Time']}")
           if st.button("View Details", key=prod["name"]):
               st.info(f"You selected {prod['name']}")

   st.markdown("---")