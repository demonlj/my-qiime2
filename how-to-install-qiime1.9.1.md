# 还能安装qiime 1.9.1吗？

虽然Qiime2已经发布了几个版本，但网上很多材料还是用qiime1，甚至很多公司回来的数据都是用qiime1分析的。所以，为了防止以后无法安装qiime1，还是在自己电脑上装一个放心点

### Let's Go!

1. 直接安装不行吗？

   `conda create -n qiime1 python=2.7 qiime matplotlib=1.4.3 mock nose -c bioconda`

   会出现如下错误

   ```
   PackagesNotFoundError: The following packages are not available from current channels:
     - qiime -> pynast==1.2.2 -> cogent[version='>=1.5.3'] -> mpi4py[version='>=1.0']
     - qiime -> xorg-libxau
     - qiime -> xorg-libxext
     - qiime -> xorg-libsm
     - qiime -> xorg-libxdmcp
     - qiime -> xorg-libxrender
     - qiime -> natsort[version='<4.0.0']
     - qiime -> libpng[version='>=1.2.50,<1.3.0a0']
     - matplotlib=1.4.3
   ```

2. 先手动新建qiime1环境

   ``conda create -n qiime1 python=2.7 ` # create conda environment "qiime1"  `

3. 进入qiime1环境，pip手动安装

   ```
   conda activate qiime1
   pip install numpy
   pip install cython # 安装biom-format前必须先安装这个
   pip install biom-format==2.1.7 # 从2.1.8版本开始不再支持python2
   pip install qiime
   pip install h5py
   pip install matplotlib==1.4.3
   ```

4. 测试安装结果

   ```
   print_qiime_config.py -t
   ```

5. 备注：国内网络环境建议更换pip源

   ```
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple qiime
   ```

   
