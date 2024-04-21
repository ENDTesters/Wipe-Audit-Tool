# Securaze Wipe Audit Tool


## Features

	- Check if a system's drive has been wiped by MSN.
    - One click to download Work report for successful wipes.
    - One click to generate and save a simple .txt audit report.
    - One click to view device on Securaze dashboard.
    - Convenient links to manufacturer support pages
    - Unique links for GEODIS


## Usage
➡️ **Recommended**  ⬅️
Use on the Web:  
[Wipe Audit Tool @ Streamlit Community Cloud](https://wipecheck.streamlit.app/)

Or, use locally on Windows:

 1. Install Python 3.11.3 or higher.
 2. Download code as a .zip file.
 3. Extract the code to a directory of your choice.
 4. Run requirements.bat to install dependencies.
 5. Open a terminal and cd to your code directory.
 6. Type "streamlit run Wipe-Audit-Tool.py" and press Enter.  
 
## Known Issues
**Severity:** Low

No "return"/"enter" key handling during main program.   
*Workaround:*   
Use the mouse to click the "🔍 Audit" button.
## Limitations
💽 Only single-disk machines have been tested so far.  
🗒️ Audit report can only be generated if the wipe is successful.  
🗒️ Audit reports are stored locally, not on the cloud.  

## Changelog
Apr 18 2024 **Version 0.1 - 0.6**
 - **🌱 Initial Development**

Apr 19 2024 **Version 0.7 Pre-Test**
 - **🔄 Rewrote to improve logic flow**
 - **🛠️ Fixed redundant API requests**
 - **🆕 Reworked UI to include sidebar**
 
 Apr 20 2024 **Version 0.8 Rolling Pre-Test**
- **🏗️ Improved verbose feedback**
- **✏️ Renamed "Wipe Report" to "Work Report"**
- **🛠️ Fixed various string inconsistencies**
- **🛠️ Fixed some UI elements appearing too early**
- **🆕 Added size toggle for wipe result element**
- **🆕 Added toggle button in sidebar for UI effects**
- **🆕 Added Useful Links section to sidebar**
- **🆕 Added organization-specific links**
- **✨ Polished login functionality**

**Next: Test in Production**
## Libraries
|streamlit|streamlit-card|streamlit-extras|requests|
|--|--|--|--|
|Web UI for Python|Wipe Pass or Fail Card|Screen Effects| API HTTPS Requests|
## Potential Features
Add WMS integration.  
Parse work report .pdf to extract more information.  
More features would be added to a seperate tab to keep execution time reasonable.  
## Security Information
[Streamlit • Trust and Security](https://streamlit.io/security)