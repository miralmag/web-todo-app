import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state['new_todo'] + '\n'
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title('My To-do App')
st.subheader('A minimalistic app')
st.write('Increase your productivity with this app')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Enter a todo...',
              on_change=add_todo, key='new_todo')

