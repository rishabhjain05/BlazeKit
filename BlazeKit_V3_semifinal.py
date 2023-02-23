import tkinter as tk
from tkinter import scrolledtext, Text
import subprocess
import tkinter.simpledialog as simpledialog

# Create the main window and name that window
root = tk.Tk()
root.geometry("1620x1080")
root.title("BlazeKit")

# Create a frame for the left column
left_frame = tk.Frame(root) #add bg tag after comma to ad background to button panel. (root, bg = 'red')
left_frame.pack(side=tk.LEFT, fill=tk.Y)

def clear_screen():
    text_widget.delete('1.0', tk.END)
    subprocess.run(['clear'])

def brew_kubectl():
    result = subprocess.run(['brew', 'install', 'kubectl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'brew install kubectl':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def download_aws_cli():
    result = subprocess.run(['curl', 'https://awscli.amazonaws.com/AWSCLIV2.pkg', '-o', 'AWSCLIV2.pkg'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = subprocess.run(['curl', 'sudo', 'installer', '-pkg', 'AWSCLIV2.pkg', '-target', '/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'curl https://awscli.amazonaws.com/AWSCLIV2.pkg -o AWSCLIV2.pkg':\n")
    text_widget.insert(tk.END, "\nOutput of 'curl sudo installer -pkg AWSCLIV2.pkg -target /':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def cluster_health():
    result = subprocess.run(['kubectl', 'get', '--raw', '/readyz?verbose'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get --raw='/readyz?verbose'':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def show_pods():
    result = subprocess.run(['kubectl', 'get', 'pods'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get pods':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def show_pods_in_detail():
    result = subprocess.run(['kubectl', 'get', 'pods', '-o', 'wide'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get pods -o wide':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def show_nodes():
    result = subprocess.run(['kubectl', 'get', 'nodes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get nodes':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def show_nodes_in_detail():
    result = subprocess.run(['kubectl', 'get', 'nodes', '-o', 'wide'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get nodes -o wide':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def show_deployments():
    result = subprocess.run(['kubectl', 'get', 'deployments'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    text_widget.insert(tk.END, "\nOutput of 'kubectl get nodes -o wide':\n")
    text_widget.insert(tk.END, output)
    text_widget.insert(tk.END, "\nDone\n")

def show_deployment_details():
    deployment_name = simpledialog.askstring("Deployment Name", "Enter the deployment name:")

    if deployment_name is not None and deployment_name.strip() != "":
        command = ['kubectl', 'describe', 'deployment', deployment_name]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode() + result.stderr.decode()
        text_widget.insert(tk.END, f"\nOutput of 'kubectl describe deployment {deployment_name}':\n")
        text_widget.insert(tk.END, output)
        text_widget.insert(tk.END, "\nDone\n")
    
    elif deployment_name is not None:
        # user clicked "OK" without entering a name
        text_widget.insert(tk.END, "Error: Please enter a deployment name.\n")

# Button Configuration Secction

button = tk.Button(left_frame, text=f"Clear Screen", command=clear_screen, fg="red")
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Install Kubectl", command=brew_kubectl)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Install AWS_CLI", command=download_aws_cli)
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

button = tk.Button(left_frame, text=f"Show Deployments", command=show_deployments)
button.pack(side=tk.TOP, pady=5)

button = tk.Button(left_frame, text=f"Show Deployment Details", command=show_deployment_details)
button.pack(side=tk.TOP, pady=5)

# Create a frame for the right column
right_frame = tk.Frame(root, bd=2, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text input in the right frame
text_widget = Text(right_frame, yscrollcommand=scrollbar.set, wrap=tk.WORD)
text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Configure the scrollbar to link to the text widget
scrollbar.config(command=text_widget.yview )

# Start the main event loop
root.mainloop()
