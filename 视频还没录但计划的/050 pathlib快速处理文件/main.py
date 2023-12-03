from pathlib import Path

# 1. 获取文件所在目录，不是工作目录
root = Path(__file__).parent
# 2. 遍历所有子文件（夹）
for dir in root.iterdir():
    print(dir.as_posix())
# 3. glob pattern
for file in root.glob("./**/*.shit"):
    print(file.as_posix())
# 4. 读写文件
(root / "a" / "a.shit").write_text("shit")
(root / "a" / "test1" / "b.shit").write_text(
    (root / "a" / "a.shit").read_text() + "bbb"
)
# 5. 链接 (what == a/a.shit)
"""
error: short read while indexing 视频还没录但计划的/050 pathlib快速处理文件/what
error: 视频还没录但计划的/050 pathlib快速处理文件/what: failed to insert into database
error: unable to index file '视频还没录但计划的/050 pathlib快速处理文件/what'
"""
(root / "what.ignore").hardlink_to(root / "a" / "a.shit")
