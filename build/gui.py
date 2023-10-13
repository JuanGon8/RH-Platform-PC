from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\juan_\OneDrive\Documentos\TRABAJO\Repos\RH-Platform-PC\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Conéctate a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema"
)

if db.is_connected():
    print("Conexión a la base de datos exitosa")
else:
    print("No se pudo conectar a la base de datos")



window = Tk()

window.geometry("1280x720")
window.configure(bg="#F4F4F4")

def check_login():
    cursor = db.cursor()
    user = entry_1.get()
    password = entry_2.get()

    # Consulta SQL para verificar el inicio de sesión
    query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
    cursor.execute(query, (user, password))
    result = cursor.fetchone()

    cursor.close()

    if result:
        messagebox.showinfo("Correcto", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Usuario o contraseña incorrecta", "Usuario o contraseña incorrecta")


canvas = Canvas(
    window,
    bg = "#F4F4F4",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    701.3330078125,
    29.53125,
    1226.66650390625,
    690.46875,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    863.0,
    298.0,
    anchor="nw",
    text="Bienvenido  ",
    fill="#2E2E2E",
    font=("Poppins Black", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("a"),
    relief="flat"
)
button_1.place(
    x=1569.0,
    y=765.0,
    width=209.0,
    height=22.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    964.0,
    410.625,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=737.0,
    y=388.125,
    width=454.0,
    height=43.0
)

canvas.create_text(
    730.0,
    360.0,
    anchor="nw",
    text="Correo electrónico",
    fill="#2E2E2E",
    font=("Poppins Regular", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    964.0,
    493.625,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=737.0,
    y=471.125,
    width=454.0,
    height=43.0
)

canvas.create_text(
    730.0,
    443.0,
    anchor="nw",
    text="Contraseña",
    fill="#2E2E2E",
    font=("Poppins Regular", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_login(),
    relief="flat"
)
button_2.place(
    x=816.0,
    y=568.0,
    width=296.0,
    height=48.0
)

canvas.create_text(
    755.0,
    529.0,
    anchor="nw",
    text="Recordar mi contraseña",
    fill="#2E2E2E",
    font=("Poppins Regular", 15 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=730.0,
    y=530.0,
    width=18.0,
    height=18.0
)

canvas.create_text(
    1316.0,
    926.0,
    anchor="nw",
    text="¿No tienes cuenta? Registrate",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    964.0,
    188.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    320.0,
    360.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
