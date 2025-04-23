import os
import subprocess
import tkinter as tk
import threading
import customtkinter as ctk
from tkinter import scrolledtext
from PIL import Image, ImageTk

# Set appearance mode and default color theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ActivatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Windows & Office Activator 11")
        self.geometry("1000x650")
        self.minsize(900, 550)
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        
        # Create sidebar frame with buttons
        self.sidebar_frame = ctk.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(12, weight=1)
        
        # App title in sidebar
        self.title_label = ctk.CTkLabel(self.sidebar_frame, text="Activator 11", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Create utility categories
        self.main_utilities = {
            "Check Activation Status": "Check_Activation_Status.cmd",
            "Change Windows Edition": "Change_Windows_Edition.cmd",
            "Change Office Edition": "Change_Office_Edition.cmd",
            "Extract OEM Folder": "Extract_OEM_Folder.cmd",
            "Troubleshoot": "Troubleshoot.cmd"
        }
        
        self.activators = {
            "HWID Activation": os.path.join("Activators", "HWID_Activation.cmd"),
            "KMS38 Activation": os.path.join("Activators", "KMS38_Activation.cmd"),
            "Online KMS Activation": os.path.join("Activators", "Online_KMS_Activation.cmd"),
            "Ohook Activation AIO": os.path.join("Activators", "Ohook_Activation_AIO.cmd"),
            "TSforge Activation": os.path.join("Activators", "TSforge_Activation.cmd")
        }
        
        # Main Utilities Label
        self.utilities_label = ctk.CTkLabel(self.sidebar_frame, text="Main Utilities", font=ctk.CTkFont(size=14, weight="bold"))
        self.utilities_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")
        
        # Create buttons for main utilities
        for i, (label, cmd_file) in enumerate(self.main_utilities.items()):
            button = ctk.CTkButton(
                self.sidebar_frame, 
                text=label,
                command=lambda cmd=cmd_file: self.run_cmd_file(cmd)
            )
            button.grid(row=i+2, column=0, padx=20, pady=5, sticky="w")
        
        # Activators Label
        self.activators_label = ctk.CTkLabel(self.sidebar_frame, text="Activation Tools", font=ctk.CTkFont(size=14, weight="bold"))
        self.activators_label.grid(row=7, column=0, padx=20, pady=(20, 5), sticky="w")
        
        # Create buttons for activators
        for i, (label, cmd_file) in enumerate(self.activators.items()):
            button = ctk.CTkButton(
                self.sidebar_frame, 
                text=label,
                command=lambda cmd=cmd_file: self.run_cmd_file(cmd),
                fg_color="#b02a37",  # Highlight activator buttons with a different color
                hover_color="#bb2d3b"
            )
            button.grid(row=i+8, column=0, padx=20, pady=5, sticky="w")
        
        # Appearance mode toggle
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=13, column=0, padx=20, pady=(20, 0), sticky="w")
        
        self.appearance_mode_option = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["System", "Light", "Dark"],
            command=self.change_appearance_mode
        )
        self.appearance_mode_option.grid(row=14, column=0, padx=20, pady=(5, 20), sticky="w")
        
        # Right side frame with output console
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        # Output header label
        self.output_header = ctk.CTkLabel(
            self.main_frame, 
            text="Welcome to Activator 11",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.output_header.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        # Output console
        self.output_console = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            background="#212121",
            foreground="#FFFFFF",
            font=("Consolas", 10)
        )
        self.output_console.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.output_console.config(state=tk.NORMAL)
        self.output_console.insert(tk.END, "Select a utility from the sidebar to get started.\n\n")
        self.output_console.insert(tk.END, "• Main utilities help you check status and change editions\n")
        self.output_console.insert(tk.END, "• Activation tools (highlighted in red) are used to activate Windows and Office\n\n")
        self.output_console.insert(tk.END, "Note: Some operations may require administrator privileges.\n")
        self.output_console.config(state=tk.DISABLED)
        
        # Status bar
        self.status_bar = ctk.CTkLabel(self.main_frame, text="Ready", anchor="w")
        self.status_bar.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="w")
        
        # Add a stop button for long-running commands
        self.stop_button = ctk.CTkButton(
            self.main_frame,
            text="Stop Process",
            command=self.stop_current_process,
            fg_color="#bb2d3b",
            hover_color="#b02a37",
            state="disabled"
        )
        self.stop_button.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="e")
        
        # Process tracking
        self.current_process = None
    
    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def run_cmd_file(self, cmd_file):
        # Clear the console
        self.output_console.config(state=tk.NORMAL)
        self.output_console.delete(1.0, tk.END)
        self.output_console.config(state=tk.DISABLED)
        
        # Update header and status
        cmd_name = os.path.basename(cmd_file)
        self.output_header.configure(text=f"Running: {cmd_name}")
        self.status_bar.configure(text="Executing command...")
        
        # Enable stop button
        self.stop_button.configure(state="normal")
        
        # Run the command in a separate thread
        thread = threading.Thread(target=self._execute_cmd, args=(cmd_file,))
        thread.daemon = True
        thread.start()
    
    def _execute_cmd(self, cmd_file):
        try:
            # Build the full path to the CMD file
            if not cmd_file.startswith("Activators"):
                cmd_path = os.path.join("activation", cmd_file)
            else:
                cmd_path = os.path.join("activation", cmd_file)
            
            # Get the directory of the CMD file
            cmd_dir = os.path.dirname(os.path.abspath(cmd_path))
            
            # Log information about execution
            self.update_console(f"Executing: {cmd_path}")
            self.update_console(f"Working directory: {cmd_dir}")
            self.update_console("Command output:")
            self.update_console("-" * 60)
            
            # Create startupinfo to prevent new window
            startupinfo = None
            if hasattr(subprocess, 'STARTUPINFO'):
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            # Start the process with correct working directory
            # Use cmd.exe directly (not using shell=True to avoid PowerShell)
            cmd_exe = os.path.join(os.environ['SYSTEMROOT'], 'System32', 'cmd.exe')
            self.current_process = subprocess.Popen(
                [cmd_exe, "/c", os.path.abspath(cmd_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                stdin=subprocess.PIPE,
                shell=False,  # Important: don't use shell=True as it might invoke PowerShell
                text=True,
                errors='replace',
                cwd=cmd_dir,
                startupinfo=startupinfo
            )
            
            # Read output line by line and update the console
            # Remove control sequences and escape characters
            import re
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            
            for line in iter(self.current_process.stdout.readline, ''):
                # Clean line of terminal control sequences
                clean_line = ansi_escape.sub('', line.strip())
                # Skip empty lines after cleaning
                if clean_line:
                    self.update_console(clean_line)
            
            # Wait for the process to complete
            self.current_process.wait()
            
            # Update status
            if self.current_process.returncode == 0:
                self.update_status(f"Command completed successfully")
            else:
                self.update_status(f"Command failed with exit code {self.current_process.returncode}")
            
            # Reset process and disable stop button
            self.current_process = None
            self.after(0, lambda: self.stop_button.configure(state="disabled"))
        
        except Exception as e:
            self.update_console(f"Error: {str(e)}")
            self.update_status("Error occurred during execution")
            self.current_process = None
            self.after(0, lambda: self.stop_button.configure(state="disabled"))
    
    def stop_current_process(self):
        if self.current_process:
            try:
                # Try to terminate the process
                self.current_process.terminate()
                self.update_console("Process terminated by user.")
                self.update_status("Process terminated")
                self.stop_button.configure(state="disabled")
            except Exception as e:
                self.update_console(f"Error stopping process: {str(e)}")
    
    def update_console(self, text):
        def _update():
            self.output_console.config(state=tk.NORMAL)
            self.output_console.insert(tk.END, text + "\n")
            self.output_console.see(tk.END)
            self.output_console.config(state=tk.DISABLED)
        
        self.after(0, _update)
    
    def update_status(self, text):
        def _update():
            self.status_bar.configure(text=text)
        
        self.after(0, _update)

if __name__ == "__main__":
    app = ActivatorApp()
    app.mainloop() 