import tkinter as tk
import subprocess

def run_command():
    result = subprocess.run(['brew', 'install', 'kubectl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text.insert(tk.END, "Output of 'brew install kubectl':\n")
    text.insert(tk.END, output)

def run_command1():
    result = subprocess.run(['kubectl', 'get', '--raw', '/readyz?verbose'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text.insert(tk.END, "\nOutput of 'kubectl get --raw='/readyz?verbose'':\n")
    text.insert(tk.END, output)

root = tk.Tk()
root.geometry('400x400')

run_command_button = tk.Button(root, text='Run Command', command=run_command)
run_command_button.pack()

run_command_button = tk.Button(root, text='Run Command', command=run_command1)
run_command_button.pack()

text = tk.Text(root, wrap=tk.WORD, bg='lightgray')
text.pack(fill=tk.BOTH, expand=True)

scroll = tk.Scrollbar(text, command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text['yscrollcommand'] = scroll.set

root.mainloop()
