# Guttman_Ismagilov_Labs

#### This github repository includes single-cell SPRITE automatic bioinformatic pipeline (Snakemake workflow) to process mouse scSPRITE data for a research paper [XYZ](https://github.com/caltech-bioinformatics-resource-center/Guttman_Ismagilov_Labs). 
#### The original SPRITE technique has been documented in this paper [Higher-Order Inter-chromosomal Hubs Shape 3D Genome Organization in the Nucleus](https://www.cell.com/cell/pdf/S0092-8674(18)30636-6.pdf).   
#### This Snakemake workflow has been tested under Centos7 environment with proper pre-installation of necessary software tools. 
####
#### Installation guide:
* Pre-install the following software tools:
  * STAR (generate STAR index for the genome of your interest);
  * samtools
  * bedtools2
  * fastqc
  * Hi-Corrector
* Install scSPRITE source codes `git clone https://github.com/caltech-bioinformatics-resource-center/Guttman_Ismagilov_Labs.git`. Modify `config.yaml` file with local PATH information for STAR, STAR index, samtools, bedtools2, fastqc and Hi-Corrector.

#### Quick run:
* `cd scSPRITE`.
* Transfer raw paired-end fastq files (xxx1.fq.gz, xxx2.fq.gz) to raw_fastq directory;
* Try a snakemake dry run: `snakemake -n`;
* If no error message, perform first step snakemake run with multi cores (e.g., 4 cores): `snakemake --cores 4`.
* If no error message, do second step snakemake run with multi cores （e.g., 4 cores): `snakemake -s Snakefile_contact_heatmap --cores 4`. 
####
#### Directory contents 
* [scSPRITE](https://github.com/caltech-bioinformatics-resource-center/Guttman_Ismagilov_Labs/tree/master/scSPRITE): A folder with Snakemake workflow scripts to process single-cell SPRITE data.

