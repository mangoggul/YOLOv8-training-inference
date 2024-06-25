import json
import os
from PIL import Image

# COCO 형식의 JSON 어노테이션 파일 경로
json_file_path = 'wheatCOCO/val/labels/instances_val2017.json'

# 이미지 및 라벨 디렉토리
image_dir = 'wheatCOCO/val/images'
label_dir = 'outputValLabels'
os.makedirs(label_dir, exist_ok=True)

# 클래스 목록
classes = ["backGround", "wheat"]

# COCO 형식의 JSON 파일을 로드
with open(json_file_path, 'r') as f:
    coco_data = json.load(f)

# 이미지 ID와 파일명 매핑 생성
image_id_to_filename = {image['id']: image['file_name'] for image in coco_data['images']}

# 이미지 크기 캐시 생성
image_size_cache = {}

# 어노테이션을 YOLO 형식으로 변환
for annotation in coco_data['annotations']:
    image_id = annotation['image_id']
    filename = image_id_to_filename[image_id]
    class_id = annotation['category_id']
    bbox = annotation['bbox']

    # YOLO 형식으로 변환 (x_center, y_center, width, height)
    x, y, width, height = bbox
    x_center = x + width / 2
    y_center = y + height / 2

    # 이미지 크기 비율로 정규화
    if filename not in image_size_cache:
        img_path = os.path.join(image_dir, filename)
        with Image.open(img_path) as img:
            img_width, img_height = img.size
            image_size_cache[filename] = (img_width, img_height)
    else:
        img_width, img_height = image_size_cache[filename]

    x_center /= img_width
    y_center /= img_height
    width /= img_width
    height /= img_height

    # 텍스트 파일로 저장
    label_file_path = os.path.join(label_dir, os.path.splitext(filename)[0] + '.txt')
    with open(label_file_path, 'a') as label_file:
        label_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
