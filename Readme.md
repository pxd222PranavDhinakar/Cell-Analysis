Here's a concise explanation of the notebook's functionality and usage:

## Cell Analysis Jupyter Notebook

This notebook provides tools for analyzing fluorescence microscopy images (.tif files) to count total cells and fluorescent (green) cells. 

### Core Functions

1. `list_tif_files(directory=".")`:
   - Recursively searches directories for .tif files
   - Returns list of file paths and prints file locations

2. `count_cells(image_path)`:
   - Processes individual .tif files
   - Uses OpenCV for image processing
   - Detects cells based on size and circularity
   - Identifies green fluorescent cells using intensity thresholds
   - Returns total cell count, green cell count, and saves visualization

3. `process_files(file_paths, save_visualizations=True)`:
   - Batch processes multiple images
   - Generates results dictionary for each image
   - Includes file info, cell counts, and green percentages

4. `display_tiff_images(file_paths, figsize=(15, 15))`:
   - Displays original .tif images
   - Can show single image or grid of multiple images

5. `process_all_files_to_csv(tif_files, output_csv_path="cell_counts.csv")`:
   - Processes all files and saves results to CSV
   - Provides summary statistics
   - Returns results as pandas DataFrame

### Usage Example

```python
# Import required libraries
import cv2
import numpy as np
from pathlib import Path
import tifffile
import os
import matplotlib.pyplot as plt
import pandas as pd

# Find all .tif files in directory
tif_files = list_tif_files("your/directory/path")

# Process all files and save results
results_df = process_all_files_to_csv(tif_files, "output.csv")

# View an image
display_tiff_images(tif_files[0])  # Single image
display_tiff_images(tif_files[0:5])  # Multiple images
```

### Key Features
- Handles batch processing of multiple images
- Saves analyzed images with cell detection visualization
- Exports results to CSV for further analysis
- Provides error handling for file processing issues
- Calculates percentage of green fluorescent cells
- Supports multiple trials and experimental conditions

The notebook is configured to work with a directory structure containing different experimental trials, timepoints, and treatment conditions (e.g., control, DFCP1, ATG13 with various concentrations).