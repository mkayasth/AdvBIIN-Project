 <h1> AdvBIIN-Project: ViralGeneClock. </h1>
 

 <h2> // Ongoing project. </h2>
 

<h2> Introduction </h2>
ViralGeneClock is a Linux tool developed through the Ubuntu subsystem. Using ViralGeneClock, the users can deposit the whole genome sequence (WGS) of different strains of a virus. The tool would then examine the evolutionary relationship of the strains, and also compare the mutation rates of the genes across the strains. It uses Prokka for viral genome annotation, Muscle for multiple sequence alignment of each gene for different strains and Neighbor Joining Algorithm for estimating the relative mutation rates of the genes and evolutionary history.

<h2> Usage </h2>

```shell

python3 main.py output-directory
```

<h2> Installations </h2>

<h3>1) Prokka:</h3> For detailed Prokka installation instructions for your OS, visit this site: https://github.com/tseemann/prokka <br> <br>
 
For brew users in Linux: <br>
minced does not properly install via brew; but minced is not required for viral annotation. After Brew installs Prokka, uninstall minced, and start working!

 ```shell
brew install brewsci/bio/prokka
brew uninstall minced
```

For Ubuntu users with sudo access, you can also follow these steps:
```shell
sudo apt-get install libdatetime-perl libxml-simple-perl libdigest-md5-perl git default-jre bioperl
sudo cpan Bio::Perl
git clone https://github.com/tseemann/prokka.git $HOME/prokka
$HOME/prokka/bin/prokka --setupdb
```
<h4> Add Prokka to your PATH. </h4> <br>

<h3>2) Muscle:</h3> For detailed Muscle installation instructions for your OS, visit this site: https://github.com/rcedgar/muscle/releases/tag/5.1.0  <br>
<h4> Add Muscle to your PATH. </h4> <br>

<h3>3) Python3:</h3> Biopython package with other modules (numpy, pandas, matplotlib) for data manipulation and visualization.

If you have pip installed for your Python3, follow these steps:
```shell

python3 -m pip install biopython
python3 -m pip install numpy
python3 -m pip install pandas
python3 -m pip install matplotlib
```
<h3>Note: </h3>This tool executes scripts using the 'python3' command, so ensure Python 3 is installed on your system. Additionally, all required packages mentioned above must be installed for the Python3 environment that is invoked when you run 'python3' from the command line.
