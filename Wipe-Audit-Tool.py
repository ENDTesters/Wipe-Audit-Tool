import time
from datetime import date
import streamlit as st
from streamlit_card import card
import streamlit_extras as st_extras
from streamlit_extras.let_it_rain import rain
import requests as req
st.set_page_config(page_title="Securaze Wipe Check & Audit Log Alpha", layout="centered")
apiLoginComplete = False
today = date.today()
dateString = today.strftime("%Y-%m-%d")
auditDate = today
col1, col2 = st.columns([1, 1])
tokenObtained = False
securazeUsername = ""
securazePassword = ""
global wipeSucceeded
wipeSucceeded = False
st.session_state.securazeUsername = True
st.session_state.securazePassword = True
st.session_state.tokenObtained = True
st.header("Securaze Wipe Check & Audit Log Alpha")
with col1:
	securazeUsername = st.text_input("Username")
if securazeUsername != "":
	with col2: 
		securazePassword = st.text_input("Password", type="password")
	if securazePassword != "" and securazeUsername != "":
		try:
			securazeLogin = {'Username': securazeUsername, 'Password': securazePassword, 'RememberMe': 'False'}
			apiAuthLink = "https://api-us-west.securaze.com/api/auth/login"
			securazeAPILogin = req.post(apiAuthLink, data=securazeLogin) 
			securazeAPILoginDict = securazeAPILogin.json() # required for API Response text
			loginYesorNoResponse = securazeAPILoginDict.get('message')
			loginRequestRaw = securazeAPILoginDict.get('result')
			loginResponseData = loginRequestRaw.get("data")
		except:
			st.toast("An unknown error has occured. Error Code: 01")
		try:
			loginToken = loginResponseData['Token']
			customerData = loginResponseData.get("Customers")
			customerZeroData = customerData[0]
			customerName = customerZeroData['Name']
			customerID = customerZeroData['CustomerID']
			tokenObtained = True
		except:
			loginToken = ""
			customerData = ""
			customerZeroData = ""
			customerName = ""
			customerID = ""
			tokenObtained = False
			st.toast("Exception handled. (No action is required)")
		if loginYesorNoResponse == "User successfully logged in.": 
			global apiLoginSuccessful
			apiLoginSuccessful = True
			apiLoginComplete = True
			st.toast(customerName + ": " + loginYesorNoResponse)
		else:
			st.error("Please check your login details, press Enter, or refresh.")
if tokenObtained == True and apiLoginComplete == True: 	
	serialNumber = st.text_input("Enter the Serial Number then press Enter")
	try: 
		serialSearchParams = {'CustomerID': customerID, 'SearchInput': serialNumber, 'Token': loginToken}
		serialSearch = req.post('https://api-us-west.securaze.com/api/products/search', data=serialSearchParams)
		serialSearchDict = serialSearch.json()
		serialSearchResults = serialSearchDict.get("result")
		serialSearchResultsData = serialSearchResults.get("data")
	except:
		st.toast("Not searching yet...")
	try:
		productID = serialSearchResultsData['ProductID']
	except:
		productID = "None"
	try:
		wipeSucceeded = serialSearchDict['succeeded']
		lookupMessage = serialSearchDict['message']
	except:
		st.toast("Not searching yet...")
	## log here
	## may be best to write to the github folder
	def wipePass():
		try: 
			card(
				title="Wipe Successful ✅",
				text="Provided Serial: " + serialNumber + " | Click for more details",
				image="https://www.fredsmithxmastrees.com/wp-content/uploads/2017/04/Square-500x500-green-264x264.png",
				url="https://us-west.securaze.com/pc-product/details?productID=" + productID + "&type=PCProduct#2",
				styles={
					"card": {
						"width": "100%",
						"height": "300px" 
					}
				}
			)
			rain(
				emoji="✅",
				font_size=30,
				falling_speed=8,
				animation_length=3
			)
		except:
			pass
			st.toast("Exception handled. (No action is required)")
	def wipeFail():
		try:
			card(
				title="Wipe Failed / Not Found ❌",
				text="Provided Serial: " + serialNumber + " | Click for more details",
				image="https://th.bing.com/th/id/OIP.0MzNC_IRoz_RF3SqpG3yVAHaGn?rs=1&pid=ImgDetMain",
				url="https://us-west.securaze.com/search?searchInput=" + serialNumber,
				styles={
					"card": {
						"width": "100%",
						"height": "300px" 
					}
				}
			)
			rain(
				emoji="❌",
				font_size=30,
				falling_speed=8,
				animation_length=3
			)
		except:
			pass
			st.toast("Exception handled. (No action is required)")
	if wipeSucceeded == True:
		wipeText = "Success"
		wipePass()
		apiPDFReportDownload = "https://api-us-west.securaze.com/api/products/download-erasure-report"
		apiPDFReportDownloadParams = {'CustomerID': customerID, 'ProductID': productID, 'Token': loginToken}
		pdfRequest = req.post(apiPDFReportDownload, data=apiPDFReportDownloadParams)
		pdfFile = pdfRequest.content
		st.download_button("Download Wipe Report", use_container_width=True, data=pdfFile, mime="application/pdf", file_name=serialNumber + "_Wipe_Report.pdf")
	else:
		wipeText = "Not Found"
		wipeFail()
		try:
			st.toast("API Response: " + lookupMessage)
		except:
			pass
	try:
		st.header("Wipe Check & Audit Log: Current Limitations")
		st.write("This program could do the same things with fewer API requests.")
		st.write("As such, it probably shouldn't be considered production-ready.")
		st.write("I have done a partial rewrite, but I think there are still issues with variable scope.")
		st.write("Audit logs can be manually created and saved by copy and pasting.")
		st.write("Audit logs only consider one drive. ")
		st.write("Additional drives must be reviewed on Securaze's dashboard.")
		st.write("Source available at https://github.com/ENDTesters/Wipe-Audit-Tool")
		auditLogFileName = serialNumber + " Wipe Audit Log.txt"
		auditLogLine1 = "System Serial Number: " + serialNumber
		auditLogLine2 = "Wipe Status: " + wipeText
		auditLogLine3 = "Audit Date: " + dateString 
		with st.expander(auditLogFileName):
			st.write(auditLogLine1)
			st.write(auditLogLine2)
			st.write(auditLogLine3)
	except:
		st.toast("Exception handled. (No action is required)")




