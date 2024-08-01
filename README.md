# Policy Management: OPA Gatekeeper & Kyverno Evaluation


As a cybersecurity research intern for Platform One, the purpose of this project is to conduct a comprehensive evaluation of Kyverno and Gatekeeper, two prominent policy management tools for Kubernetes. The goal is to analyze their respective capabilities, performance, and suitability for enforcing policies within Kubernetes clusters. This evaluation will provide valuable insights and recommendations to enhance Platform One's policy enforcement strategies, ensuring robust security, compliance, and operational efficiency in managing Kubernetes resources.



## Description

I have developed a code that pulls YAML files from the cloned Big Bang repository and analyzes them. The purpose of this project is to conduct a detailed evaluation of two prominent policy management tools for Kubernetes: Kyverno and Gatekeeper. By leveraging the extracted YAML files, this evaluation aims to compare and contrast the capabilities, performance, and suitability of Kyverno and Gatekeeper in enforcing policies within Kubernetes clusters.


## Getting Started

### Dependencies

* Visual Studio Code (VSCode):
Integrated development environment used for writing and editing the code.
Installed YAML extension in VSCode for syntax highlighting and validation.

* Access to the Big Bang Repository:
The Big Bang repository is publicly accessible and contains the YAML files needed for analysis.
Cloned the repository locally for file access and manipulation.

* Python 3:

Used as the primary programming language for developing the code to pull and analyze YAML files.
Installed necessary Python libraries, including PyYAML for parsing YAML files.


### Installing

* Clone the Big Bang/Platform One Repository:
Open a terminal and run the following command to clone the repository:
git clone https://github.com/big-bang-repo/big-bang.git

* Set Up an Integrated Development Environment (IDE):
While Visual Studio Code (VSCode) is recommended, any IDE can be used for this project. Download and install your preferred IDE.

* Install the YAML Extension (if using VSCode):
Open VSCode. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
Search for "YAML" and install the extension provided by Red Hat.

* Install Python 3:
Download and install Python 3 from here.
Ensure that Python is added to your PATH during installation.

### Executing program

* Place the Python Script: (Provided in Code Sections)
Download the provided Python script (gatekeeper_yaml_pull.py) and place it in the root directory of the cloned repository.

* Navigate to the Repository:
Open a terminal and navigate to the root directory of the cloned repository.
Run the Script: (Provided in Code Sections)



## Help

* If the required packages are not installed, the code might not run properly, leading to potential errors or unexpected behavior. For instance, the script relies on the PyYAML library to parse YAML files; without it, the script will fail with an import error. Additionally, using an IDE without the YAML extension might result in incorrect syntax highlighting and validation, making it harder to identify issues in the YAML files. Ensuring that all dependencies are correctly installed is crucial for the script to execute smoothly and produce organized and readable output. If you encounter any issues, verify that Python 3 and all necessary libraries, like PyYAML, are installed and up to date.



## Authors

Contributors names and contact info

ex. Oluwatomisin Omonira
ex. [tomomonira@gmail.com] (https://www.linkedin.com/in/oluwatomisin-omonira-a16238278/)

## Version History

* 0.2
    * Various bug fixes and optimizations
* 0.1
    * Initial Release

## License

This project is licensed under the [GNU GPLv3] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [PlatformOne](https://github.com/DoD-Platform-One)
