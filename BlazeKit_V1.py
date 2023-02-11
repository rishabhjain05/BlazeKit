import tkinter as tk
import subprocess

def brew_kubectl():
    result = subprocess.run(['brew', 'install', 'kubectl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "Output of 'brew install kubectl':\n")
    text_widget.insert(tk.END, output)

def cluster_health():
    result = subprocess.run(['kubectl', 'get', '--raw', '/readyz?verbose'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get --raw='/readyz?verbose'':\n")
    text_widget.insert(tk.END, output)

def show_pods():
    result = subprocess.run(['kubectl', 'get', 'pods'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get pods':\n")
    text_widget.insert(tk.END, output)

def show_nodes():
    result = subprocess.run(['kubectl', 'get', 'nodes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get nodes':\n")
    text_widget.insert(tk.END, output)

# Change the name of window
root = tk.Tk()
root.title("BlazeKit")

# Set the default window size to 800x800
root.geometry("900x1000")

# Button adding and creation

button = tk.Button(root, text="Install Kubectl", command=brew_kubectl)
button.pack(anchor="nw", padx=10, pady=5)

button = tk.Button(root, text="Cluster Health", command=cluster_health)
button.pack(anchor="n", padx=1, pady=1)

button = tk.Button(root, text="Show Pods", command=show_pods)
button.pack(anchor="nw", padx=10, pady=5)

button = tk.Button(root, text="Show Nodes", command=show_nodes)
button.pack(anchor="nw", padx=10, pady=5)

label_result = tk.Label(root, text="")
button.pack()

text_widget = tk.Text(root, wrap=tk.WORD, bg='white')
text_widget.pack(fill=tk.BOTH, expand=True)

scroll = tk.Scrollbar(text_widget, command=text_widget.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text_widget['yscrollcommand'] = scroll.set

root.mainloop()
