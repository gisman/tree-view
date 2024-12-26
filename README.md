Improved version of the Linux tree utility.

Includes features useful for big data analysis and documentation.

Written for Python 3.12.3, works on Python 3.10 and above. It is expected to work on Python 3.2 and above.

## Features

* Tree structure output
* Size: human-readable
* File count
* File list limit
* Pretty diretory emoji 📂


## Usage

### Print help

> $ treeview -h

```
usage: treeview [-h] [-d] [-L LEVEL] [-n MAX_FILES] [-f] directory

List directory contents.

positional arguments:
  directory             Directory to read

options:
  -h, --help            show this help message and exit
  -d                    List directories only
  -L LEVEL, --level LEVEL
                        Descend only level directories deep
  -n MAX_FILES, --max-files MAX_FILES
                        Print only N files in each directory
  -f, --files-first     Print files before directories

github: https://github.com/gisman/tree-view
```

### Default
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

### List directories only
> $ treeview -d 3d_car_instance_sample
```
📂 3d_car_instance_sample [2 GB]
└──📂 3d_car_instance_sample [2 GB]
    ├──📂 camera [340 B    2 개의 파일]
    ├──📂 car_models [25 MB    79 개의 파일]
    ├──📂 car_poses [1 MB    1,003 개의 파일]
    ├──📂 images [2 GB    1,003 개의 파일]
    └──📂 split [29 KB    2 개의 파일]
```

### Depth limit

> $ treeview -d -L 1 3d_car_instance_sample
```
📂 3d_car_instance_sample [2 GB]
└──📂 3d_car_instance_sample [2 GB]
```

### File List limit

> $ treeview -n 1 3d_car_instance_sample
```
📂 3d_car_instance_sample [2 GB]
└──📂 3d_car_instance_sample [2 GB]
    ├──📂 camera [340 B    2 개의 파일]
    │   └── 5.cam [169 B]
    ├──📂 car_models [25 MB    79 개의 파일]
    │   └── 019-SUV.pkl [338 KB]
    ├──📂 car_poses [1 MB    1,003 개의 파일]
    │   └── 180116_053947113_Camera_5.json [1 KB]
    ├──📂 images [2 GB    1,003 개의 파일]
    │   └── 180116_053947113_Camera_5.jpg [2 MB]
    └──📂 split [29 KB    2 개의 파일]
       └── train.txt [21 KB]
```
