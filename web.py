# WEB
import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    # session_state è un dizionario
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    #print(todo)
    functions.write_todos(todos)

# Legge la lista todos
todos = functions.get_todos()

st.title('My Todo App')
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # Viene rimosso l'item con il checkbox attivo
        todos.pop(index)
        functions.write_todos(todos)
        # Occorre cancellarlo anche dalla liste creata dal session state
        # Non usare experimental_rerun() in quanto è stato deprecato
        del st.session_state[todo]
        st.rerun()

# st.text_input(label="Enter a todo: ")
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# Visualizza nel browser il dictionary
#st.session_state

