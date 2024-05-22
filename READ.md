# Python Exam

Creating the virtual env
```bash
# Setting up virtual env named venv
python -m venv venv
```

Entering the virtual env
```bash
source venv/bin/activate
```

To connect your Python virtual environment to a Jupyter notebook (.ipynb file) as a kernel, you can follow these steps:
First, make sure your virtual environment is activated in your terminal or command prompt.
Install the ipykernel package in your virtual environment. You can do this by running the following command:
```bash
pip install ipykernel
```

Next, you need to create a kernel using the Python interpreter from your virtual environment. 
You can create a new kernel by running the following command and replacing <your-virtual-environment-name> with the name of your virtual environment:
```bash
python -m ipykernel install --user --name=<your-virtual-environment-name>
```

To exit vitual env
```bash
deactivate
```