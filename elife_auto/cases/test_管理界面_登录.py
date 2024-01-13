import sys
sys.path.append('elife_auto')
import selenium.webdriver.common.by as By
from util.webUI_SMP import smpUI
#import util.webUI_SMP
import time
import pytest



def test_SMP_login_001():
    smpUI.login('byhy','sdfsdf')
    
    time.sleep(1)
    nav = smpUI.wd.find_element(By.By.TAG_NAME,'nav')
    assert nav != []
    
    
@pytest.fixture
def clearAlter():
    yield
    try:
        smpUI.wd.switch_to.alert.accept()    
    except Exception as e:
        print(e)

@pytest.mark.parametrize('username,password,expectedAlert',[
    (None,'sdfsdf','请输入用户名'),
    ('byhy',None,'请输入密码'),
    ('byhy','sdfsdff','登录失败： 用户名或者密码错误'),
    ('byhy','sdfsd','登录失败： 用户名或者密码错误'),
    ('byhyy','sdfsdf','登录失败： 用户名不存在'),
    ('byh','sdfsdf','登录失败： 用户名不存在'),
    ])
    
def test_SMP_login_002(username,password,expectedAlert,clearAlter):
    smpUI.login(username,password)
    time.sleep(1)
    alter = smpUI.wd.switch_to.alert
    assert alter.text == expectedAlert
    