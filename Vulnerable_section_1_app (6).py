 import subprocess
 
 def greet(name):
     print(f"Hello, {name}!")
 
 def run_command(cmd):
    # Kerentanan: menggunakan shell=True dan input tidak tervalidasi
    subprocess.call(cmd, shell=True)
 
 if __name__ == "__main__":
     name = input("Enter your name: ")