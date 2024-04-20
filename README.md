# Securaze Wipe Audit Tool
Features:

	- Determine if a system's drive has been wiped by MSN.
    - Shortcut to download Work report.
    - Generates a simple audit report in .txt format.
    - Click Wipe Card to view on Securaze Dashboard.


# Usage
**Recommended:**  
Use on the Web:  
[Wipe Audit Tool @ Streamlit Community Cloud](https://wipecheck.streamlit.app/)

Or, use locally on Windows:

 1. Install Python 3.11.3 or higher.
 2. Download code as a .zip file.
 3. Extract the code to a directory of your choice.
 4. Run requirements.bat to install dependencies.
 5. Open a terminal and cd to your code directory.
 6. Type "streamlit run Wipe-Audit-Tool.py" and press Enter.

# Libraries
|streamlit|streamlit-card|streamlit-extras|requests|
|--|--|--|--|
|Web UI for Python|Wipe Pass or Fail Card|Screen Effects| API HTTPS Requests|
# Known Issues
When user login is complete, the login text boxes remain visible until the next UI refresh. I could not easily fix this issue, but since the log-in is in the sidebar, it's mostly just a mild annoyance.
