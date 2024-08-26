import subprocess

def runserver():
    subprocess.run("source .venv/bin/activate && python manage.py runserver", shell=True)

if __name__ == "__main__":
    runserver()
