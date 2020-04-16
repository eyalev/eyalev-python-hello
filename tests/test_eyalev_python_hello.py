
from eyalev_python_hello import __version__
from eyalev_python_hello import main


def test_version():
    assert __version__ == '0.1.0'


def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"
