# 安装lefse

1. 由于lefse使用的环境比较早，建议使用conda虚拟环境的方式安装，可以省掉不少麻烦

```
conda create -n lefse python=2.7 python=2.7 #python这里选成2.7否则会卡住
```

2. 环境安装完成后，进入环境安装lefse

```
source activate lefse
conda install lefse
```

3. Plot_cladogam.py出现错误

   ```
   MatplotlibDeprecationWarning: The set_axis_bgcolor function was deprecated in version 2.0. Use set_facecolor instead.
   ```

   重新安装matplotlib ==1.5.3

   ```
   pip uninstall matplotlib
   
   pip install matplotlib==1.5.3
   ```
