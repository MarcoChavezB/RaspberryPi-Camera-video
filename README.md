# RaspberryPi-Camera-video

Instrucciones para configurar y utilizar la cámara en Raspberry Pi para grabación de video.

## Configuracion Raspi-camera

```bash
sudo raspi-config
  - interface options
      Legacy Camera [Enabled]
      VNC [Enabled]
```


## Requisitos previos
Asegúrate de haber actualizado tu sistema y haber instalado las siguientes dependencias:

```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
 - sudo apt-get install libjasper-dev
sudo apt-get install libhdf5-dev

sudo apt-get install libopencv-dev python3-opencv
```

## Instalación de OpenCV

```bash
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python
```

## Instalación de dependencias adicionales

```bash
(Necesario si es version lite)
sudo apt install python3-pip

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install imutils
sudo pip3 install picamera[array]

```

## Notas importantes
Deprecated: Las siguientes dependencias están obsoletas y no necesitan ser instaladas:
- libqtgui4
- libqt4-test


## Uso
Una vez instaladas las dependencias navegamos hasta el directorio RaspberryPi-Camera-video y ejecutamos main.py


## Preview
![Captura desde 2024-04-02 23-26-18](https://github.com/MarcoChavezB/RaspberryPi-Camera-video/assets/123757334/d547ca0f-2ed3-432a-8f57-debbd7e496f7)


