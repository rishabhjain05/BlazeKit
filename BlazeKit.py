import tkinter as tk
import subprocess

def brew_kubectl():
    result = subprocess.run(['brew', 'install', 'kubectl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text.insert(tk.END, output)

def cluster_health():
    output = subprocess.run(['kubectl', 'get', '--raw', '/readyz?verbose'], capture_output=True, text=True)
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, output.stdout)
    text_widget.config(state="disabled")

def show_pods():
    output = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, output.stdout)
    text_widget.config(state="disabled")

def show_nodes():
    output = subprocess.run(["kubectl", "get", "nodes"], capture_output=True, text=True)
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, output.stdout)
    text_widget.config(state="disabled")

# Change the name of window
root = tk.Tk()
root.title("BlazeKit")

# Set the default window size to 800x800
root.geometry("900x1000")

# Button adding and creation

button = tk.Button(root, text="Install Kubectl", command=brew_kubectl)
button.pack(anchor="nw", padx=10, pady=5)

button = tk.Button(root, text="Cluster Health", command=cluster_health)
button.pack(anchor="nw", padx=10, pady=5)

button = tk.Button(root, text="Show Pods", command=show_pods)
button.pack(anchor="nw", padx=10, pady=5)

button = tk.Button(root, text="Show Nodes", command=show_nodes)
button.pack(anchor="nw", padx=10, pady=5)

label_result = tk.Label(root, text="")
button.pack(anchor="w", padx=10, pady=5)

text_widget = tk.Text(root, state="disabled")
text_widget.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(text_widget)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# brew_install

text = tk.Text(root, wrap=tk.WORD, bg='white')
text.pack(fill=tk.BOTH, expand=True)

# brew_install
scroll = tk.Scrollbar(text, command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text['yscrollcommand'] = scroll.set

root.mainloop()
