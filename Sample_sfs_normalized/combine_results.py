import numpy as np
import os
import glob
from tqdm import tqdm

def compute_true_variance(output_dir, max_key=20):
    """Compute variance across ALL individual files"""
    # First pass: count total files and initialize arrays
    total_files = 0
    for f in glob.glob(os.path.join(output_dir, "histograms_*.npy")):
        total_files += np.load(f).shape[0]
    
    # Pre-allocate memory
    all_means = np.zeros(max_key)
    all_squares = np.zeros(max_key)
    
    # Second pass: compute running sums
    for f in tqdm(glob.glob(os.path.join(output_dir, "histograms_*.npy")),
                  desc="Processing files"):
        data = np.load(f)  # shape: (files_in_folder, max_key)
        all_means += data.sum(axis=0)
        all_squares += (data**2).sum(axis=0)
    
    # Final calculations
    global_mean = all_means / total_files
    global_var = (all_squares/total_files) - (global_mean**2)
    
    return global_mean, global_var, total_files

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--max_key", type=int, default=20)
    args = parser.parse_args()
    
    print("Computing true variance across all files...")
    means, variances, total_files = compute_true_variance(args.output_dir, args.max_key)
    print(f"Processed {total_files:,} files")
    
    # Save results
    with open(os.path.join(args.output_dir, "TRUE_global_stats.txt"), 'w') as f:
        f.write("Key\tMean\tVariance\tStdDev\n")
        for key in range(args.max_key):
            std = np.sqrt(variances[key])
            f.write(f"{key+1}\t{means[key]:.6f}\t{variances[key]:.6f}\t{std:.6f}\n")
    
    print("Variance now properly computed across all individual files")
# import numpy as np
# import os
# import glob
# from tqdm import tqdm

# def load_all_histograms(output_dir):
#     """Load all histogram files with progress tracking"""
#     files = sorted(glob.glob(os.path.join(output_dir, "histograms_*.npy")))
#     all_histograms = []
#     total_files = 0
    
#     for f in tqdm(files, desc="Loading histograms"):
#         arr = np.load(f)
#         all_histograms.append(arr)
#         total_files += arr.shape[0]
    
#     return np.concatenate(all_histograms), total_files

# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--output_dir", required=True)
#     parser.add_argument("--max_key", type=int, default=20)
#     args = parser.parse_args()
    
#     print("Combining results from all folders...")
#     histograms, total_files = load_all_histograms(args.output_dir)
#     print(f"Loaded {total_files:,} files total")
    
#     means = histograms.mean(axis=0)
#     variances = histograms.var(axis=0, ddof=0)
    
#     # Save results
#     output_path = os.path.join(args.output_dir, "global_stats.txt")
#     with open(output_path, 'w') as f:
#         f.write("Key\tMean\tVariance\n")
#         for key in range(args.max_key):
#             f.write(f"{key+1}\t{means[key]:.6f}\t{variances[key]:.6f}\n")
    
#     print(f"Results saved to {output_path}")

# import numpy as np
# from collections import defaultdict
# import os
# import glob

# def combine_results(output_dir):
#     result_files = glob.glob(os.path.join(output_dir, "results_*.npz"))
    
#     total_sums = defaultdict(float)
#     total_sums_sq = defaultdict(float)
#     total_files = 0
    
#     for f in result_files:
#         data = np.load(f, allow_pickle=True)
#         sums = data['sums'].item()
#         sums_sq = data['sums_sq'].item()
#         count = data['count'].item()
        
#         for key in sums:
#             total_sums[key] += sums[key]
#             total_sums_sq[key] += sums_sq[key]
#         total_files += count
    
#     # Calculate averages and variances
#     avg_norm_hist = {k: total_sums[k]/total_files for k in total_sums}
#     variance_norm_hist = {k: (total_sums_sq[k]/total_files) - (avg_norm_hist[k]**2) for k in total_sums}
    
#     # Save final results
#     with open(os.path.join(output_dir, 'final_normalized_histogram.txt'), 'w') as f:
#         f.write("Key\tProbability\tVariance\n")
#         for key in sorted(avg_norm_hist.keys()):
#             f.write(f"{key}\t{avg_norm_hist[key]:.6f}\t{variance_norm_hist[key]:.6f}\n")
    
#     print(f"Processed {len(result_files)} folders with {total_files} total files")

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 2:
#         print("Usage: python combine_results.py <output_dir>")
#         sys.exit(1)
    
#     combine_results(sys.argv[1])