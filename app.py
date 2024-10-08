import streamlit as st
import pandas as pd
from database import create_table, add_cliente, view_all_clientes, get_cliente_by_id, edit_cliente, delete_cliente
from st_aggrid import AgGrid

# setar a página par modo wide
def wide_space_default():
    st.set_page_config(layout='wide')

wide_space_default()

# Aplicativo Streamlit


def main():
    
    # st.markdown("<h1 style='text-align: center; color: red;'>Escritório de Advocacia - Dra. Vanessa Streck</h1>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: center; color: white;'>Av. Pereira Rego, 1100, sala 09 - Centro - Candelária - RS - Telefone/WhatsApp (51) 9999 9999</p><br>", unsafe_allow_html=True)


    menu = ['Cadastrar', 'Consultar', 'Editar', 'Excluir']
    choice = st.sidebar.selectbox('Escritório de Advocacia - Dra. Vanessa Streck', menu)

    create_table()

    if choice == 'Cadastrar':
        st.subheader('Cadastrar Novo Cliente')

        nome = st.text_input('Nome')
        telefone = st.text_input('Telefone')
        email = st.text_input('E-mail')
        endereco = st.text_area('Endereço')

        if st.button('Cadastrar'):
            add_cliente(nome, telefone, email, endereco)
            st.success(f'Cliente {nome} cadastrado com sucesso!')

    elif choice == 'Consultar':
        st.subheader('Lista de Clientes')
        clientes = view_all_clientes()
        if clientes:
            df = pd.DataFrame (clientes, columns=['ID', 'Nome', 'Telefone', 'E-mail', 'Endereço'])      
            AgGrid(df, editable=True,key='grid5')
       
        else:
            st.info('Nenhum cliente cadastrado.')

    elif choice == 'Editar':
        st.subheader('Editar Cliente')
        clientes = view_all_clientes()
        if clientes:
            df = pd.DataFrame(clientes, columns=[
                                'ID', 'Nome', 'Telefone', 'E-mail', 'Endereço'])
            AgGrid(df)

            cliente_id = st.number_input(
                'ID do Cliente para editar', min_value=1, step=1)
            cliente = get_cliente_by_id(cliente_id)

            if cliente:
                nome = st.text_input('Nome', cliente[1])
                telefone = st.text_input('Telefone', cliente[2])
                email = st.text_input('E-mail', cliente[3])
                endereco = st.text_area('Endereço', cliente[4])

                if st.button('Atualizar'):
                    edit_cliente(cliente_id, nome, telefone, email, endereco)
                    st.success(f'Cliente {nome} atualizado com sucesso!')
            else:
                st.warning('Cliente não encontrado.')
        else:
            st.info('Nenhum cliente cadastrado para editar.')

    elif choice == 'Excluir':
        st.subheader('Excluir Cliente')
        clientes = view_all_clientes()
        if clientes:
            df = pd.DataFrame(clientes, columns=[
                              'ID', 'Nome', 'Telefone', 'E-mail', 'Endereço'])
            AgGrid(df)

            cliente_id = st.number_input(
                'ID do Cliente para excluir', min_value=1, step=1)
            if st.button('Excluir'):
                delete_cliente(cliente_id)
                st.success(
                    f'Cliente com ID {cliente_id} excluído com sucesso!')
        else:
            st.info('Nenhum cliente cadastrado para excluir.')


if __name__ == '__main__':
    main()
