import customtkinter as ctk
import pymysql
import pandas as pd
from tkinter import messagebox, Toplevel, Label, Text, Button

conexao = pymysql.connect(
    host='localhost',
    user='loja_cristina',
    password= 'Urubu123#',   
    database='loja_cristina',
    port=3306,
)
cursor = conexao.cursor()

DB_CONFIG = {
'host' : 'localhost',
'user' : 'loja_cristina',
'password' : 'Urubu123',
'database' : 'loja_cristina',
'port' : 3306,
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def get_db_connection():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        return conn
    except pymysql.Error as err:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco de dados: {err}\n"
                                                "Verifique as configurações em DB_CONFIG e se o servidor MySQL está rodando.")
        return None
