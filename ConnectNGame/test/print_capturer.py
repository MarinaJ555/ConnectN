import io
from typing import List


class PrintCapturer(object):
    """
    Use with patch to capture the output of the print function.
    Each call to print will be stored as one element of output.

    If you would prefer a single string use the as_string method
    which will return everything that would have been printed as
    a single string.
    """

    def __init__(self) -> None:
        self.output: List[str] = []

    def as_string(self):
        """
        Returns everything that would have been printed
        as one single string
        :return:
        """
        return ''.join(self.output)

    def __call__(self, *args, **kwargs):
        line = io.StringIO(newline=None)
        print(*args, **kwargs, file=line)
        self.output.append(line.getvalue())
        line.close()
