import re
import traceback
import rich
from pygments import highlight
from pygments.lexers import Python3Lexer
from pygments.formatters import TerminalFormatter

def f():
    raise Exception("111112222报错辣")

def main():
    f()

try:
    main()
except Exception as e:
    exc = traceback.format_exc().strip()  # 获取traceback
    err, msg = exc.splitlines()[-1].split(": ") if len(exc.splitlines()[-1].split(": ")) == 2 else (exc.splitlines()[-1], "")  # 获取err,msg
    tb = re.findall(r" +File [\"'](.+)[\"'], line (\d+), in (.+)\n +(.+)", exc, re.M)
    # 获取到信息之后就可以开始打印了
    rich.print("[red]Traceback[/red] [blue](most recent call last):[/blue]")
    for i in tb:
        rich.print(f"  [green]{i[0].split('/')[-1]}[/green] >> {i[2]}")
        rich.print(f"    {i[1]:0>3} | ", end="")
        print(highlight(i[3], Python3Lexer(), TerminalFormatter()), end="")
    rich.print(f"[blue]{err}[/blue] {msg}")
