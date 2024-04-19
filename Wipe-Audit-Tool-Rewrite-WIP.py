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
if 'securazeUsername' and 'securazePassword' and 'loginToken' not in st.session_state:
	st.session_state['userLoginCompleted'] = False
else:
	if '' == 'securazeUsername' or 'securazePassword' or 'loginToken' in st.session_state:
		st.session_state['userLoginCompleted'] = False
	else:
		st.session_state['userLoginCompleted'] = True

# Set API variables

#apiAuthLink = "https://api-us-west.securaze.com/api/auth/login"
apiAuthLink = "placeholder"
# Streamlit Page Setup

st.set_page_config(page_title="Securaze Wipe Check & Audit Log Alpha", layout="centered")
col1, col2 = st.columns([1, 1])

#define login function

def login():
	try:
		loginQueryParams = {'Username': st.session_state['securazeUsername'], 'Password': st.session_state['securazePassword'], 'RememberMe': 'True' }
		securazeAPILogin = req.post(apiAuthLink, data=loginQueryParams)

		st.write(loginQueryParams)

	except:
		pass

# check to see if the session is logged in yet or not

try:
	if st.session_state['userLoginCompleted'] == True:
		pass
		st.success("Login Established!")
		#mainLoop()
	while st.session_state['userLoginCompleted'] == False:
		st.toast("Waiting for Authentication")
		with st.sidebar:
			st.session_state['securazeUsername'] = st.text_input("Username")
		with st.sidebar: 
			st.session_state['securazePassword'] = st.text_input("Password", type="password")
		with st.sibebar:	
			if st.button("Login", use_container_width=True):
				login()
except:
	st.toast("An issue may have occured during the login process.")

with st.sidebar:

	if st.button("Reset Authentication", use_container_width=True):
		st.session_state['userLoginCompleted'] = False
		st.session_state['securazeUsername'] = ''
		st.session_state['securazePassword'] = ''
		st.session_state['loginToken'] = ''
	if st.button("Debug: Login Response", use_container_width=True):
		st.write("")
	if st.button("Debug: Serial search", use_container_width=True):
		st.write("")
	if st.button("Simulate Successful Login", use_container_width=True):
		st.session_state['userLoginCompleted'] = True
	st.write("Loaded at " + time)


st.write(st.session_state['securazeUsername'])
st.write(st.session_state['securazePassword'])
st.write(st.session_state['userLoginCompleted'])
def mainLoop(): [

]

