# Fast install qiime2 in China region

Qiime2 更新还算频繁，虽说通过conda安装很简单，但每次安装都慢的要（而且conda的wget无法断点续传），尤其在国内。以2019.10为例解释如何快速安装qiime2

1. 分析`qiime2-2019.10-py36-osx-conda.yml`文件

   1. Channels 有4个，其中2-4有国内镜像可以替换，只有第一个不行

      ```
      - qiime2/label/r2019.10
      - conda-forge
      - bioconda
      - defaults
      ```

      替换为

      ```
      - qiime2/label/r2019.10
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda
      - defaults
      ```

      这样可以解决除了qiime2安装包以外的下载问题

   2. Dependencies 

      删除qiime2相关包，等建立好conda的env之后再单独安装

      ```
      - q2-alignment=2019.10.0
      - q2-composition=2019.10.0
      - q2-cutadapt=2019.10.0
      - q2-dada2=2019.10.0
      - q2-deblur=2019.10.0
      - q2-demux=2019.10.0
      - q2-diversity=2019.10.0
      - q2-emperor=2019.10.0
      - q2-feature-classifier=2019.10.0
      - q2-feature-table=2019.10.0
      - q2-fragment-insertion=2019.10.0
      - q2-gneiss=2019.10.0
      - q2-longitudinal=2019.10.0
      - q2-metadata=2019.10.0
      - q2-phylogeny=2019.10.0
      - q2-quality-control=2019.10.0
      - q2-quality-filter=2019.10.0
      - q2-sample-classifier=2019.10.0
      - q2-taxa=2019.10.0
      - q2-types=2019.10.0
      - q2-vsearch=2019.10.0
      - q2cli=2019.10.0
      - q2templates=2019.10.0
      - qiime2=2019.10.0
      ```

2. 执行conda命令`conda env create -n qiime2-2019.10 --file qiime2-2019.10-py36-osx-conda.yml`，速度应该很快

3. 下载qiime2相关包

   1. 获取包名称及md5

      ```
      conda search q2 --info -c qiime2/label/r2019.10 > ~/qiime2.packages
      ```

      vim编辑器

      ```
      $ vi qiime2.packages
      :%s/^\(url.*\)\n\(md5 \+: \)/\1:/
      :v/^http/d
      :v/qiime2/d
      :wq
      ```

   2. 下载

      ```
      python3 fetch-qiime2-packages.py
      ```

4. 安装qiime2软件包

   ```
   $ for n in `*.bz2`
   do
   conda install --offline $n
   done
   ```
##Note: 

- 仅仅适用于OSX，如果是linux，需要修改python文件中的prefix
