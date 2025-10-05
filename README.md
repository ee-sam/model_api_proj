# **0.0 Goal**
### **0.1 Exposing a Transformer Model as a RESTful Microservice**
- Use FastAPI to wrap a T5-based summarization model as a backend microservice.
- Expose the model’s summarization feature through RESTful API endpoints.
 - Create a PySide6 local UI that communicates with the API.
- Build understanding of how to integrate machine learning models into applications via microservices.


# **1.0 Devp**

### **1.1 Activate PowerShell to Develop GUI using Pyside6** 

1. In VS code, open new PowerShell(PS) terminal.
2. Enter the path where vitual environment is created:
`cd /path/to/.venv`
3. To prevent error like "running scripts is disabled on this system", open PS as an administrator and run:
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
4. Activate the virtual env: `Scripts/activate.ps1`
5. Run the command below to activate the UI designer: `pyside6-designer`

### **1.2 UI Development using PySide6**
1. Save the ui desgined in .ui under the `/frontend` folder and convert the .ui file to .py in the terminal: `pyside6-uic frontend/main_view.ui -o frontend/main_view_ui.py`
2. Create a main_view.py to execute the main_view_ui.py
3. Run the command: `python view/main_view.py` for runtime execution of GUI


### **1.3 Frontend with MVC Architecture setup**
1. Separate the functions into `main_model.py`, `main_view.py`, and `main_controller.py`, where `main.py` will initialize all three modules.
2. Implement the `main_model.py` module to call the exposed API for running the summarizer.


### **1.4 Backend microservice development with FastAPI**
1. 


### **1.5 Launch the microservice**
1. Change directory cd to the location where the backend/ folder is located.
2. Run the service (Option 1): `uvicorn backend.summarizer:app --reload`, (Option 2): `python backend/summarizer.py`

 