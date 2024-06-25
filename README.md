# YOLOv8-training-inference
![image](https://github.com/mangoggul/YOLOv8-training-inference/assets/102888719/3cdc6ae9-9705-4797-b9bb-54ac4d147d0c)

## How to Use
### 1. First git clone this file 
<br/>
    
```
git clone https://github.com/mangoggul/YOLOv8-training-inference.git
```

### 2. You need to download Training Dataset / Dataset Architecture needs to be 

#### Dataset Tree

```bash
├── dataName
│   ├── train
│         ├── images
│         └── labels
│   ├── val
│         ├── images
│         └── labels
``` 
So For example 
```bash
├── wheatCOCO
│   ├── train
│         ├── images
│         └── labels
│   ├── val
│         ├── images
│         └── labels
``` 
>Important Thing : YOLO doesnt support json Annotation Files so you need to change json to txt<br/>

>if you only have json file use json2txt.py to convert json file to txt

### 3. Start Training
first you need to make yaml file.

```
names:
  0: backGround
  1: wheat
nc : 2

path: C:/Users/user/Desktop/vscodeOD/YOLO_v8/wheatCOCO/  # Base dataset directory
train: train/images
val: val/images

```
this one is my yaml file.  
names : class name 

><YOLO detect background also So if you want to detect 1 object you need to write Object name and background> 

nc : class number

path : dataset Path

train : dataset/train Path

val : dataset/val Path

---

use train.ipynb file to train your own custom data<br/>you can choose epochs, workers, etc. <br/> consider below documents to know more about parameters
>https://docs.ultralytics.com/modes/train/#train-settings

### 4. Inference 
After Training you can use inference.ipynb file. 
from ultralytics import YOLO


```
# Load a model
model = YOLO("runs/detect/train17/weights/best.pt")  # pretrained YOLOv8n model
```

In this part, put your pt file to run inference!

Enjoy Detection!
