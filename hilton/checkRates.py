#! /usr/bin/env python3

# This script compares HLT rates from two text files (reference and test) and generates a report of differences.
# It reads the rates, calculates percentage differences, and outputs a report in both original and sorted order.
# Meant to assist in validating HLT rate changes in Fast-Track Validation
# Last updated: 2026-03 by Luca Ferragina

import re

# Input configuration
ref_filename = "ref_HLT_rates.txt"
test_filename = "test_HLT_rates.txt"

# Output configuration
output_filename = "rates_comparison_report.txt"
sorted_output_filename = "rates_comparison_report_sorted.txt"


def parse_hlt_file(filepath):
    """Parses the HLT rate file and returns a dictionary of {path: rate}."""
    data = {}
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    with open(filepath, "r") as f:
        for line in f:
            clean_line = ansi_escape.sub("", line).strip()
            clean_line = clean_line.replace("[0;0m", "").replace("[0;0;32m", "")
            parts = clean_line.split()

            # 4 columns: HLT path name, L1 seeds, Prescale counts, HLT path counts
            if len(parts) >= 4 and parts[-1].isdigit():
                path_name = parts[0]
                try:
                    data[path_name] = float(parts[-1])
                except ValueError:
                    continue
    return data


def build_report_content(changes, total_paths):
    """Constructs the text report with data and final summary."""
    lines = []
    lines.append(f"{'HLT Path Name':<65} | {'Ref Rate':<10} | {'Test Rate':<10} | {'Diff (%)':<10}")
    lines.append("-" * 105)

    if not changes:
        lines.append("No rate differences found.")
    else:
        for c in changes:
            lines.append(f"{c['path']:<65} | {int(c['ref']):<10} | {int(c['test']):<10} | {c['diff_pct']:<10}")

    lines.append("\n" + "="*45 + " SUMMARY REPORT " + "="*44)
    lines.append(f"Total HLT Paths Processed:      {total_paths}")
    lines.append(f"Paths with Rate Differences:    {len(changes)}")
    lines.append("=" * 105 + "\n")

    return lines


def compare_rates():
    ref_data = parse_hlt_file(ref_filename)
    test_data = parse_hlt_file(test_filename)

    rate_changes = []
    total_paths = 0

    # Process all paths found in the reference file
    for path, ref_rate in ref_data.items():
        if path in test_data:
            total_paths += 1
            test_rate = test_data[path]

            if ref_rate != test_rate:
                if ref_rate == 0:
                    diff_val = float('inf')
                    diff_pct = "+INF"
                else:
                    diff_val = ((test_rate - ref_rate) / ref_rate) * 100
                    diff_pct = f"{diff_val:+.2f}%"

                rate_changes.append({
                    'path': path,
                    'ref': ref_rate,
                    'test': test_rate,
                    'diff_val': diff_val,
                    'diff_pct': diff_pct
                })

    # Original file order
    standard_content = build_report_content(rate_changes, total_paths)
    with open(output_filename, "w") as f:
        f.write("\n".join(standard_content))

    # Sorted results
    sorted_changes = sorted(rate_changes, key=lambda x: x['diff_val'], reverse=True)
    sorted_content = build_report_content(sorted_changes, total_paths)
    with open(sorted_output_filename, "w") as f:
        f.write("\n".join(sorted_content))

    # Print standard report
    print("\n".join(standard_content))
    print("Two reports generated:")
    print(f"    - Standard Order: {output_filename}")
    print(f"    - Sorted by Diff: {sorted_output_filename}")


if __name__ == "__main__":
    try:
        compare_rates()
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure input files exist in the current directory.")
