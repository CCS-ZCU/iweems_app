import streamlit as st
import overview
import explorer

st.set_page_config(
    page_title="iWEEMS",
    page_icon="📊",
    layout="wide"
)

# Define the pages
PAGES = {
    "📊 About": overview,
    "🔍 Visualization App": explorer,
}

# Initialize session state if not set
if "page" not in st.session_state:
    st.session_state.page = "🔍 Visualization App"  # default page

# Sidebar title
st.sidebar.title("📌 Navigation")

# Sidebar buttons
for page_name in PAGES:
    if st.sidebar.button(page_name):
        st.session_state.page = page_name

# Load selected page
selected_page = PAGES[st.session_state.page]
selected_page.app()