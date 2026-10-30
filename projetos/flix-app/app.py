
import streamlit as st

from auth.page import render_login


def main():
    if 'token' not in st.session_state:
        render_login()
    else:
        ...


if __name__ == "__main__":
    main()
