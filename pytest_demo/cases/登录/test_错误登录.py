from pytest_demo.lib.login import loginAndCheck

class Test_FailLogin:
    # @pytest.mark.parametrize('username, password, expectedalert', [
    #     (None, '88888888', '请输入用户名'),
    #     ('byhy', None, '请输入密码'),
    #     ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
    #     ('byhy', '8888888', '登录失败 : 用户名或者密码错误'),
    #     ('byhy', '888888888', '登录失败 : 用户名或者密码错误'),
    # ]
    #                          )
    # def test_UI_0001_0005(self, username, password, expectedalert):
    #     alertText = loginAndCheck(username, password)
    #     assert alertText == expectedalert
        
    def test_UI_0001(self):
        print("\n用例 UI_0001")
        
        alertText = loginAndCheck(None,"88888888")
        
        assert alertText == "请输入用户名"
       
    
    def test_UI_0002(self):
        print("\n用例 UI_0002")
        
        alertText = loginAndCheck("byhy",None)
        
        assert alertText == "请输入密码"
        
    def test_UI_0003(self):
        print("\n用例 UI_0003")
        
        alertText = loginAndCheck("byh","88888888")
        
        assert alertText == "登录失败 : 用户名或者密码错误"
    
    def test_UI_0004(self):
        print("\n用例 UI_0004")
        
        alertText = loginAndCheck("byhy","8888888")
        
        assert alertText == "登录失败 : 用户名或者密码错误"
    
    def test_UI_0005(self):
        print("\n用例 UI_0005")
        
        alertText = loginAndCheck("byhy","888888888")
        
        assert alertText == "登录失败 : 用户名或者密码错误"
        
    