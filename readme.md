
# Securaze Wipe Audit Tool
Features:

	- Check if a system's drive has been wiped by MSN.
    - One click to download Work report for successful wipes.
    - One click to generate and save a simple audit report in .txt format for successful wipes.
    - One click to view device on Securaze dashboard.


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
**Severity:** Mild  

When user login is complete, the login UI remains visible in the sidebar until the next UI refresh.

**Severity:** Mild  

No "return" key handling. The tool is designed to be used with the mouse or tab keys.
# Current Limitations
Only single-disk machines have been tested so far.
Audit report can only be generated if the wipe is successful.
Audit reports must be manually generated.
Audit reports are stored locally, not on the cloud.
# Potential Features
Add WMS integration.
Parse work report .pdf to extract more information.
# Changelog
Apr 18 2024 **Version 0.1:**

 - **Initial Release**

Apr 19 2024 **Version 0.2:**
 - **Rewrote to improve logic flow**
 - **Fixed redundant API requests**
 - **Reworked UI to include sidebar**
 
 Apr 20 2024 **Version 0.3:**
 - **Improved verbose feedback**
 - **Rename "Wipe Report" to "Work Report".**
 - **Fixed various string inconsistencies.**

Apr 20 2024 **Version 0.4**
- **Added toggle button in sidebar for UI effects**

Apr 20 2024 **Version 0.5**
- **Added toggle button in sidebar to enable or disable the Wipe Card UI element.**