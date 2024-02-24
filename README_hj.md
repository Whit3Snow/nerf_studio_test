# data preprocessing

/home/nas4_user/sungwonhwang/ws_student/hyojinjang/nerfstudio/data_spinnerf/

```
#이 디렉토리 안에 train_1_images(1번째 사진) 이랑 10_img(10번째 사진) 있음. 
cd data_spinnerf
```

transforms.json이 있으면 안해도 됨 (data_spinnerf 안에 있음.)
```
ns-process-data images --data /home/nas4_user/sungwonhwang/ws_student/hyojinjang/nerfstudio/data_spinnerf/10_img/images --output-dir ./scene_1_processed
```


# train
```
ns-train nerfacto --data data_spinnerf/10_img  # viewer
ns-train nerfacto --vis tensorboard --data data_spinnerf/10_img # tensorboard

```


그러면 outputs 폴더에 학습 결과 생성됨. 

# camera extract 
```
ns-export cameras --load-config outputs/10_img/nerfacto/2024-02-XX-_XXXXXX/config.yml --output-dir scene_10_poses
```

그러면 scene_10_poses 디렉토리에 transforms_eval.json / transforms_train.json 파일 생성

```
python camera_extract.py --scene 파일생성이름 --width 4032 --height 2268 --fov 40
```
그러면 camera_path_파일생성이름.json 파일이 생성됨. 

# render
```
ns-render camera-path --load-config outputs/10_img/nerfacto/2024-02-XX_XXXXXX/config.yml --rendered-output-names rgb --camera-path-filename camera_path_파일생성이름.json --output-format images --output-path scene_10_rgb

```

그러면 scene_10_rgb 폴더 생기고 그 안에 image들 들어감. 
