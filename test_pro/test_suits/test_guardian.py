import requests
import pytest
import json
import yaml
import jwt

from time import time
from input_base.input_guardian import *
from output_base.output_guardian import *
from jwt_base import get_token_payload

class GuardianSessionBase(object):
    ''' guardian login can throught 4 ways:
            - name, password
            - mobile, smsCode
            - mobile, password
            - wechatId

        5 kinds smscode without status of login
            - sign up
            - sign in
            - mobile binding
            - forget password
            - wechat binding
    '''
    @pytest.fixture(scope='class')
    def guardian_login_with_name_valid(self):
        # login with name vliad fixtured method
        r = requests.post(GUARDIAN_SESSIONS_URL,
                json=GUARDIAN_SESSIONS_NAME_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('name') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_name = content_dict.get('name')
        return login_token, guardian_type, guardian_id, guardian_name

    @pytest.fixture(scope='class')                                        
    def guardian_login_with_mobile_pswd_valid(self):                                 
        # login with mobile-password vliad fixtured method                           
        r = requests.post(GUARDIAN_SESSIONS_URL,
                json=GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_mobile = content_dict.get('mobile')
        return login_token, guardian_type, guardian_id, guardian_mobile

    @pytest.fixture(scope='class')
    def guardian_login_with_mobile_smscode_valid(self, guardian_sms_signin):
        # login with mobile-smscode vliad fixtured method                           
        r = requests.post(GUARDIAN_SESSIONS_URL,
                json=GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_mobile = content_dict.get('mobile')
        return login_token, guardian_type, guardian_id, guardian_mobile

    @pytest.fixture(scope='class')
    def guardian_login_with_wechatid_valid(self):
        # login with wechatid vliad fixtured method                           
        r = requests.post(GUARDIAN_SESSIONS_URL,
                json=GUARDIAN_SESSIONS_WECHATID_VALID_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('token') == True
        assert content_dict.has_key('type') == True
        assert content_dict.has_key('id') == True
        assert content_dict.has_key('mobile') == True
        login_token = content_dict.get('token')
        guardian_type = content_dict.get('type')
        guardian_id = content_dict.get('id')
        guardian_mobile = content_dict.get('mobile')
        return login_token, guardian_type, guardian_id, guardian_mobile

    @pytest.fixture(scope='class')
    def guardian_sms_signin(self):
        # guardian send smscode request for login with mobile and smscode
        r = requests.post(GUARDIAN_SMS_URL,
                json=GUARDIAN_SMS_SIGNIN_DATA)
        assert r.status_code == 201
        content_dict = json.loads(r.content)
        assert content_dict.has_key('id') == True
        _id = content_dict.get('id')
        return _id


    # TODO 
    # guardian login test with invalid input data

    '''
    def test_guardian_login_with_name_invalid_schema_01(self):








    '''
class TestGuardianSession(GuardianSessionBase):
    def test_login_with_name(self, guardian_login_with_name_valid):
        login_token, guardian_type, guardian_id, guardian_name = guardian_login_with_name_valid
        assert guardian_name == OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA.get('name') 
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA.get('type') 
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_NAME_VALID_DATA.get('id') 
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
        
    def test_login_with_mobile_pswd(self, guardian_login_with_mobile_pswd_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get('mobile') 
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get('type') 
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_MOBILE_PSWD_VALID_DATA.get('id') 
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()

    def test_login_with_mobile_smscode(self,
            guardian_login_with_mobile_smscode_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA.get('mobile') 
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA.get('type') 
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_MOBILE_SMSCODE_VALID_DATA.get('id') 
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
    """
    def test_login_with_wechatid(self,
            guardian_login_with_wechatid_valid):
        login_token, guardian_type, guardian_id, guardian_mobile = guardian_login_with_mobile_pswd_valid
        assert guardian_mobile == OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA.get('mobile') 
        assert guardian_type == OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA.get('type') 
        assert guardian_id == OUTPUT_GUARDIAN_SESSIONS_WECHATID_VALID_DATA.get('id') 
        payload = get_token_payload(login_token)
        assert payload.get('exp') > time()
    """