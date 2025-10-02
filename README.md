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
1. Save the ui desgined in .ui under the `/view` folder and convert the .ui file to .py in the terminal: `pyside6-uic view/main_view.ui -o view/main_view_ui.py`
2. Create a main_view.py to execute the main_view_ui.py
3. Run the command: `python view/main_view.py` for runtime execution of GUI



