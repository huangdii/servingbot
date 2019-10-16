# Map Server Package


## Yaml 

    이게 멥 메타 데이타임 , 이미지 파일이름 정해주고 인코딩 관련 데이타를 만들어주게끔해준다

    OS X 에서의 PNG 파일 빼고는 대부분의 이미지를 정해준다 
    
### YAML FOrmat 

ex) 
    
    image: testmap.png
    resolution: 0.1
    origin: [0.0, 0.0, 0.0]
    occupied_thresh: 0.65
    free_thresh: 0.196
    negate: 0

- image
    
    image 는 이미지 경로를 정하는거임

- resolution

    meter/pixel

- origin

    지도의 왼쪽 아래부분의 좌표를 x,y,yaw 순으로 들어간 값임 오른쪽, 아래쪽으로 가는 방향이 -방향이다

- occupied_thresh

    이 값보다 큰 occupancy probability 를 가진 픽셀은 채워진걸로 인식함

- free_thresh

    이값보다 작은 occupancy probability 를 가진 픽셀은 비어있는 걸로 간주함

- negate 

    map 색깔을 반전시킬지 말지 정함, 0 이면 흰색 바탕에 검은색 지도 1 이면 반대

- mode 

    scale, trinary, raw 값을 정해준다. 기본적으로 trinary 값으로 설정되있음 
    
    - trinary 의 경우 세가지 해석을 준다는 뜻임 
        - p > occupancy_thresh 이면 __100__ 을 반환해서 셀이 채워졌다고 알려줌
        - p < free_thresh 이면 __0__ 을 반환해서 cell 이 비워져있다고 알려줌 
        - 그외의 경우 -1 을 반환(unsigned char 로 255 ), unknown 으로 반환됨 
    - scale 
        - p > occupancy_thresh 이면 __100__ 
        - p < free_trhesh 이면 __0__
        - 그외의 경우 99* (p -free_thresh ) / (occupied_thresh- free_thresh) 반환
        0 ~ 100 까지의 full gradient  value 들을 출력하게끔 해준다고함 

    - raw 
        - [0 ~ 255 ] 까지의 픽셀값을 그대로 출력

## command-line tools 

- 사용방법

    map_server <map.yaml>

- 예시
            
    rosrun map_server map_server mymap.yaml

- 발행되는 토픽들 

|타입|노드 이름 | 토픽 or 변수 |설명|
|-|-|-|-|
|Publish|__map_metadata__|nav_msgs/MapMetaData|맵 메타데이타를 받음
|Publish|__map__|nav_msgs/OccupancyGrid| 멥을 받음 (latched topic)
|Service|__static_map__|nav_msgs/GetMap| 멥을 받음(service)
|hyper parameter|frame_id|string, default="map"| 발행된 맵의 프레임(이름)

- map_saver
    - Usage
        
        rosrun map_server map_saver [--occ <threshold_occupied>] [--free <threshold_free>] [-f <mapname>]

    - Example

        rosrun map_server map_saver -f mymap

    - Subscribed Topics 

        nav_msgs/OccupancyGrid







[map_server문서](http://wiki.ros.org/map_server)
<!-- TODO 기술문서 요약해서 우리가 쓸 API, Wrapper 정리 -->


