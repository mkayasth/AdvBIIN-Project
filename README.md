 AdvBIIN-Project

 // Ongoing project.

 Installations:

 1) Prokka: minced does not install via brew; but minced not required for viral annotation. Brew install Prokka, uninstall minced, start working.
       If brew installed:
    > brew install brewsci/bio/prokka
    > brew uninstall minced

Error with hmmer3 for bacterial and archael annotation. However, hmmer3 not required for viral annotation. If you want to work with bacterial genome:
> cpan
> install Bio::searchIO::hmmer3
> exit

2) Muscle: from https://github.com/rcedgar/muscle/releases/tag/5.1.0
 Add Muscle to your PATH.

4) Python3: numpy, pandas, matplotlib, biopython
