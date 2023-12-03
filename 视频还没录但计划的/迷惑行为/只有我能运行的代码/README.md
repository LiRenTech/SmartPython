1. 生成 rsa 私钥和公钥（私钥必须是 pksc1 格式，公钥必须是 pksc8 格式，不带密码）
2. 在 `real.py` 中编写要加密的代码
3. 运行 `main.py`，会在 `project/my_utils.bin` 生成加密代码
4. 在 `project/main.py` 中可以导入 `loader`，通过 `exec(loader.load_module())` 将加密代码导入到当前作用域
