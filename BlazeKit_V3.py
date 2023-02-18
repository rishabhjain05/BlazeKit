import tkinter as tk
import subprocess

# Create the main window and name that window
root = tk.Tk()
root.geometry("1620x1080")
root.title("BlazeKit")

# Create a frame for the left column
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

def clear_screen():
    text_widget.delete('1.0', tk.END)
    result = subprocess.run(['clear'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, output)

def brew_kubectl():
    result = subprocess.run(['brew', 'install', 'kubectl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'brew install kubectl':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone")

def cluster_health():
    result = subprocess.run(['kubectl', 'get', '--raw', '/readyz?verbose'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get --raw='/readyz?verbose'':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone")

def show_pods():
    result = subprocess.run(['kubectl', 'get', 'pods'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get pods':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone")

def show_pods_in_detail():
    result = subprocess.run(['kubectl', 'get', 'pods', '-o', 'wide'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get pods -o wide':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone")

def show_nodes():
    result = subprocess.run(['kubectl', 'get', 'nodes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get nodes':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone")

def show_nodes_in_detail():
    result = subprocess.run(['kubectl', 'get', 'nodes', '-o', 'wide'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get nodes -o wide':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone")

# Button Configuration Secction

button = tk.Button(left_frame, text=f"Clear Screen", command=clear_screen)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Install Kubectl", command=brew_kubectl)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Cluster Health", command=cluster_health)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Show Pods", command=show_pods)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"View Pods Detail", command=show_pods_in_detail)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Show Nodes", command=show_nodes)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"View Nodes Detail", command=show_nodes_in_detail)
button.pack(side=tk.TOP, pady=5)

    # button = tk.Button(left_frame, text=f"Install Kubectl {i+1}", command=brew_kubectl)
    # button.pack(side=tk.TOP, pady=5)

# Create a frame for the right column
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a text input in the right frame
text_widget = tk.Text(right_frame)
text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()