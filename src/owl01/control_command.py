from .airplane_core import AirplaneCore
from enum import IntEnum

from .relay import Relay


class AirplaneModeEnum(IntEnum):
    """
    无人机airplane_mode函数设置飞行模式指令
    """
    CommonMode = 1
    MapMode = 2


class AirplaneController(AirplaneCore):
    """
    无人机控制
    此类包含控制单个无人机的所有指令
    """
    count: int = 1

    __relay = None

    def use_fast_mode(self, enable=True):
        pass

    def __init__(self, id: str, relay: Relay):
        # super(AirplaneCore, self).__init__()
        # super(Relay, self).__init__()
        self.keyName = id
        self.__relay = relay

    def _next_count(self):
        self.count = self.count + 2
        return self.count

    def _prepare_command(self, command: str) -> str:
        return self.keyName + ' ' + str(self._next_count()) + ' ' + command

    def _send_cmd(self, command: str) -> str:
        self.count = self.count + 1
        return self.__relay.send_cmd(self._prepare_command(command))

    def ping(self):
        return None

    def start(self):
        return None

    def mode(self, mode: AirplaneModeEnum):
        """
        控制无人机飞行模式
        :param mode: 1,2,3,4
        :return:
        """
        self.airplane_mode(mode)
        pass

    def takeoff(self, high: int):
        """
        控制无人机起飞
        :param high: 起飞到指定高度
        :return:
        """
        return self._send_cmd(f"takeoff {high}")

    def land(self):
        """
        控制无人机降落
        """
        return self._send_cmd(f"land")

    def emergency(self):
        """停桨"""
        return self._send_cmd(f"emergency")

    def up(self, distance: int):
        """
        向上移动
        :param distance:移动距离（厘米）
        """
        return self._send_cmd(f"up {distance}")

    def down(self, distance: int):
        """
        向下移动
        :param distance:移动距离（厘米）
        """
        return self._send_cmd(f"down {distance}")

    def forward(self, distance: int):
        """
        The forward function moves the drone forward by a specified distance (meters).

        向前移动
        :param distance:移动距离（厘米）

        :param self: Access variables that belongs to the class
        :param distance:int: Specify the distance to move
        :return: The string &quot;ok&quot; if the command was successful
        :doc-author: Jeremie
        """
        return self._send_cmd(f"forward {distance}")

    def back(self, distance: int):
        """
        向后移动
        :param distance:移动距离（厘米）
        """
        return self._send_cmd(f"back {distance}")

    def left(self, distance: int):
        """
        向左移动
        :param distance:移动距离（厘米）
        """
        return self._send_cmd(f"left {distance}")

    def right(self, distance: int):
        """
        向右移动
        :param distance:移动距离（厘米）
        """
        return self._send_cmd(f"right {distance}")

    def goto(self, x: int, y: int, h: int):
        """
        控制无人机到达指定位置
        :param x: x轴方向位置（厘米）
        :param y: y轴方向位置（厘米）
        :param h: 高度（厘米）
        """
        return self._send_cmd(f"goto {x} {y} {h}")

    def flip(self, direction: str):
        """
        flip函数用于控制无人机翻滚
        :param direction: 翻滚方向（f前 b后 l左 r右）
        """
        return self._send_cmd(f"flip {direction} 1")

    def flip_forward(self):
        """向前做翻转（翻跟头）动作
        """
        self.flip("f")
        pass

    def flip_back(self):
        """向后做翻转（翻跟头）动作
        """
        self.flip("b")
        pass

    def flip_left(self):
        """向左做翻转（翻跟头）动作
        """
        self.flip("l")
        pass

    def flip_right(self):
        """向右做翻转（翻跟头）动作
        """
        self.flip("r")
        pass

    def rotate(self, degree: int):
        """
        控制无人机旋转
        :param degree: 自转方向和角度（正数顺时针，负数逆时针，单位为度数）
        """
        return self._send_cmd(f"rotate {degree}")

    def cw(self, degree: int):
        """
        控制无人机顺时针自转
        :param degree: 自转角度度数
        """
        return self._send_cmd(f"cw {degree}")

    def ccw(self, degree: int):
        """
        控制无人机逆时针自转
        :param degree: 自转角度度数
        """
        return self._send_cmd(f"ccw {degree}")

    def high(self, high: int):
        """
        控制无人机飞行高度
        :param high: 飞行到指定高度
        :return:
        """
        return self._send_cmd(f"high {high}")

    def speed(self, speed: int):
        """
        设置无人机飞行速度
        :param speed: 飞行速度（0-200厘米/秒）
        """
        return self._send_cmd(f"setSpeed {speed}")

    def led(self, r: int, g: int, b: int):
        """
        控制无人机灯光为指定颜色
        :param r: 灯光颜色R通道
        :param g: 灯光颜色G通道
        :param b: 灯光颜色B通道
        """
        return self._send_cmd(f"light {r} {g} {b}")

    def bln(self, r: int, g: int, b: int):
        """
        控制无人机灯光，呼吸灯
        :param r: 灯光颜色R通道
        :param g: 灯光颜色G通道
        :param b: 灯光颜色B通道
        """
        return self._send_cmd(f"bln {r} {g} {b}")

    def rainbow(self, r: int, g: int, b: int):
        """
        控制无人机灯光，七彩变换
        :param r: 灯光颜色R通道
        :param g: 灯光颜色G通道
        :param b: 灯光颜色B通道
        """
        return self._send_cmd(f"rainbow {r} {g} {b}")

    def airplane_mode(self, mode: AirplaneModeEnum):
        """
        设置无人机飞行模式
        :param mode: AirplaneModeEnum 1,2,3,4
        :return:
        """
        return self._send_cmd(f"airplane_mode {mode.value}")

    def stop(self):
        """
        控制无人机悬停
        """
        return self.hover()

    def hover(self):
        """
        控制无人机悬停
        """
        return self._send_cmd(f"hover")

    def take_photo(self, c: int):
        if c == 1:
            return self._send_cmd(f"capture_image front")
        elif c == 2:
            return self._send_cmd(f"capture_image down")
        else:
            pass
    pass

    def shutdown(self):
        pass

# class AirplaneControllerExtended(AirplaneController):
#     """
#     无人机扩展控制类
#     此类为预留给各个实机接口库的适配类，
#     所有为特定实机而实现的接口库都应该将其所特有的功能实现在此扩展类中
#     """
#
#     def __getattr__(self, item):
#         """
#         此函数为方法拦截器，
#         用来拦截对此对象的不存在的函数的获取和调用，
#         为了对其他库实现的适配而存在
#         from https://stackoverflow.com/questions/14612442/how-to-handle-return-both-properties-and-functions-missing-in-a-python-class-u
#         """
#         def func(*arg, **kwargs):
#             print("AirplaneControllerExtended __getattr__ placement")
#             return None
#
#         return func
#
#     pass
