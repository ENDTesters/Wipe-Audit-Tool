

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
 
# Known Issues
**Severity:** Mild  

When user login is complete, the login UI remains visible in the sidebar until the next UI refresh.  

**Severity:** Moderate  

No "return" key handling, annoying during logon. The tool is best used with the mouse and/or tab navigation.  
# Limitations
Only single-disk machines have been tested so far.  
Audit report can only be generated if the wipe is successful.  
Audit reports must be manually generated.  
Audit reports are stored locally, not on the cloud.  

# Changelog
Apr 18 2024 **Version 0.1 - 0.7**
 - **Initial Development**

Apr 19 2024 **Version 0.8 Pre-Test**
 - **Rewrote to improve logic flow**
 - **Fixed redundant API requests**
 - **Reworked UI to include sidebar**
 
 Apr 20 2024 **Version 0.8 Pre-Test**
 - **Improved verbose feedback**
 - **Rename "Wipe Report" to "Work Report"**
 - **Fixed various string inconsistencies**
 - **Fixed some UI elements appearing too early**
- **Added toggle button in sidebar for Wipe Card element**
- **Added toggle button in sidebar for UI effects**
- **Added Useful Links section to sidebar**
- **Added organization-specific links**

**Next: Test in Production**
# Libraries
|streamlit|streamlit-card|streamlit-extras|requests|
|--|--|--|--|
|Web UI for Python|Wipe Pass or Fail Card|Screen Effects| API HTTPS Requests|
# Potential Features
Add WMS integration.  
Parse work report .pdf to extract more information.  
More features would be added to a seperate tab to keep execution time reasonable.  
