import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from login.page import show_login
from home.page import show_home
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('🎬 Flix App')

        menu_option = st.sidebar.selectbox(
            '📌 Selecione uma opção',
            ['🏠 Início', '🎭 Gêneros', '🎬 Atores/Atrizes', '🎥 Filmes', '⭐ Avaliações']
        )

        if menu_option == '🏠 Início':
            st.markdown("""
            Bem-vindo ao **Flix App**, sua central para explorar e descobrir informações
            sobre filmes, atores e avaliações!
        """)
            show_home()

        elif menu_option == '🎭 Gêneros':
            st.subheader('🎭 Gêneros de Filmes')
            st.write('Descubra uma variedade de gêneros cinematográficos.')
            show_genres()

        elif menu_option == '🎬 Atores/Atrizes':
            st.subheader('🎬 Lista de Atores e Atrizes')
            st.write('Aqui está a lista de atores e atrizes populares.')
            show_actors()

        elif menu_option == '🎥 Filmes':
            st.subheader('🎥 Lista de Filmes')
            st.write('Confira alguns dos filmes mais populares.')
            show_movies()

        elif menu_option == '⭐ Avaliações':
            st.subheader('⭐ Avaliações de Filmes')
            st.write('Veja as avaliações dos usuários sobre os filmes mais recentes.')
            show_reviews()


if __name__ == '__main__':
    main() 
