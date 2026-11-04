
import streamlit as st

from auth.page import render_login


def main():
    if 'token' not in st.session_state:
        render_login()
    else:
        pages = {
            'Flix App': [
                st.Page('genres/page.py', title='Gêneros')
            ],
        }
        pg = st.navigation(pages)
        pg.run()


if __name__ == "__main__":
    main()
