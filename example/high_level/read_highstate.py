import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize

from unitree_sdk2py.idl.default import unitree_go_msg_dds__SportModeState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_


def HighStateHandler(msg: SportModeState_):


    # print("imu_state rpy is : ", msg.imu_state.rpy) # roll to left is negative, roll to right is positive. 
                                                    # pitch up is negative, pitch down is positive. 
                                                    # yaw, right is negative, left is positive.

    # print('#' * 80)
    print("Position: ", msg.position)  # [0.7058750987052917, 2.2694053649902344, 0.0498991422355175]  forward and left is positive. normally standup z is 0.316
    # print("Velocity: ", msg.velocity)  # [-0.015101952478289604, 0.007969869300723076, -0.010988537222146988]
    # print("Yaw velocity: ", msg.yaw_speed)  # -0.004261057358235121  yaw to left is positive, yaw to right is negative
    # print("Foot position in body frame: ", msg.foot_position_body)  # [0.2040419727563858, -0.14439928531646729, -0.06941508501768112, 0.20272481441497803, 0.1433950513601303, -0.06855681538581848, -0.18394531309604645, -0.15891306102275848, -0.03322017937898636, -0.18634292483329773, 0.16037331521511078, -0.03440554440021515]
    # print("Foot velocity in body frame: ", msg.foot_speed_body)  # [-0.00022158260981086642, 0.004106577951461077, -0.0035810077097266912, -0.00016417723963968456, -0.0037794357631355524, -0.002281155437231064, 0.004133503884077072, -0.0009295002091675997, -0.0027029241900891066, 0.00011078730312874541, -0.0010817940346896648, 0.007877965457737446]


    # print('#' * 80)
    # print("stamp : ", msg.stamp)  # TimeSpec_(sec=1726944379, nanosec=428202803)
    # print("error_code : ", msg.error_code)  # 0
    # print("imu_state : ", msg.imu_state)  # MUState_(quaternion=[-0.968059778213501, -0.006306705996394157, 0.053207866847515106, -0.2449275702238083], gyroscope=[0.012783171609044075, -0.0021305286791175604, -0.004261057358235121], accelerometer=[0.8415619134902954, -0.03711012750864029, 9.641449928283691], rpy=[-0.013932709582149982, -0.1063062846660614, 0.49635809659957886], temperature=80)
    # print("mode : ", msg.mode)  # 7
    # print("progress : ", msg.progress)  # 0
    # print("gait_type : ", msg.gait_type) # 1
    # print("foot_raise_height : ", msg.foot_raise_height) # 0.09000000357627869
    # print("position : ", msg.position)  # [0.7058767676353455, 2.269404888153076, 0.04989853501319885]
    print("body_height : ", msg.body_height)  # 0.3199999928474426
    # print("velocity : ", msg.velocity)  # [-0.015073548071086407, 0.008032148703932762, -0.011166661977767944]
    # print("yaw_speed : ", msg.yaw_speed)  # -0.0063915858045220375
    # print("range_obstacle : ", msg.range_obstacle)  # [2.0, 2.0, 2.0, 2.0]
    # print("foot_force : ", msg.foot_force)  # [15, 14, 16, 16]
    # print("foot_position_body : ", msg.foot_position_body)  # [0.2040419727563858, -0.14440138638019562, -0.06941211968660355, 0.20272056758403778, 0.1433992087841034, -0.06855150312185287, -0.18394531309604645, -0.15891405940055847, -0.03321677818894386, -0.18634101748466492, 0.16037333011627197, -0.03441193699836731]
    # print("foot_speed_body : ", msg.foot_speed_body)  # [-0.0016539974603801966, 0.004070406313985586, -0.004647781141102314, -0.007219802588224411, 0.004715122748166323, 0.010087724775075912, 0.003343236865475774, -0.0030250512063503265, 0.004163768608123064, 0.001835255534388125, -0.0005620100419037044, -0.004121926613152027]
    # print("path_point : ", msg.path_point)  # PathPoint_(t_from_start=0.0, x=0.0, y=0.0, yaw=0.0, vx=0.0, vy=0.0, vyaw=0.0)
    

    # stamp: 'unitree_sdk2py.idl.unitree_go.msg.dds_.TimeSpec_'
    # error_code: types.uint32
    # imu_state: 'unitree_sdk2py.idl.unitree_go.msg.dds_.IMUState_'
    # mode: types.uint8
    # progress: types.float32
    # gait_type: types.uint8
    # foot_raise_height: types.float32
    # position: types.array[types.float32, 3]
    # body_height: types.float32
    # velocity: types.array[types.float32, 3]
    # yaw_speed: types.float32
    # range_obstacle: types.array[types.float32, 4]
    # foot_force: types.array[types.int16, 4]
    # foot_position_body: types.array[types.float32, 12]
    # foot_speed_body: types.array[types.float32, 12]
    # path_point: types.array['unitree_sdk2py.idl.unitree_go.msg.dds_.PathPoint_', 10]




if __name__ == "__main__":
    # sys.argv[1]: name of the network interface
    ChannelFactoryInitialize(0, sys.argv[1])
    sub = ChannelSubscriber("rt/sportmodestate", SportModeState_)
    sub.Init(HighStateHandler, 10)

    while True:
        time.sleep(10.0)
