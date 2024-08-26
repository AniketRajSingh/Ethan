import os
import subprocess

def activate_virtualenv_and_runserver():
    # Path to the virtual environment
    venv_path = os.path.join(os.getcwd(), ".venv/bin/activate")

    try:
        # Activate the virtual environment and run the Django server
        subprocess.run(f"source {venv_path} && python manage.py runserver", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    activate_virtualenv_and_runserver()
