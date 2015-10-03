from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	# check that we get a 200 on the / URL
	resp = app.request("/")
	assert_response(resp, status="200")
	
	# test our first get request to /hello
	resp = app.request("/hello_form_layout")
	assert_response(resp)
	
	# make sure that default values work for the form
	resp = app.request("/hello_form_layout", method="POST")
	assert_response(resp, contains="Nobody")

	# test that we get expected values
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello_form_layout", method="POST", data=data)
	assert_response(resp, contains="Zed")
	