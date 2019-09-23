# Serving robot


```bash
# house map 을 시작하기 
roslaunch servebot house.launch
```
![image](pictures/gazebo.png)

```bash
# 실제 로봇 Simulation -  Gazebo 
roslaunch servebot rrbot_world.launch

# Rviz 로 topic 현황 확인하기 
roslaunch servebot rrbot_rviz.launch   
```
![image](pictures/gazebo_rviz.png)

```bash
# 현재 Robot Camera streaming record하기
# script 실행시킨 디렉토리 위치에 'output.avi'로 저장 됨
rosrun servebot CamRecord.py
```
