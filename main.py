import streamlit as st
from datetime import datetime
import models.Colaborador as colaborador
import database as db


def pagina_cadastro_colab():
    st.title("Cadastrar Colcaborador")

    with st.form(key="include_colaborador"):
        input_nome = st.text_input(label="Insira seu nome")
        input_botao_cadastrar_colab = st.form_submit_button("Cadastrar colaborador")
        input_botao_exibe_colabs = st.form_submit_button("Exibir colaboradores")
        input_botao_deleta_colabs = st.form_submit_button("Remover colaborador")

    if input_botao_cadastrar_colab:
        colaborador.nome = input_nome
        db.cadastrarColab(input_nome)

# fazer exibir e deletar funcionar
    if(input_botao_exibe_colabs):
       db.exibirColabs()


    if(input_botao_deleta_colabs):
        db.removerColab(input_nome)

pagina_selecionada = st.sidebar.radio("Navegação", ["Cadastrar Colaborador", "Lista de Tarefas"])

if pagina_selecionada == "Cadastrar Colaborador":
    pagina_cadastro_colab()



def pagina_lista_tarefa():
    st.title("Lista de tarefas")

    with st.form(key="include_tarefa"):
        input_nome_tarefa = st.text_input(label="Descreva a terefa")
        input_hora = st.time_input("Selecione uma hora", datetime.now().time())
        input_colaborador = st.selectbox("Colaborador", ["Sarah", "Sabrina", "Samuel"])
        input_botao_tarefa = st.form_submit_button("Cadastrar Tarefa")

        if input_botao_tarefa:
            st.write(f'Descrição Tarefa: {input_nome_tarefa}')
            st.write(f'Horário: {input_hora}')
            st.write(f'Colaborador: {input_colaborador}')

if pagina_selecionada == "Lista de Tarefas":
    pagina_lista_tarefa()
