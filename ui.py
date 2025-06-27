import customtkinter as ctk
from tkinter import messagebox
from controller import autenticar

def iniciar_interface():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("MITA CONTROL")
    app.geometry("1000x800")

    ctk.CTkLabel(app,  text="LOGIN", font=("Arial", 30), text_color="blue" ).pack()
    # label.place(relx=0.5, rely=0, anchor="center")

    ctk.CTkLabel(app, text="E-mail").pack()
    ipt_email = ctk.CTkEntry(app)
    ipt_email.pack()

    ctk.CTkLabel(app, text="Senha").pack()
    ipt_senha = ctk.CTkEntry(app)
    ipt_senha.pack()

    def ao_cadastrar():
        ax_email = ipt_email.get()
        ax_senha = ipt_senha.get()
        response = autenticar(ax_email, ax_senha)
        if response['ok']:
            messagebox.showinfo("Sucesso", "Redirecionando!")
        else:
            messagebox.showerror("Erro", response['msg'])

    ctk.CTkButton(app, text="ENTRAR", command=ao_cadastrar).pack(pady=20)

    app.mainloop()