# 각종 설치 


## 그래픽드라이버 설치 및 커널 업데이트로 인한 고통 

https://docs.nvidia.com/cuda/archive/10.0/cuda-installation-guide-linux/index.html

openssl 1.1 을 받아야함 
wget https://www.openssl.org/source/openssl-1.1.0l.tar.gz

우분투 16.04 에서  kernel 5.1 업데이트하는거 --> https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.1.21/ 에서 데비안 페키지를 
wget 으로 전부 받고 dpkg 로 인스톨한다

nvidia 드라이버는 410 이 kernel 5.1 과 호환이 안되는듯해서 호환이 되는 드라이버를 깔아야할듯 

일단 이거 포기하고 430으로 가기로함 근데 깔때마다 
ssl 1.1 이 문제가 났었음 

다행히
http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.0k-1~deb9u1_amd64.deb 여기서 데비안 페키지 ssl1.1 을 운좋게 받을 수 
있었다


이제 NVIDIA 설치를 하려는데 

cc_version_check 에서 문제가 난다 ;

CC  환경변수를 gcc-5 <경로>

이것도 안되서 
sudo apt-get install module-assistant
su -c 'm-a prepare' 를 하라는 누군가의 말을 듣고 이걸따라해봄


이것도 꽝이어서 gcc-9 를 받음 왜냐면 내가 커널 빌드할때 쓴게 gcc-9 이기 때문
그래서 이걸로 바꾼뒤에 

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 \
                         --slave /usr/bin/g++ g++ /usr/bin/g++-5 

를 한뒤에 다시 엔비디아 드라이버를 깜


오른쪽 컴에 
https://www.nvidia.com/Download/index.aspx
드가서 다시 드라이버 깜


pre-install 없애던가 이름 바꾸던가해서 스크립트 충돌없애고 엔비디아 드라이버 깔기 


다 지우고 까니까 이제는 로그인이 안댐
