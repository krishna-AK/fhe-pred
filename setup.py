import subprocess
import venv
import os

def create_virtualenv(env_path):
    venv.create(env_path, with_pip=True)

def install_requirements(env_path):
    pip_path = os.path.join(env_path, "Scripts", "pip.exe")
    requirements_path = os.path.join(os.getcwd(), "requirements.txt")
    subprocess.check_call([pip_path, "install", "-r", requirements_path])

if __name__ == "__main__":
    env_name = "venv"
    env_path = os.path.join(os.getcwd(), env_name)

    print(f"Creating virtual environment in {env_path}...")
    create_virtualenv(env_path)

    print("Installing requirements...")
    install_requirements(env_path)

    print("Setup complete! Activate the virtual environment by running:")
    print(f"{env_path}\\Scripts\\activate")