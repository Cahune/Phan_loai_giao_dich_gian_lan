import streamlit as st
from streamlit_option_menu import option_menu
import base64


import home, login, prediction, about
st.set_page_config(
        page_title="Cahu",
)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./images/bg.png')
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })
        
    def run():
        # Initialize session state
        if 'selected' not in st.session_state:
            st.session_state.selected = "Trang chủ"
        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False

        st.markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: #95D2B3;
            }
        </style>
        """, unsafe_allow_html=True)

        # Sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Menu",
                options=["Trang chủ", "Đăng nhập", "Kết quả dự đoán","Thông tin"],
                icons=["house-heart-fill", "arrow-right-square-fill", "search-heart-fill","info-circle-fill"],
                menu_icon="app-indicator",
                default_index=0,
                styles={
                    "container": {"background-color": "#F1F8E8"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#55AD9B"},
                }
            )

        # Handle different selections
        if selected == "Trang chủ":
            home.Home()
        elif selected == "Đăng nhập":
            login.Login()
        elif selected == "Kết quả dự đoán":
            prediction.Prediction()
        elif selected == "Thông tin":
            about.About()

    run()
