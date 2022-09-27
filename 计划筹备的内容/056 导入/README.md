# 导入问题

---

## 不同位置的导入问题

### 同级导入

直接import即可

### 引入更下面的内容

imoprt 文件夹.模块名 即可

### 引入上面的内容

这个比较麻烦

```python
import sys

sys.path.insert(0, "../")
import phe

def main():
    print(phe.f())
    return None
```

这个情况是，目前写的这个文件在一个文件夹里。但是phe文件在父层文件夹里

缺点：pycharm不认，虽然运行不会报错，但是会有红色波浪线，很烦



## 模块代码自动执行问题

会自动执行的情况

```python
import xxx
```

只会执行一次