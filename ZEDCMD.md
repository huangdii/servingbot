## zed 관련 

### zed 노드 및 노드릿 실행
제드카메라 nodelet 을 실행, local nodelet 이 실행되며 local 에서 rviz 를 켜서 zed 의 각종 토픽들을 볼 수 있다.
    
    # nodelet 실행하기 
    roslaunch servebot zed_camera_nodelet.launch 

    # node 실행하기 , 원격서버에서 대부분의 topic을 열람할 수 있다.
    rosrun servebot servebot_zed_node 

### zed 기반 rtabmapping (namlonx 로봇에서 실행 ! )
namlonx 로봇에서 ssd 에 저장하는 스크립트

    # 아래 스크립트 실행 이후 만든 파일은 이름을 꼭 변경해야함 ! 
    roslaunch servebot zed_rtabmap_ssd.launch

    # servebot 안에있는 스크립트를 이용해서 쉽게 할 수있음 . 
    rtabmapping.sh <rtabmap이름.db>

### zed를 이용해 svo 녹화하기

    #먼저 노드릿을 켜주고 
    roslaunch servebot zed_nodelet.launch 

    # ros service call 을 통해서 svo file 녹화를 할 수 있다 ! 
    rosservice call /start_svo_recording  --> 녹화시작
    rosservice call /stop_svo_recording --> 녹화 종료

### zed svo 를 가지고 mapping 하기 --> .db 파일을 만드는 작업!    

    # svo file 이 있다면 해당 svo file 을 이용해서 rtabmap 을 만드는 스크립트
    roslaunch servebot zed_rtabmap_svo.launch svo_file:=<svo 파일 이름.svo>

    # zed spatial mapping 을 만들기 
    # params/zed/commons.yaml 에 있는 mapping 옵션을 true 로 바꾸고 아래 명령어를 실행하면 mapping 이 실행됨 ! 
    roslaunch zed_wrapper zed.launch svo_file:=/path/to/file.svo 

[mapping 옵션, service call 을 더 자세히 보려면 여기로!](https://www.stereolabs.com/docs/ros/zed_node/)



### zed 를 이용한  ※ localization .db 파일이 있어야함 

    # .ros/<db이름.db> 기반 localization
    roslaunch servebot zed_rtabmap_localization database_path:=/db파일경로/<db파일이름.db>


### zed laserscan 을 이용한 gmapping ※ 뭔가 별로 안좋음; base_link문제가 의심이 됨

    roslaunch zed_laserscan_gmapping.launch


#### etc zed 실행시 logging 색깔 바꿔주는거
https://termcolor.readthedocs.io/
