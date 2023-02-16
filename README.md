# robot-arm
A software for a 6-axis robot arm which can be controlled over usb as well as a web-server with gut to control the robot from any device

The Controller.ino file will serve as a generall controller which is able to operate the robot as well as recieving commands over serial-input such as usb.

The host device will have a web server which allows sending Commands to the robot, creating automations (saved motion coreographys) and shortcuts as well as a 3d rendered robot, to see the previeus of the shortcuts without moving the actual robot
