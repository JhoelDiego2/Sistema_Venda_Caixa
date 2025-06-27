# from tkinter import messagebox, Toplevel, Label, Text, Button
from database.database import criar_tabelas
from src.ui.login import iniciar_interface

if __name__ == "__main__":
    criar_tabelas()
    iniciar_interface()
