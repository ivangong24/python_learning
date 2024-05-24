## ---------------------------
##
## Script name: 1-install_packages.R
##
## Purpose of script: To install the necessary Python packages for the project
##
## Author: Yufan Gong
##
## Date Created: 2024-05-12
##
## Copyright (c) Yufan Gong, 2024
## Email: ivangong@ucla.edu
##
## ---------------------------
##
## Notes:
##   
##
## ---------------------------

if (!require("reticulate", quietly = TRUE)) {
  install.packages("reticulate")
}
library(reticulate)

py_list_packages() # List all installed Python packages
py_install(c("pandas", "numpy", "pyprojroot", 
             "matplotlib", "Seaborn", "plotly", "pyodbc"))

