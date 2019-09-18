# -*- coding: utf-8 -*-


class MockSignal(object):

    def __init__(self):
        self.history = []

    def send(self, **kwargs):
        self.history.append(kwargs)


signal_1 = MockSignal()


def clear():
    global signal_1
    signal_1 = MockSignal()
