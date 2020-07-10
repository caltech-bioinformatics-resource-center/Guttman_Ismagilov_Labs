# Guttman_Ismagilov_Labs

#### This github repository includes single-cell SPRITE automatic data processing pipeline (Snakemake workflow) for a research paper [XYZ](https://github.com/caltech-bioinformatics-resource-center/Guttman_Ismagilov_Labs). 
#### The original SPRITE technique has been documented in this paper [Higher-Order Inter-chromosomal Hubs Shape 3D Genome Organization in the Nucleus](https://www.cell.com/cell/pdf/S0092-8674(18)30636-6.pdf).   
#### Snakemake workflow has been tested under UNIX environment with proper pre-installation of necessary software tools. 
####
#### Installation guide:
* Pre-install the following software tools:
  * STAR (generate STAR index for the genome of your interest);
  * samtools
  * bedtools2
  * fastqc
  * Hi-Corrector
* Install scSPRITE data codes `git clone `. Modify `config.yaml` file with local PATH information for STAR, STAR index, samtools, bedtools2, fastqc and Hi-Corrector.

#### Quick run:
* Transfer raw paired-end fastq files (xxx1.fq.gz, xxx2.fq.gz) to raw_fastq directory;
* Try a snakemake dry run: `snakemake -n`;
* If no error message, do a snakemake run with multi cores (e.g., 4 cores): `snakemake --cores 4`.
####
#### Directory contents 
* [scSPRITE](https://github.com/caltech-bioinformatics-resource-center/Guttman_Ismagilov_Labs/tree/master/scSPRITE): A folder with Snakemake workflow scripts to process single-cell SPRITE data.

