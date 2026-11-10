
import streamlit as st

from auth.page import render_login


def main():
    if 'token' not in st.session_state:
        render_login()
    else:
        pages = {
            'Flix App': [
                st.Page('home/page.py', title='Início', url_path='home'),
                st.Page('actors/page.py', title='Atores', url_path='actors'),
                st.Page('reviews/page.py', title='Avaliações', url_path='reviews'),
                st.Page('genres/page.py', title='Gêneros', url_path='genres'),
                st.Page('movies/page.py', title='Filmes', url_path='movies'),
            ],
        }
        pg = st.navigation(pages)
        pg.run()


if __name__ == "__main__":
    main()
