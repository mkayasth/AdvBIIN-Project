 <h1> AdvBIIN-Project: ViralGeneClock. </h1>
 

 <h2> // Ongoing project. </h2>
 

<h2> Introduction </h2>
ViralGeneClock is a Linux tool developed through the Ubuntu subsystem. Using ViralGeneClock, the users can deposit the whole genome sequence (WGS) of different strains of a virus. The tool would then examine the evolutionary relationship of the strains, and also compare the mutation rates of the genes across the strains. It uses Prokka for viral genome annotation, Muscle for multiple sequence alignment of each gene for different strains and Neighbor Joining Algorithm for estimating the relative mutation rates of the genes and evolutionary history.

<h2> Usage </h2>

```shell

python3 main.py output-directory
```

<h2> Installations: </h2>

1) Prokka: For detailed Prokka installation in your system, visit this site: https://github.com/tseemann/prokka
 
For brew users in Linux: <br>
minced does not install via brew; but minced is not required for viral annotation. After Brew installs Prokka, uninstall minced, and start working!

 ```shell
brew install brewsci/bio/prokka
brew uninstall minced
```
<b> Add Prokka to your PATH. </b> <br> <br>



2) Muscle: Install Muscle as per your OS from this site: https://github.com/rcedgar/muscle/releases/tag/5.1.0  <br>
<b> Add Muscle to your PATH. </b> <br> <br>



3) Python3: with the Biopython package and other modules (numpy, pandas, matplotlib) for data manipulation and visualization.

If you have pip installed for your Python3, follow these steps:
```shell

python3 -m pip install biopython
python3 -m pip install numpy
python3 -m pip install pandas
python3 -m pip install matplotlib
```
