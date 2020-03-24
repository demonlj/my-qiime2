# Fast install qiime2 in China region 

Qiime2 更新还算频繁，虽说通过conda安装很简单，但每次安装都慢的要（而且conda的wget无法断点续传），尤其在国内。~~以2019.10为例解释如何快速安装qiime2~~

update for 2020.2



1. 依赖

   ```
   system： linux or OSX
   conda
   gnu-sed for OSX
   ```

   

2. 根据官方文档获取yml文件：qiime2-2020.2-py36-linux-conda.yml 或者 qiime2-2020.2-py36-osx-conda.yml

3. 替换国内镜像。Channels 有4个，其中2-4有国内镜像可以替换，只有第一个不行

   1. Linux

   ```
   sed -i "s/conda-forge/https:\/\/mirrors.tuna.tsinghua.edu.cn\/anaconda\/cloud\/conda-forge/" qiime2-2020.2-py36-linux-conda.yml
   sed -i "s/bioconda/https:\/\/mirrors.tuna.tsinghua.edu.cn\/anaconda\/cloud\/bioconda/" qiime2-2020.2-py36-linux-conda.yml
   sed -i "/^- q2/d" qiime2-2020.2-py36-linux-conda.yml
   sed -i "/^- qiime2/d" qiime2-2020.2-py36-linux-conda.yml
   ```

   2. OSX

   ```
   gsed -i "s/conda-forge/https:\/\/mirrors.tuna.tsinghua.edu.cn\/anaconda\/cloud\/conda-forge/" qiime2-2020.2-py36-osx-conda.yml
   gsed -i "s/bioconda/https:\/\/mirrors.tuna.tsinghua.edu.cn\/anaconda\/cloud\/bioconda/" qiime2-2020.2-py36-osx-conda.yml
   gsed -i "/^- q2/d" qiime2-2020.2-py36-osx-conda.yml
   gsed -i "/^- qiime2/d" qiime2-2020.2-py36-osx-conda.yml
   ```

4. 执行conda命令，速度快多了

   1. Linux

      `conda env create -n qiime2-2020.2 --file qiime2-2020.2-py36-linux-conda.yml`

   2. OSX
      `conda env create -n qiime2-2020.2 --file qiime2-2020.2-py36-osx-conda.yml`

5. 下载qiime2相关包

   1. 进入qiime2环境

      `conda activate qiime2-2020.2`

   2. 下载并按照qiime2相关包

   ```
   python3 install-qiime2-packages.py
   ```

## Note: 

- 仅仅适用于OSX和linux。~~需要修改python文件中的prefix，需要做相应修改。~~

## 安装q2-studio

npm下载electron非常慢

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
pip install .
cnpm install
```
