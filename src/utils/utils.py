# utils.py

import streamlit as st

def apply_styles():
    st.markdown(
    """
    <style>
    .chat-container {
        max-height: 70vh;  /* Set the height of the chat container */
        overflow-y: auto;  /* Enable scrolling if messages overflow */
        padding: 10px;
        border-bottom: 2px solid #ccc;
        margin-bottom: 60px;  /* Space at the bottom to not overlap with the input */
    }

    .input-container {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: white;
        padding: 10px;
        border-top: 2px solid #ccc;
        z-index: 1000;  /* Ensures it stays on top */
    }

    .input-container input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }

    /* Ensure body takes the full height to allow scrollable content above the fixed input box */
    body {
        margin: 0;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True
    )
