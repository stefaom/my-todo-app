# WEB
import streamlit as st
#from altair.vegalite.v6.theme import theme
import functions

import streamlit as st

st.markdown(
    """
    <style>
    /* =========================
       PAGINA
       ========================= */
    .stApp {
        background-color: white;
        color: black;
    }

    h1, h2, h3, h4, h5, h6,
    p, span, label {
        color: black !important;
    }

    /* =========================
       CHECKBOX - PARTE CRITICA
       ========================= */

    /* Input vero e proprio */
    input[type="checkbox"] {
        appearance: none;              /* Rimuove stile di default */
        -webkit-appearance: none;
        -moz-appearance: none;

        width: 16px;
        height: 16px;
        background-color: white !important;
        border: 2px solid black !important;
        border-radius: 3px;
        cursor: pointer;
        position: relative;
    }

    /* Checkbox selezionato */
    input[type="checkbox"]:checked {
        background-color: white !important;
        border-color: black !important;
    }

    /* Segno di spunta */
    input[type="checkbox"]:checked::after {
        content: "✔";
        position: absolute;
        top: -2px;
        left: 2px;
        font-size: 14px;
        color: black;
    }

    /* Testo checkbox (dinamici inclusi) */
    div[data-testid="stCheckbox"] label,
    div[data-testid="stCheckbox"] span {
        color: black !important;
    }

    /* =========================
       INPUT BOX
       ========================= */
    input, textarea {
        background-color: white !important;
        color: black !important;         /* testo normale */
        border: 1px solid #000 !important;
    }

    /* Placeholder visibile */
    input::placeholder,
    textarea::placeholder {
        color: #555 !important;          /* placeholder grigio scuro */
        opacity: 1 !important;           /* forza piena opacità */
    }   

    </style>
    """,
    unsafe_allow_html=True
)


todos = functions.get_todos()

def add_todo():
    # session_state è un dizionario
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    #print(todo)
    functions.write_todos(todos)

# Legge la lista todos
todos = functions.get_todos()

# Riempie la pagina partendo da sinistra
st.set_page_config(layout="wide")

st.title('My Todo App')
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

# st.text_input(label="Enter a todo: ")
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

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

# Visualizza nel browser il dictionary
#st.session_state

