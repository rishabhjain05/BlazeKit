import tkinter as tk
import subprocess

def show_output():
    output = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, output.stdout)
    text_widget.config(state="disabled")

root = tk.Tk()
root.title("Kubectl Output")

button = tk.Button(root, text="Show Pods", command=show_output)
button.pack()

text_widget = tk.Text(root, state="disabled")
text_widget.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(text_widget)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

root.mainloop()
