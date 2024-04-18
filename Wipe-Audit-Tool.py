import time
import streamlit as st
from streamlit_card import card
import streamlit_extras as st_extras
from streamlit_extras.let_it_rain import rain
import requests as req
st.set_page_config(page_title="Noah's Audit Tool Test Build", layout="centered")
apiLoginComplete = False
col1, col2 = st.columns([1, 1])
with col1:
	securazeUsername = st.text_input("Username")
if securazeUsername != "":
	with col2: 
		securazePassword = st.text_input("Password", type="password")
	if securazePassword != "" and securazeUsername != "":
		securazeLogin = {'Username': securazeUsername, 'Password': securazePassword, 'RememberMe': 'True'}
		apiAuthLink = "https://api-us-west.securaze.com/api/auth/login"
		securazeAPILogin = req.post(apiAuthLink, data=securazeLogin) 
		securazeAPILoginDict = securazeAPILogin.json() # required for API Response text
		loginYesorNoResponse = securazeAPILoginDict.get('message')
		loginRequestRaw = securazeAPILoginDict.get('result')
		loginResponseData = loginRequestRaw.get("data")
		loginToken = loginResponseData['Token']
		customerData = loginResponseData.get("Customers")
		customerZeroData = customerData[0]
		customerName = customerZeroData['Name']
		customerID = customerZeroData['CustomerID']
		if loginYesorNoResponse == "User successfully logged in.": 
			global apiLoginSuccessful
			apiLoginSuccessful = True
			apiLoginComplete = True
			st.toast(customerName + ": " + loginYesorNoResponse)
			serialNumber = st.text_input("Enter the device serial then press Enter")
			if serialNumber != "":
				serialSearchParams = {'CustomerID': customerID, 'SearchInput': serialNumber, 'Token': loginToken}
				serialSearch = req.post('https://api-us-west.securaze.com/api/products/search', data=serialSearchParams)
				serialSearchDict = serialSearch.json()
				serialSearchResults = serialSearchDict.get("result")
				serialSearchResultsData = serialSearchResults.get("data")
				try:
					productID = serialSearchResultsData['ProductID']
				except:
					productID = "None"
				# st.table(serialSearchDict)
				wipeSucceeded = serialSearchDict['succeeded']
				lookupMessage = serialSearchDict['message']
				## log here
				## may be best to write to the github folder
				def wipePass():
					card(
        				title="Wipe Successful ✔️",
        				text="Device Serial: " + serialNumber,
        				image="https://www.fredsmithxmastrees.com/wp-content/uploads/2017/04/Square-500x500-green-264x264.png",
        				url="https://us-west.securaze.com/pc-product/details?productID=" + productID + "&type=PCProduct#2",
    				)
					rain(
						emoji="✔️",
						font_size=30,
						falling_speed=8,
						animation_length=1
					)
				def wipeFail():
					card(
        				title="Wipe Failed or Exceptioned ❌",
        				text="Device Serial: " + serialNumber,
        				image="https://th.bing.com/th/id/OIP.0MzNC_IRoz_RF3SqpG3yVAHaGn?rs=1&pid=ImgDetMain",
        				url="https://us-west.securaze.com/search?searchInput=" + serialNumber,
    				)
					rain(
						emoji="❌",
						font_size=30,
						falling_speed=8,
						animation_length=1
					)

				if wipeSucceeded == True:
					wipePass()
				if wipeSucceeded == False:
					wipeFail()
				st.toast("API Response: " + lookupMessage)
		else:
			st.toast("Please click the login button to renew your session.")