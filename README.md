# Securaze Wipe Audit Tool (for Single Disks)


## Features

	- Check if a system's drive has been wiped by MSN.
    - One click to download Work report for successful wipes.
    - One click to generate and save a simple .txt audit report.
    - One click to view device on Securaze dashboard.
    - Convenient links to manufacturer support pages

## Usage
➡️ **Recommended**  ⬅️
Use on the Web:  
[Wipe Audit Tool @ Streamlit Community Cloud](https://wipe-audit-tool.streamlit.app/)

## Known Issues
**Severity:** Low

No "return"/"enter" key handling during main program.   
*Workaround:*   
Use the mouse to click the "🔍 Audit" button.

## Limitations
💽 If multiple drives are detected, the program just provides a link to the portal.
🗒️ Audit report can only be generated if the wipe is successful on a single-disk machine.
🗒️ Audit reports are stored locally, not on the cloud.  

## Changelog
Apr 18 2024 **Version 0.1 - 0.6**
 - **🌱 Initial Development**

Apr 19 2024 **Version 0.7 Pre-Test**
 - **🔄 Rewrote to improve logic flow**
 - **🛠️ Fixed redundant API requests**
 - **🆕 Reworked UI to include sidebar**
 
 Apr 20 2024 **Version 0.8 Rolling**
- **🏗️ Improved verbose feedback**
- **✏️ Renamed "Wipe Report" to "Work Report"**
- **🛠️ Fixed various string inconsistencies**
- **🛠️ Fixed some UI elements appearing too early**
- **🆕 Added size toggle for wipe result element**
- **🆕 Added toggle button in sidebar for UI effects**
- **🆕 Added Useful Links section to sidebar**
- **✨ Polished login functionality**

 Apr 21 2024 **Version 0.8 Rolling 2**
- **🆕 Added favicon**
- **✨ Improved user experience**  
- **🏗️ Added a check to see if multiple drives are installed.**
   
**Next: Test**
## Libraries
|streamlit|streamlit-card|streamlit-extras|requests|
|--|--|--|--|
|Web UI for Python|Wipe Pass or Fail Card|Screen Effects| API HTTPS Requests|

## Security Information
[Streamlit • Trust and Security](https://streamlit.io/security)
