import sys
sys.path.append('elife_auto')
import selenium.webdriver.common.by as By
import selenium.webdriver.support.ui as UI
from util.webUI_SMP import smpUI
#import util.webUI_SMP
import time
import pytest
import util.cfg

@pytest.fixture(scope='module')
def inDeviceModelMgr():
    print('**  inDeviceModelMgr setup  **')
    smpUI.login('byhy','sdfsdf')
    time.sleep(1)
    smpUI.wd.get(util.cfg.SMP_URL_Device_Model)
    
    yield
    
    print('**  inDeviceModelMgr teardown  **')

@pytest.fixture()
def delAddedDeviceModel():
    print('**  删除添加的设备型号  setup  **')
    yield
    print('**  删除添加的设备型号  teardown  **')
    smpUI.del_first_item()

def test_SMP_device_model_001(inDeviceModelMgr,delAddedDeviceModel):
    #点击添加按钮
    time.sleep(3)
    topBtn = smpUI.wd.find_element(By.By.CSS_SELECTOR,'.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()
     
    smpUI.add_device_model('存储柜','elife-canbinlocker-g22-10-20-40','南京e生活存储柜-10大20中40小')

    dms = smpUI.get_first_page_device_model()
    assert dms == [['存储柜',
                    'elife-canbinlocker-g22-10-20-40',
                    '南京e生活存储柜-10大20中40小']]
    

def test_SMP_device_model_002(inDeviceModelMgr,delAddedDeviceModel):
    #点击添加按钮
    time.sleep(3)
    topBtn = smpUI.wd.find_element(By.By.CSS_SELECTOR,'.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()
    
    smpUI.add_device_model('存储柜','汉'*100,'南京e生活存储柜-10大20中40小')
    
    dms = smpUI.get_first_page_device_model()
    assert dms == [['存储柜',
                    '汉'*100,
                    '南京e生活存储柜-10大20中40小']]
    


