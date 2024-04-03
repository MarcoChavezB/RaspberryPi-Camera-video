# RaspberryPi-Camera-video

Instrucciones para configurar y utilizar la cámara en Raspberry Pi para grabación de video.

## Requisitos previos
Asegúrate de haber actualizado tu sistema y haber instalado las siguientes dependencias:

```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
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
sudo apt install python3-pip (Necesario si es version lite)

sudo pip3 install flask
sudo pip3 install numpy
```

## Notas importantes
Deprecated: Las siguientes dependencias están obsoletas y no necesitan ser instaladas:
- libqtgui4
- libqt4-test


## Uso
Una vez instaladas las dependencias navegamos hasta el directorio RaspberryPi-Camera-video y ejecutamos main.py
