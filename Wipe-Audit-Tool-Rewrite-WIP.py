# Requirements

import time
from datetime import date
import datetime
import streamlit as st
from streamlit_card import card
import streamlit_extras as st_extras
from streamlit_extras.let_it_rain import rain
import requests as req

# Set date string for audit report

now = datetime.datetime.now()
today = date.today()
auditDate = today.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

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
#apiAuthLink = "placeholder"
# Streamlit Page Setup

st.set_page_config(page_title="Securaze Wipe Check & Audit Log Alpha", layout="centered")
col1, col2 = st.columns([1, 1])

#define login function
# check to see if the session is logged in yet or not
try:
	if st.session_state['loginYesorNoResponse'] == "User successfully logged in.":
		st.session_state['userLoginCompleted'] = True
except:
	st.toast('Could not find a previous successful connection. Check your username and password.')

try:
	if st.session_state['userLoginCompleted'] == True:
		st.toast("Login for " + st.session_state['securazeUsername'] + " remembered.")
		st.info("Latest login response: " + st.session_state['loginYesorNoResponse'], icon=ℹ)
		#mainLoop()
	else:
		st.session_state['securazeUsername'] = st.text_input("Username")
		st.session_state['securazePassword'] = st.text_input("Password", type="password")
		if st.button("Login", use_container_width=True):
			with st.sidebar:
				try:
					loginQueryParams = {'Username': st.session_state['securazeUsername'], 'Password': st.session_state['securazePassword'], 'RememberMe': 'True' }
					securazeAPILogin = req.post(apiAuthLink, data=loginQueryParams)
					securazeAPILoginDict = securazeAPILogin.json()
					st.session_state['loginYesorNoResponse'] = securazeAPILoginDict.get('message')
					loginRequestRaw = securazeAPILoginDict.get('result')
					loginResponseData = loginRequestRaw.get("data")	
					try:
						loginToken = loginResponseData['Token']
						customerData = loginResponseData.get("Customers")
						st.session_state['customerZeroData'] = customerData[0]
						st.session_state['customerName'] = st.session_state['customerZeroData']['Name']
						st.session_state['customerID'] = st.session_state['customerZeroData']['CustomerID']
						st.session_state['tokenObtained'] = True
					except:
						loginToken = ""
						customerData = ""
						st.session_state['customerZeroData'] = ""
						st.session_state['customerName'] = ""
						st.session_state['customerID'] = ""
						st.session_state['tokenObtained'] = ""
						st.toast("An error occured, but the program will continue to run. Check your login details.")
				except:
					pass
except:
	pass

def login():
	try:
		loginQueryParams = {'Username': st.session_state['securazeUsername'], 'Password': st.session_state['securazePassword'], 'RememberMe': 'True' }
		securazeAPILogin = req.post(apiAuthLink, data=loginQueryParams)
		securazeAPILoginDict = securazeAPILogin.json()
		st.session_state['loginYesorNoResponse'] = securazeAPILoginDict.get('message')
		loginRequestRaw = securazeAPILoginDict.get('result')
		loginResponseData = loginRequestRaw.get("data")	
		st.write(loginQueryParams)
		st.header("api is being queried")
		try:
			loginToken = loginResponseData['Token']
			customerData = loginResponseData.get("Customers")
			st.session_state['customerZeroData'] = customerData[0]
			st.session_state['customerName'] = st.session_state['customerZeroData']['Name']
			st.session_state['customerID'] = st.session_state['customerZeroData']['CustomerID']
			st.session_state['tokenObtained'] = True
		except:
			loginToken = ""
			customerData = ""
			st.session_state['customerZeroData'] = ""
			st.session_state['customerName'] = ""
			st.session_state['customerID'] = ""
			st.session_state['tokenObtained'] = ""
			st.toast("An error occured, but the program will continue to run. Check your login details.")
	except:
		pass


with st.sidebar:
	if st.button("Reset Login", use_container_width=True):
		st.session_state['userLoginCompleted'] = False
		st.session_state['securazeUsername'] = ''
		st.session_state['securazePassword'] = ''
		st.session_state['loginYesorNoResponse'] = ''
	if st.button("Refresh", use_container_width=True):
		pass
	if st.button("Debug: Login Response", use_container_width=True):
		pass
	if st.button("Debug: Serial Search", use_container_width=True):
		pass
	if st.button("Simulate Successful Login", use_container_width=True):
		st.session_state['userLoginCompleted'] = True
	st.write("Loaded at " + time)

if st.session_state['userLoginCompleted'] == False:
	userLoginCompletedStr = "False"
else:
	userLoginCompletedStr = "True"
def mainLoop(): [

]
