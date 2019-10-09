제드카메라 2cm 씩 차이남 위아래 1미터 왔다갔다할때

https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

sudo make modules_prepare 로 커널 헤더를 준비함 ..? 이걸하니까 됨 ! 

cp cp210x.ko to /lib/modules/<kernel-version>/kernel/drivers/usb/serial

usb/serial 폴더 만듬

insmod /lib/modules/<kernel-version/kernel/drivers/usb/serial/usbserial.ko

이거하려니 없어서 libserial-dev 를 설치
sudo apt-get install libserial-dev

택도 없는짓이라 구글ㄹ링

https://askubuntu.com/questions/935350/ubuntu-16-04-1-usbserial-missing


sudo apt-get install linux-image-extra-virtual

하렸는데 안되서 여기 포럼에서 커널을 업데이트하라는 말을 들음 

https://devtalk.nvidia.com/default/topic/1026162/


make modules_prepare

make M=drivers/usb/serial/

https://developer.nvidia.com/embedded/dlc/sources-r2821
이 링크가 우리꺼 젯슨 커널 

sudo cp drivers/usb/serial/ch341.ko /lib/modules/$(uname -r)/kernel 에다 직접 커널 오브젝트를 넣어줬었음 

insmod cp210x.ko