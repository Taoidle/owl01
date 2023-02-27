from functools import reduce
from typing import List, Dict, Any, Optional

from .control_command import AirplaneController, AirplaneControllerExtended
from ..js import sendCmd, jsSleepWithCallbackEvery, getBufMsgList


class AirplaneManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    airplanes_table: Dict[str, AirplaneControllerExtended] = {}

    def ping(self):
        return None

    def start(self):
        return None

    def get_airplane(self, id: str) -> Optional[AirplaneController]:
        """
        获取指定无人机
        :param id: 无人机的 keyName
        :return: AirplaneController
        """
        return self.airplanes_table.get(id)
        pass

    def get_airplane_extended(self, id: str) -> Optional[AirplaneControllerExtended]:
        """
        获取扩展飞机对象
        这个函数获取的API在完全适配PhantasyIslandPythonRemoteControl的API基础上，添加了FH0A无人机特有功能API
        :param keyName: 无人机的 keyName
        :return: AirplaneController
        """
        return self.airplanes_table.get(id)
        pass

    def sleep(self, wait_time: int) -> None:
        jsSleepWithCallbackEvery(
            wait_time * 1000, 50,
            lambda: self.__receive_msg()
        )

    def __send_cmd(self, command: str) -> str:
        self.__receive_msg()
        return sendCmd(command)

    def __receive_msg(self) -> None:
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
            if len(m) >= 3:
                if m[1] == '0' and m[2] == 'status':
                    states: str = m[3]
                    st: Dict[str, Any] = reduce(
                        self._split_state,
                        states.split(';'),
                        {}
                    )
                    if m[0] in self.uav_statement:
                        self.uav_statement[m[0]].update(st)
                    else:
                        self.uav_statement[m[0]] = st
                elif m[1] != '0':
                    # cmd table
                    cId = int(m[1]) - 1
                    if cId in self.cmd_table:
                        tt = self.cmd_table[cId]
                        self.cmd_table[cId] = (tt[0], msg)
                    pass
            pass

    def flush(self):
        """
        更新当前管理器所管理的所有飞机的状态
        """
        airplane_status: Dict[str, Dict[str, any]] = process_airplane(get_all_airplane_status())
        if airplane_status is not None:
            # print('airplane_status', airplane_status)
            for k, status in airplane_status.items():
                # print('k', k)
                if self.airplanes_table.get(k) is None:
                    self.airplanes_table[k] = AirplaneControllerExtended(
                        keyName=status['keyName'],
                        typeName=status['typeName'],
                        updateTimestamp=status['updateTimestamp'],
                        status=status['status'],
                    )
                else:
                    a: AirplaneController = self.airplanes_table.get(k)
                    a.keyName = status['keyName']
                    a.typeName = status['typeName']
                    a.updateTimestamp = status['updateTimestamp']
                    a.status = make_AirplaneFlyStatus(status['status'])
                    a.cameraFront = status['cameraFront']
                    a.cameraDown = status['cameraDown']
                pass
            pass
        else:
            return None


def get_airplane_manager():
    """
    AirplaneManager是以单例模式工作的，故而需要使用这个函数来获取AirplaneManager单例对象
    :return: AirplaneManager单例对象
    """
    return AirplaneManager()
