from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_home():
	resp = app.request("/")
	assert_response(resp, contains="Rajesh Family Trust")

def test_family_members():
	resp = app.request("/")
	assert_response(resp, contains="Rajesh Family Trust")
	resp = app.request("/family_members")
	assert_response(resp, contains="Family Members")

def test_family_member():
	resp = app.request("/")
	assert_response(resp, contains="Rajesh Family Trust")
	resp = app.request("/family_members")
	assert_response(resp, contains="Family Members")
	resp = app.request("/family_member", method="POST")
	assert_response(resp, contains="Family Member")
	