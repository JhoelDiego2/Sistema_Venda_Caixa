import customtkinter as ctk
from tkinter import messagebox
from src.controller.user import autenticar
from PIL import Image

def iniciar_interface():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("         MITA CONTROL  |  LOGIN     ")
    app.geometry("1000x600")
    app.grid_columnconfigure(0, weight=1)  
    app.grid_columnconfigure(1, weight=1) 
    app.grid_rowconfigure(0, weight=1)

    frame_imagem = ctk.CTkFrame(app, width=500, height=600)
    frame_imagem.grid(row=0, column=0, sticky="nsew")
    

    ax_imagem = Image.open('src/assets/login.png')
    img_ctk = ctk.CTkImage(light_image=ax_imagem, dark_image=ax_imagem, size=(500, 600))
    label_img = ctk.CTkLabel(frame_imagem, image=img_ctk )
    label_img.grid(row=0, column=0, sticky="nsew")

    frame_form = ctk.CTkFrame(app, width=500, height=600)
    frame_form.grid(row=0, column=1, sticky="nsew")

    ctk.CTkLabel(frame_form, text="Bem-vindo de volta!", font=("Arial", 40), text_color="blue").grid(row=0, column=0, pady=50)

    ctk.CTkLabel(frame_form, text="Faça seu login para entrar na sua conta", font=("Arial", 20), text_color="blue").grid(row=1, column=0,)


    ctk.CTkLabel(frame_form, text="E-mail: ").grid(row=2, column=0, padx=10)
    ipt_email = ctk.CTkEntry(frame_form, placeholder_text="seuemail@gmail.com")
    ipt_email.grid(row=4, column=0, padx=10, pady=(0, 20))

    ctk.CTkLabel(frame_form, text="Senha: ").grid(row=3, column=0, padx=10)
    ipt_senha = ctk.CTkEntry(frame_form, show="*",  placeholder_text="**********")
    ipt_senha.grid(row=6, column=0, padx=10, pady=(0, 20))

    def ao_cadastrar():
        ax_email = ipt_email.get()
        ax_senha = ipt_senha.get()
        print('Email = ' + ax_email + 'SENHA' +  ax_senha)
        response = autenticar(ax_email, ax_senha)
        if response['ok']:
            messagebox.showinfo("Sucesso", "Redirecionando!")
        else:
            messagebox.showerror("Erro", response['msg'])

    btn_entrar = ctk.CTkButton(frame_form, text="ENTRAR", command=ao_cadastrar, 
                               hover_color="green", corner_radius=10, border_color="#FFCC70",  border_width=2
                               )
    btn_entrar.grid(row=7, column=0, pady=20, padx=10, sticky="ew")

    app.mainloop()
