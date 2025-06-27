# from tkinter import messagebox, Toplevel, Label, Text, Button
from database import criar_tabelas
from ui import iniciar_interface

if __name__ == "__main__":
    criar_tabelas()
    iniciar_interface()
