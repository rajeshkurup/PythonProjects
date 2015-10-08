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
	resp = app.request("/family_member")
	assert_response(resp, contains="Family Member")
	
def test_family_member_edit():
	resp = app.request("/")
	assert_response(resp, contains="Rajesh Family Trust")
	resp = app.request("/family_members")
	assert_response(resp, contains="Family Members")
	resp = app.request("/family_member")
	assert_response(resp, contains="Family Member")
	resp = app.request("/family_member_edit")
	assert_response(resp, contains="Edit Family Member")

def test_family_member_submit():
	resp = app.request("/")
	assert_response(resp, contains="Rajesh Family Trust")
	resp = app.request("/family_members")
	assert_response(resp, contains="Family Members")
	resp = app.request("/family_member")
	assert_response(resp, contains="Family Member")
	resp = app.request("/family_member_edit")
	assert_response(resp, contains="Edit Family Member")
	resp = app.request("/family_member_submit", method="POST")
	assert_response(resp, status="303")
