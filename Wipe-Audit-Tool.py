import time
import streamlit as st
from streamlit_card import card
import streamlit_extras as st_extras
from streamlit_extras.let_it_rain import rain
import requests as req
st.set_page_config(page_title="Noah's Wipe Check", layout="centered")
apiLoginComplete = False
col1, col2 = st.columns([1, 1])
with col1:
	securazeUsername = st.text_input("Username")
if securazeUsername != "":
	with col2: 
		securazePassword = st.text_input("Password", type="password")
	if securazePassword != "" and securazeUsername != "":
		try:
			securazeLogin = {'Username': securazeUsername, 'Password': securazePassword, 'RememberMe': 'True'}
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
		except:
			loginToken = ""
			customerData = ""
			customerZeroData = ""
			customerName = ""
			customerID = ""
			st.toast("Exception handled. (Normal)")
		if loginYesorNoResponse == "User successfully logged in.": 
			global apiLoginSuccessful
			apiLoginSuccessful = True
			apiLoginComplete = True
			st.toast(customerName + ": " + loginYesorNoResponse)
			serialNumber = st.text_input("Enter the Serial Number then press Enter")
			if serialNumber != "":
				try: 
					serialSearchParams = {'CustomerID': customerID, 'SearchInput': serialNumber, 'Token': loginToken}
					serialSearch = req.post('https://api-us-west.securaze.com/api/products/search', data=serialSearchParams)
					serialSearchDict = serialSearch.json()
					serialSearchResults = serialSearchDict.get("result")
					serialSearchResultsData = serialSearchResults.get("data")
				except:
					st.toast("An unknown error has occured. Error Code: 02")
				try:
					productID = serialSearchResultsData['ProductID']
				except:
					productID = "None"
				# st.table(serialSearchDict)
				try:
					wipeSucceeded = serialSearchDict['succeeded']
					lookupMessage = serialSearchDict['message']
				except:
					st.toast("An unknown error has occured. Error Code: 03")
				## log here
				## may be best to write to the github folder
				def wipePass():
					try: 
						card(
        					title="Wipe Successful ✔️",
        					text="Device Serial: " + serialNumber + " | Click for more details",
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
							emoji="✔️",
							font_size=30,
							falling_speed=8,
							animation_length=1
						)
					except:
						pass
						st.toast("Exception handled. (Normal)")
				def wipeFail():
					try:
						card(
        					title="Wipe Failed ❌",
        					text="Device Serial: " + serialNumber + " | Click for more details",
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
							animation_length=1
						)
					except:
						pass
						st.toast("Exception handled. (No action is required - this is expected behavior)")

				if wipeSucceeded == True:
					wipePass()
				if wipeSucceeded == False:
					wipeFail()
				st.toast("API Response: " + lookupMessage)
		else:
			st.error("Please check your login details, press Enter, or refresh.")