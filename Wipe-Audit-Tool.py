# Wipe Audit Tool Version 0.5
# Written by Noah Dailey
# Usable by any company that uses Securaze Work on computer systems
# Still learning to program... some stuff is done inefficiently
# However, the program's scope is pretty simple, and its' functionality should be fairly complete at this point.

# Requirements

import time
from datetime import date
import datetime
import streamlit as st
from streamlit_card import card
import streamlit_extras as st_extras
from streamlit_extras.let_it_rain import rain
import requests as req
now = datetime.datetime.now()
today = date.today()
auditDate = today.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
st.set_page_config(page_title="Securaze Wipe Check & Audit Log Alpha", layout="centered")
col1, col2 = st.columns([1, 1])
		
# Set cross-run variables to 'unassigned' string if they aren't assigned,
# establish variables that help the rest of the program query

if 'securazeUsername' not in st.session_state:
	st.session_state['securazeUsername'] = ''
if 'securazePassword' not in st.session_state:
	st.session_state['securazePassword'] = ''
if 'loginToken' not in st.session_state:
	st.session_state['loginToken'] = ''
if 'customerID' not in st.session_state:
	st.session_state['customerID'] = ''
if 'userLoginCompleted' not in st.session_state:
	st.session_state['userLoginCompleted'] = False

# Set API variables

apiAuthLink = "https://api-us-west.securaze.com/api/auth/login"
apiProductLink = "https://api-us-west.securaze.com/api/products/search"
apiLoadLink = "https://api-us-west.securaze.com/api/products/load"
#define login function
# check to see if the session is logged in yet or not
if 'verboseMode' not in st.session_state:
	st.session_state['verboseMode'] = False
if 'showWipeCard' not in st.session_state:
	st.session_state['showWipeCard'] = True
	if st.session_state['verboseMode'] == True:
		st.toast['Showing Full Wipe Card.']
try:
	if st.session_state['loginYesorNoResponse'] == "User successfully logged in.":
		st.session_state['userLoginCompleted'] = True
		userLoginCompleted = True
except:
	if st.session_state['verboseMode'] == True:
		st.toast('Waiting for login.')
if 'uiEffectsEnabled' not in st.session_state:
			st.session_state["uiEffectsEnabled"] = True
			st.toast("UI Effects Enabled")
if 'is_expanded' not in st.session_state:
	st.session_state['is_expanded'] = True
try:
	
	if st.session_state['userLoginCompleted'] == True:
		pass
	else:
		with st.container(border=15):
			with st.sidebar:
				st.session_state['securazeUsername'] = st.text_input("Username", key='user', help='Format: username@organization')
				st.session_state['securazePassword'] = st.text_input("Password", type="password", key='pass')
				if st.button("🔓 Log In", use_container_width=True):
					try:
						loginQueryParams = {'Username': st.session_state['securazeUsername'], 'Password': st.session_state['securazePassword'], 'RememberMe': 'True' }
						securazeAPILogin = req.post(apiAuthLink, data=loginQueryParams)
						securazeAPILoginDict = securazeAPILogin.json()
						loginYesorNoResponse = securazeAPILoginDict.get('message')
						st.session_state['loginYesorNoResponse'] = securazeAPILoginDict.get('message')
						loginRequestRaw = securazeAPILoginDict.get('result')
						loginResponseData = loginRequestRaw.get("data")	
						try:
							st.session_state['loginToken'] = loginResponseData['Token']
							st.session_state['customerData'] = loginResponseData.get("Customers")
							st.session_state['customerZeroData'] = st.session_state['customerData'][0]
							st.session_state['customerName'] = st.session_state['customerZeroData']['Name']
							st.session_state['customerID'] = st.session_state['customerZeroData']['CustomerID']
							st.session_state['tokenObtained'] = True
							loginQueryParams = {'Username': st.session_state['securazeUsername'], 'Password': st.session_state['securazePassword'], 'RememberMe': 'True' }
							securazeAPILogin = req.post(apiAuthLink, data=loginQueryParams)
							securazeAPILoginDict = securazeAPILogin.json()
							st.session_state['loginYesorNoResponse'] = securazeAPILoginDict.get('message')
							loginRequestRaw = securazeAPILoginDict.get('result')
							loginResponseData = loginRequestRaw.get("data")	
							if loginYesorNoResponse == "User successfully logged in.":
								st.session_state['userLoginCompleted'] = True
							if st.session_state['verboseMode'] == True:
								st.toast("Username and password entered.")
						except:
							with st.sidebar:
								st.error("Failed to authenticate. Check your username and password.")
					except:
						st.toast("Enter your login credentials.")
except:
	if st.session_state['verboseMode'] == True:
		st.toast("An issue occured during the login process.")
if 'verboseMode' not in st.session_state:
	st.session_state['verboseMode'] = False
with st.sidebar:
	if st.button('✴️ Toggle UI Effects', use_container_width=True, help="Enable or disable emoji rain."):
		if st.session_state["uiEffectsEnabled"] == True:
			st.session_state["uiEffectsEnabled"] = False
			st.toast("UI Effects Disabled")
		else:
			st.session_state['uiEffectsEnabled'] = True
			st.toast("UI Effects Enabled")
	if st.button('🗚 Compact Wipe Results', use_container_width=True, help="Enable or disable wipe report card."):
		if st.session_state["showWipeCard"] == True:
			st.session_state["showWipeCard"] = False
			st.toast("Wipe result will be shown as a link.")
		else:
			st.session_state['showWipeCard'] = True
			st.toast("Wipe result will be displayed using the st.card library.")

	if st.button('👨‍💻 Toggle Verbose Mode', use_container_width=True, help="Extend messaging on-screen."):
		if st.session_state['verboseMode'] == False:
			st.toast("Enabled Verbose Mode.")
			st.session_state['verboseMode'] = True
		else:
			st.toast("Disabled Verbose Mode.")
			st.session_state['verboseMode'] = False

if st.session_state['userLoginCompleted'] == False:
	userLoginCompletedStr = "False"
elif st.session_state['userLoginCompleted'] == True:
	userLoginCompletedStr = "True"
	serialNumber = st.text_input("Enter the Serial Number then Click Audit")
	if st.button('🔍 Audit', use_container_width=True, help="Click to check if the entered serial has been wiped."):
		try:
			st.session_state['serialNumber'] = serialNumber
			serialSearchParams = {'CustomerID': st.session_state['customerID'], 'SearchInput': st.session_state['serialNumber'], 'Token': st.session_state['loginToken']}
			serialSearch = req.post(apiProductLink, data=serialSearchParams)
			serialSearchDict = serialSearch.json()
			serialSearchResults = serialSearchDict.get("result")
			serialSearchResultsData = serialSearchResults.get("data")
			DiskDrive1Data = serialSearchResultsData['DiskDrives'][0]
			DiskDrive1Brand = DiskDrive1Data["Vendor"]
			DiskDrive1Serial = DiskDrive1Data["SerialNumber"]
			DiskDrive1SmartScore = DiskDrive1Data["SmartScore"]
			DiskDrive1OverallSmartState = DiskDrive1Data["OverallState"]
			productID = serialSearchResultsData["ProductID"]
			productDetailURL = "https://us-west.securaze.com/pc-product/details?productID=" + productID + "&type=PCProduct"
			wipeSucceeded = serialSearchDict['succeeded']
			lookupMessage = serialSearchDict['message']
			st.session_state['lookupMessage'] = lookupMessage
			st.session_state['serialSearchParams'] = serialSearchParams
			st.session_state['serialSearch'] = serialSearch
			st.session_state['serialSearchDict'] = serialSearchDict
			st.session_state['serialSearchResults'] = serialSearchResults
			st.session_state['serialSearchResultsData'] = serialSearchResultsData
			st.session_state['DiskDrive1Data'] = DiskDrive1Data
			st.session_state['DiskDrive1Brand'] = DiskDrive1Brand
			st.session_state['DiskDrive1Serial'] = DiskDrive1Serial
			st.session_state['DiskDrive1SmartScore'] = DiskDrive1SmartScore
			st.session_state['DiskDrive1OverallSmartState'] = DiskDrive1OverallSmartState
			st.session_state['productID'] = productID
			st.session_state['productDetailURL'] = productDetailURL
			st.session_state['wipeSucceeded'] = wipeSucceeded
			st.toast("Audit successful.")
		except:
			wipeText = "Not Found"
			st.toast("Audit failed.")
			try:
				if st.session_state['showWipeCard'] == True:	
					card(
						title="Wipe Failed, Incomplete, or Not Found ❌",
						text="Provided Serial: " + st.session_state['serialNumber'] + " | Click for more details",
						url="https://us-west.securaze.com/search?searchInput=" + st.session_state['serialNumber'],
						styles={
							"card": {
								"width": "100%",
								"height": "200px",
								"background-color": "red", 
								#"padding-bottom": "0px",
							}
						}
					)
				else:
					st.page_link(label="Wipe failed, incomplete, or not found. Click here for more details.", page="https://us-west.securaze.com/pc-product/details?productID=" + st.session_state['productID'] + "&type=PCProduct#2")
				if st.session_state['uiEffectsEnabled'] == True:
					rain(
						emoji="❌",
						font_size=30,
						falling_speed=8,
						animation_length=3
					)
				st.session_state['wipeSucceeded'] = False
			except:
				if st.session_state['verboseMode'] == True:
					st.toast("Wipe not found, unable to print Wipe Card")
				st.session_state['wipeSucceeded'] = False
try:
	if st.session_state['wipeSucceeded'] == True and serialNumber == st.session_state['serialNumber']:
		wipeText = "Success"
		apiPDFReportDownload = "https://api-us-west.securaze.com/api/products/download-erasure-report"
		apiPDFReportDownloadParams = {'CustomerID': st.session_state['customerID'], 'ProductID': st.session_state['productID'], 'Token': st.session_state['loginToken']}
		pdfRequest = req.post(apiPDFReportDownload, data=apiPDFReportDownloadParams)
		pdfFile = pdfRequest.content
		try:
			if st.session_state['showWipeCard'] == True:
				card(
					title="Wipe Successful ✅",
					text="Provided Serial: " + st.session_state['serialNumber'] + " | Click for more details",
					url="https://us-west.securaze.com/pc-product/details?productID=" + st.session_state['productID'] + "&type=PCProduct#2",
					styles={
						"card": {
							"width": "100%",
							"height": "200px",
							"background-color": "green",
							"margin-bottom": "0px",
						}
					}
				)
			else:
				st.page_link(label="Wipe successful. Click here for more details.", page="https://us-west.securaze.com/pc-product/details?productID=" + st.session_state['productID'] + "&type=PCProduct#2")
			if st.session_state['uiEffectsEnabled'] == True:
				rain(
					emoji="✅",
					font_size=30,
					falling_speed=8,
					animation_length=3
				)
		except:
			pass																							
except:
	pass
try:
	if st.session_state['verboseMode'] == True:
		st.toast("API Response: " + lookupMessage)
except:
	if st.session_state['verboseMode'] == True:
		st.toast("Showing cached data if available.")
with st.sidebar:
	if st.button("🔄 Force UI Update", use_container_width=True, help="Use after first login or to restore latest session."):
		pass
	st.container()
	if st.session_state['userLoginCompleted'] == True:
		if st.button("🔒 Log Out", help="Forget Login and Start Over", use_container_width=True):
			st.session_state['userLoginCompleted'] = False
			st.session_state['securazeUsername'] = ''
			st.session_state['securazePassword'] = ''
			st.session_state['loginYesorNoResponse'] = ''
			st.rerun()
try:
	if st.session_state['wipeSucceeded'] == True and serialNumber == st.session_state['serialNumber']:
		try: 
			reportLine0 = "Audit Report  \n"
			reportLine1 = "Device Serial: " + st.session_state['serialNumber'] + "  \n"
			reportLine2 = "Wipe Successful: Yes  \n"
			reportLine3 = "Audit Date: " + auditDate + "  \n"
			reportLine4 = "Drive Brand: " + st.session_state['DiskDrive1Brand'] + "  \n"
			reportLine5 = "Drive Serial: " + st.session_state['DiskDrive1Serial'] + "  \n"
			reportLine6 = "Drive Health Description: " + st.session_state['DiskDrive1OverallSmartState'] + "  \n"
			reportLine7 = "Drive Health Percentage: " + str(st.session_state['DiskDrive1SmartScore']) + "%  \n"
			reportLine8 = "Wipe Method: "
			auditReport = reportLine0 + reportLine1 + reportLine2 + reportLine3 + reportLine4 + reportLine5 + reportLine6 + reportLine7
			with st.container(border=15):
				
				st.download_button("↓  Download Work Report", type="primary", use_container_width=True, data=pdfFile, mime="application/pdf", file_name=st.session_state['serialNumber'] + "_Work_Report.pdf")
				st.download_button("↓  Download Audit Report", type="primary", use_container_width=True, data=auditReport, file_name=st.session_state['serialNumber'] + "_Audit_Report.txt")
				st.link_button(label="🔬 View on Dashboard", url=st.session_state['productDetailURL'], use_container_width=True)
				if st.button("📖 Show Audit Report", use_container_width=True):
					st.markdown(auditReport)
		except:
			pass
except:
	pass
