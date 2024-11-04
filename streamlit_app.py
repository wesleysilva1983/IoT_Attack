import streamlit as st

with open("graphic.py") as f:
    exec(f.read())

with open("model.py") as f:
    exec(f.read())
