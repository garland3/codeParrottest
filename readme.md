# setup

* setup on `rupod.io`

`workspace` is the persistent directory

```bash
cd /workspace
mkdir temp
mkdir anaconda
mkdir git
cd temp
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh
chmod +x Miniconda3-py37_4.12.0-Linux-x86_64.sh
./Miniconda3-py37_4.12.0-Linux-x86_64.sh -b -f -p /workspace/anaconda
# I had to move to the anaconda location to find conda
cd /workspace/anaconda/bin
conda init bash
# restart a terminal
cd /workspace/git
conda create --name test1 python=3.10
conda activate test1
conda config --add channels conda-forge
conda config --add channels pytorch
```


### now we can start coding. 
```bash
conda install -c conda-forge transformers
conda install ipykernel
```

In VScode install the python tools, and then I can run interactive python files in a jupyter notebook like way. 


