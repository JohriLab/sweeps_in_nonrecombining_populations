import os
import numpy as np
from collections import defaultdict
import sys

def process_folder(folder_path, max_key=20):
    """Process all files while preserving individual file histograms"""
    file_histograms = []  # Store each file's normalized histogram
    file_count = 0
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r') as f:
                    values = [int(line.strip()) for line in f if line.strip()]
                    
                    hist = defaultdict(int)
                    for val in values:
                        if 1 <= val <= max_key:
                            hist[val] += 1
                    
                    total = sum(hist.values())
                    if total == 0:
                        continue
                    
                    # Store normalized histogram for this file
                    norm_hist = {k: v/total for k,v in hist.items()}
                    file_histograms.append(norm_hist)
                    file_count += 1
                    
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
                continue
    
    # Convert to numpy arrays for efficient storage
    all_data = []
    for hist in file_histograms:
        arr = np.zeros(max_key)
        for k,v in hist.items():
            arr[k-1] = v  # key=1 → index 0
        all_data.append(arr)
    
    return np.array(all_data), file_count

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python process_histograms.py <base_dir> <task_id> <output_dir>")
        sys.exit(1)
        
    base_dir = sys.argv[1]
    task_id = int(sys.argv[2])
    output_dir = sys.argv[3]
    
    folder_path = os.path.join(base_dir, str(task_id))
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found!")
        sys.exit(1)
    
    histograms, count = process_folder(folder_path)
    output_path = os.path.join(output_dir, f"histograms_{task_id}.npy")
    np.save(output_path, histograms)
    print(f"Saved {count} file histograms from folder {task_id}")

# import os
# import numpy as np
# from collections import defaultdict
# from pathlib import Path

# def process_files(base_dir, max_key=20):
#     # Initialize dictionaries to store:
#     # - Sum of normalized histogram values
#     # - Sum of squares for variance calculation
#     norm_hist_sums = defaultdict(float)
#     norm_hist_sums_sq = defaultdict(float)
#     file_count = 0
    
#     # Walk through all directories from 1 to 47
#     for dir_num in range(1, 48):
#         dir_path = os.path.join(base_dir, str(dir_num))
#         if not os.path.exists(dir_path):
#             continue
            
#         # Process each file in the directory
#         for filename in os.listdir(dir_path):
#             if filename.endswith('.txt'):
#                 file_path = os.path.join(dir_path, filename)
#                 with open(file_path, 'r') as f:
#                     # Read values and convert to integers
#                     values = [int(line.strip()) for line in f if line.strip()]
                    
#                     # Create histogram for this file
#                     hist = defaultdict(int)
#                     for val in values:
#                         if 1 <= val <= max_key:
#                             hist[val] += 1
                    
#                     # Calculate total counts for normalization
#                     total_counts = sum(hist.values())
#                     if total_counts == 0:  # Skip empty files
#                         continue
                    
#                     # Add normalized values to our sums
#                     for key in range(1, max_key + 1):
#                         norm_val = hist.get(key, 0) / total_counts
#                         norm_hist_sums[key] += norm_val
#                         norm_hist_sums_sq[key] += norm_val ** 2
                    
#                     file_count += 1
    
#     if file_count == 0:
#         print("No files found!")
#         return None, None
    
#     # Calculate average normalized histogram and variance
#     avg_norm_hist = {}
#     variance_norm_hist = {}
    
#     for key in range(1, max_key + 1):
#         avg = norm_hist_sums[key] / file_count
#         avg_sq = norm_hist_sums_sq[key] / file_count
#         variance = avg_sq - avg**2
        
#         avg_norm_hist[key] = avg
#         variance_norm_hist[key] = variance
    
#     return avg_norm_hist, variance_norm_hist

# def save_results(avg_norm_hist, variance_norm_hist, output_dir):
#     # Save average normalized histogram
#     with open(os.path.join(output_dir, 'average_normalized_histogram.txt'), 'w') as f:
#         f.write("Key\tProbability\tVariance\n")
#         for key in sorted(avg_norm_hist.keys()):
#             f.write(f"{key}\t{avg_norm_hist[key]:.6f}\t{variance_norm_hist[key]:.6f}\n")

# if __name__ == "__main__":
#     # Set your base directory containing the numbered folders
#     base_dir = "/work/users/s/a/sackau/UNC_work/Corresponding_SFS_sample/Sample_txt_files"
#     output_dir = "/work/users/s/a/sackau/UNC_work/Corresponding_SFS_sample/Results"
    
#     # Create output directory if it doesn't exist
#     Path(output_dir).mkdir(parents=True, exist_ok=True)
    
#     # Process files and calculate statistics
#     avg_norm_hist, variance_norm_hist = process_files(base_dir)
    
#     if avg_norm_hist and variance_norm_hist:
#         # Save results
#         save_results(avg_norm_hist, variance_norm_hist, output_dir)
#         print("Processing complete. Results saved to:", output_dir)
#         print(f"Total files processed: {sum(1 for _ in Path(base_dir).rglob('*.txt'))}")