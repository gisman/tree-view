# Gimi9 Tree View

향상된 버전의 Linux tree 유틸리티입니다.

빅 데이터 분석 및 문서화에 유용한 기능을 포함하고 있습니다.

Python 3.12.3을 위해 작성되었으며, Python 3.10 이상에서 작동합니다. Python 3.2 이상에서도 작동할 것으로 예상됩니다.

## 기능

* 트리 구조 출력
* 크기: 사람이 읽기 쉬운 형식
* 파일 수
* 파일 목록 제한
* 예쁜 디렉토리 이모지 📂

## 설치

> $ pip install gimi9_tree_view

## 사용법

### 도움말 출력

> $ treeview -h

```
사용법: treeview [-h] [-d] [-L LEVEL] [-n MAX_FILES] [-f] directory

디렉토리 내용을 나열합니다.

위치 인수:
  directory             읽을 디렉토리

옵션:
  -h, --help            이 도움말 메시지를 표시하고 종료합니다
  -d                    디렉토리만 나열합니다
  -L LEVEL, --level LEVEL
                        지정한 깊이만큼 디렉토리를 내려갑니다
  -n MAX_FILES, --max-files MAX_FILES
                        각 디렉토리에서 N개의 파일만 출력합니다
  -f, --files-first     디렉토리보다 파일을 먼저 출력합니다

github: https://github.com/gisman/tree-view
```

### 기본 사용법
> $ treeview 3d_car_instance_sample

```
 📂 3d_car_instance_sample                   [2GB]
    ├── 📂 camera                            [340B 2개의 파일]
    │   ├── 📄 5.cam [169B]
    │   └── 📄 6.cam [171B]
    ├── 📂 car_models                        [25MB 79개의 파일]
    │   ├── 📄 019-SUV.pkl [338KB]
    │   ├── 📄 036-CAR01.pkl [329KB]
    │   ├── 📄 037-CAR02.pkl [354KB]
    │   └── 📄 MG-GT-2015.pkl [313KB]
    ├── 📂 car_poses                         [1MB 1,003개의 파일]
    │   ├── 📄 180116_053947113_Camera_5.json [1KB]
    │   ├── 📄 180116_053947909_Camera_5.json [2KB]
    │   ├── 📄 180116_053948523_Camera_5.json [2KB]
    │   └── 📄 180116_053949115_Camera_5.json [1KB]
    ├── 📂 images                            [2GB 1,003개의 파일]
    │   ├── 📄 180116_053947113_Camera_5.jpg [2MB]
    │   ├── 📄 180116_053947909_Camera_5.jpg [2MB]
    │   ├── 📄 180116_053948523_Camera_5.jpg [2MB]
    │   └── 📄 180116_053949115_Camera_5.jpg [2MB]
    └── 📂 split                             [29KB 2개의 파일]
        ├── 📄 train.txt [21KB]
        └── 📄 val.txt [8KB]
```

### 디렉토리만 나열

> $ treeview -d 3d_car_instance_sample

```
 📂 3d_car_instance_sample                   [2GB]
    ├── 📂 camera                            [340B 2개의 파일]
    ├── 📂 car_models                        [25MB 79개의 파일]
    ├── 📂 car_poses                         [1MB 1,003개의 파일]
    ├── 📂 images                            [2GB 1,003개의 파일]
    └── 📂 split                             [29KB 2개의 파일]
```

### 깊이 제한

> $ treeview -d -L 1 train
```
 📂 train                                    [9GB 1개의 파일]
    ├── 📂 camera                            [66B 1개의 파일]
    ├── 📂 car_poses                         [12MB 4,283개의 파일]
    ├── 📂 ignore_mask                       [614MB 4,283개의 파일]
    ├── 📂 images                            [8GB 4,283개의 파일]
    ├── 📂 keypoints                         [17MB]
    └── 📂 split                             [130KB 2개의 파일]
```

### 파일 목록 제한

> $ treeview -n 1 3d_car_instance_sample
```
 📂 3d_car_instance_sample                   [2GB]
    ├── 📂 camera                            [340B 2개의 파일]
    │   └── 📄 5.cam [169B]
    ├── 📂 car_models                        [25MB 79개의 파일]
    │   └── 📄 019-SUV.pkl [338KB]
    ├── 📂 car_poses                         [1MB 1,003개의 파일]
    │   └── 📄 180116_053947113_Camera_5.json [1KB]
    ├── 📂 images                            [2GB 1,003개의 파일]
    │   └── 📄 180116_053947113_Camera_5.jpg [2MB]
    └── 📂 split                             [29KB 2개의 파일]
        └── 📄 train.txt [21KB]
```

