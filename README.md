**Contig Analysis Script**
---
*Overview*
This script is designed to analyze a file containing data about contigs, which are contiguous sequences typically found in DNA sequence assemblies. It calculates important metrics such as N50 and L50, which are commonly used in genomics to assess the quality of a genome assembly.

**Usage**
---
*Prerequisites*
Python 3.x installed on your system

**Running the Script**
---
Clone the Repository: Clone or download the repository containing the script to your local machine.

Navigate to the Directory: Open a terminal or command prompt and navigate to the directory where the script (L50N50.py) is located.

Run the Script: Execute the script by running the following command: python L50N50.py

Follow the Prompts: The script will prompt you to enter the path to the file you want to analyze. Make sure to provide the correct path to the file.

View the Results: Once the script completes execution, it will display the results, including the total contig length, the amount of contigs, N50 value, and L50 value.

**File Format**
---
The script expects the input file to be in a specific format:

Each line should represent a contig.
Fields in each line should be separated by tabs.
The third field should contain the length of the contig, preceded by 'LN:'
This is a usual .txt file resulting from basic contig analysis in bash using gatk

Example of the format can be found in examplefile.txt

**Additional Information**
---
N50 Value: The N50 value represents the length of the shortest contig such that at least 50% of the total length is contained in contigs of that length or longer.

L50 Value: The L50 value represents the number of contigs that make up the N50 value.

Output: The script will display the results in the console. You can also modify the script to save the results to a file if needed.

**Troubleshooting**
---
If you encounter any issues while running the script, ensure that you have provided the correct path to the input file and that the file is formatted correctly.
