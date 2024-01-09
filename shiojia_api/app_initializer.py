# app_initializer.py

def initialize_app():
    import shioaji as sj
    api = sj.Shioaji(simulation=True)
    # 登入API
    api.login(
        api_key="J8Y5k6yRHF5B524hEPVM1m6KfRHPwec772zu9FasKVbE",     # 請修改此處
        secret_key="5biJqZb8CKQufjA11kWKYGPr8R2c2wRXHdsdASYBfRLb"   # 請修改此處
    )
    return api

# 在模块级别初始化 app
api = initialize_app()