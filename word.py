from pdf2docx import Converter

def convert_pdf_to_word(pdf_path):
    """
    Convert PDF to Word (.docx)
    """
    docx_path = pdf_path.replace(".pdf", ".docx")

    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    return docx_path
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def convert_file():
    file_path = entry.get()

    if file_path == "":
        messagebox.showerror("Error", "Please select a PDF file")
        return

    try:
        output = convert_pdf_to_word(file_path)
        messagebox.showinfo("Success", f"Word File Created:\n{output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))



root = tk.Tk()
root.title("PDF to Word Converter")
root.geometry("420x200")

entry = tk.Entry(root, width=45)
entry.pack(pady=20)

tk.Button(root, text="Browse PDF File", command=browse_file).pack(pady=5)
tk.Button(root, text="Convert to Word", command=convert_file).pack(pady=15)

root.mainloop()