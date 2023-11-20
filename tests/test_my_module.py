import os
import sys
from datetime import datetime
from unittest.mock import Mock, patch

import pytest

script_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    # script_dir が指すディレクトリ内の全てのファイル名やディレクトリ名を含んだリスト内に "src" という名前があるのか確認
    if "src" in os.listdir(script_dir):
        break

    # script_dir の指すディレクトリを含むディレクトリ、つまり、1つ上のディレクトリを再代入
    script_dir = os.path.dirname(script_dir)

    # ルートディレクトリに到達した場合、srcディレクトリが見つからなかったとしてエラーを表示
    if script_dir == "/":
        raise FileNotFoundError("src directory not found")

# srcディレクトリの絶対パスを生成
src_dir = os.path.join(script_dir, "src")

# srcディレクトリをsys.pathに追加
sys.path.insert(0, src_dir)

for i in sys.path:
    print(i)

from python_de_manabu_parsing.my_module import add, divide, return_now_datetime


# @pytest.yield_fixture()
@pytest.fixture()
def before_and_after_and_return_1():
    print("BEFORE")
    yield 1
    print("AFTER")


def test_add(before_and_after_and_return_1):
    # import pdb;pdb.set_trace()
    assert add(before_and_after_and_return_1, 2) == 3


@pytest.mark.parametrize(
    ("x", "y", "expected"), [(10, 5, 2), (100, 10, 10), (50, 2, 25), (9, 3, 3)]
)
def test_divide(x, y, expected):
    assert divide(x, y) == expected


def test_divide_raise_error():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.skip()
def test_return_now_datetime_cannot_patch_immutable_attribute(monkeypatch):
    # TypeError: cannot set 'now' attribute of immutable type 'datetime.datetime'
    monkeypatch.setattr(datetime, "now", datetime.fromisoformat("2023-01-01T00:00:00"))
    assert return_now_datetime() == datetime(2023, 1, 1, 0, 0, 0)


def test_return_now_datetime_monkeypatch(monkeypatch):
    mock_datetime = Mock(wraps=datetime)
    mock_datetime.now.return_value = datetime.fromisoformat("2023-01-01T00:00:00")
    monkeypatch.setattr("python_de_manabu_parsing.my_module.datetime", mock_datetime)
    assert return_now_datetime() == datetime(2023, 1, 1, 0, 0, 0)


@patch("python_de_manabu_parsing.my_module.datetime")
def test_return_now_datetime_patch(mock_datetime):
    mock_datetime.now.return_value = datetime.fromisoformat("2023-01-01T00:00:00")
    assert return_now_datetime() == datetime(2023, 1, 1, 0, 0, 0)
    # with patch("python_de_manabu_parsing.my_module.datetime",
    # new_callable=MyCustomMock) as m_datetime:
    #     m_datetime.now.return_value = datetime.fromisoformat("2023-01-01T00:00:00")
    #     assert return_now_datetime() == datetime(2023, 1, 1, 0, 0, 0)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        # script_dir が指すディレクトリ内の全てのファイル名やディレクトリ名を含んだリスト内に "src" という名前があるのか確認
        if "src" in os.listdir(script_dir):
            break

        # script_dir の指すディレクトリを含むディレクトリ、つまり、1つ上のディレクトリを再代入
        script_dir = os.path.dirname(script_dir)

        # ルートディレクトリに到達した場合、srcディレクトリが見つからなかったとしてエラーを表示
        if script_dir == "/":
            raise FileNotFoundError("src directory not found")

    # srcディレクトリの絶対パスを生成
    src_dir = os.path.join(script_dir, "src")

    # srcディレクトリをsys.pathに追加
    sys.path.insert(0, src_dir)
