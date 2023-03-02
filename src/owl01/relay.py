from typing import List

from js import sendCmd, jsSleepWithCallbackEvery, getBufMsgList

class Relay(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


    def send_cmd(self, command: str) -> str:
        self.receive_msg()
        return sendCmd(command)

    def sleep(self, wait_time: int) -> None:
        jsSleepWithCallbackEvery(
            wait_time * 1000, 50,
            lambda: self.receive_msg()
        )

    def receive_msg(self) -> None:
        """
        The _receive_msg function is a private function that parses the data received from the drone.
        It splits it into individual messages and then checks if each message contains status information or not.
        If it does, then it updates the dictionary of states with this new information. If not, then we know that
        the message is a command response to one of our commands sent earlier.

        :param self: Access the attributes and methods of the class in python
        :doc-author: Jeremie
        """
        """
        解析返回数据
        :return: None
        """
        msgs: List[str] = getBufMsgList().split('\n')
        for msg in msgs:
            m: List[str] = msg.split(' ')
            # if len(m) >= 3:
            #     if m[1] == '0' and m[2] == 'status':
            #         states: str = m[3]
            #         st: Dict[str, Any] = reduce(
            #             self._split_state,
            #             states.split(';'),
            #             {}
            #         )
            #         if m[0] in self.uav_statement:
            #             self.uav_statement[m[0]].update(st)
            #         else:
            #             self.uav_statement[m[0]] = st
            #     elif m[1] != '0':
            #         # cmd table
            #         cId = int(m[1]) - 1
            #         if cId in self.cmd_table:
            #             tt = self.cmd_table[cId]
            #             self.cmd_table[cId] = (tt[0], msg)
            #         pass
            # pass