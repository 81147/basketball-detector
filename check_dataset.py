from pathlib import Path
import yaml
import cv2
import random

ROOT = Path(__file__).parent
DATA_YAML=ROOT/"dataset"/"data.yaml"
with open(DATA_YAML,"r",encoding="utf-8")as f:
    data = yaml.safe_load(f)
dataset_dir = DATA_YAML.parent

base_path = dataset_dir / data["path"]
train_images = base_path / data["train"]
val_images = base_path / data["val"]
train_imgs = list(train_images.glob("*"))

def check_split(images_dir,labels_dir):
    img_paths = list(images_dir.glob("*.jpg"))

    total_imgs = len(img_paths)
    missing = 0
    total_boxes = 0
    bad_class = 0
    out_of_range = 0
    
    for img_path in img_paths:
        stem = img_path.stem
        label_path = labels_dir / (stem + ".txt")
        if not label_path.exists():
            missing+=1
            continue
        content = label_path.read_text(encoding="utf-8")
        lines = content.strip().split("\n")
        for line in lines:
            parts = line.split()
            if len(parts) != 5:
                continue
            cls = int(parts[0])
            x,y,w,h = float(parts[1]),float(parts[2]),float(parts[3]),float(parts[4])
            total_boxes+=1
            if cls != 0:
                bad_class+=1
            if not(0<=x<=1 and 0<=y<=1 and 0<w<=1 and 0<h<=1):
                out_of_range+=1
    print("图片数量：",total_imgs)
    print("缺失标签：",missing)
    print("总框数量：",total_boxes)
    print("class_id非0：",bad_class)
    print("坐标越界",out_of_range)

def draw_samples(images_dir,labels_dir,out_dir,n=5):
    out_dir.mkdir(exist_ok=True)
    img_paths=list(images_dir.glob("*.jpg"))
    chosen=random.sample(img_paths,n)
    for img_path in chosen:
        img=cv2.imread(str(img_path))
        if img is None:
            print("读图失败",img_path)
            continue
        img_h,img_w = img.shape[:2]
        label_path=labels_dir/(img_path.stem+".txt")
        content=label_path.read_text(encoding="utf-8")
        for line in content.strip().split("\n"):
            parts = line.split()
            if len(parts)!=5:
                continue
            xc=float(parts[1])
            yc=float(parts[2])
            w=float(parts[3])
            h=float(parts[4])
            x1=int((xc-w/2)*img_w)
            y1=int((yc-h/2)*img_h)
            x2=int((xc+w/2)*img_w)
            y2=int((yc+h/2)*img_h)
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        save_path=out_dir/img_path.name
        cv2.imwrite(str(save_path),img)
        print("已保存",save_path)
        
check_split(train_images,train_images.parent/"labels")
check_split(val_images,val_images.parent/"labels")
DEBUG_DIR=ROOT/"debug"
draw_samples(train_images,train_images.parent/"labels",DEBUG_DIR,n=5)







        
    
