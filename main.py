import streamlit as st
from core.session_manager import SessionManager
from ui.layouts import AppLayout

def main():
    SessionManager.initialize()
    layout = AppLayout()
    layout.setup_page()
    layout.render_sidebar()
    layout.render_main_content()

if __name__ == "__main__":
    main()