import os


def find_s4p_files(directory, prefix_to_ignore):
    s4p_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".s4p") and not file.startswith(prefix_to_ignore):
                s4p_files.append(os.path.join(root, file))
    return s4p_files


def write_sample_extraction_txt(s4p_files, cal_file, output_file):
    with open(output_file, "w") as f:
        f.write("! Sample extraction\n")
        for s4p_file in s4p_files:
            f.write("# isd \n")
            f.write("test_coupon " + cal_file + "\n")
            f.write("dut_fixture " + s4p_file + "\n")
            f.write("linear_2x 3\n")
            f.write("port_order 2\n")
            f.write("smooth_dut 2\n")
            f.write("passive 1\n\n")


def main():
    # Prompt user for directory path
    directory = input("Enter the directory path: ")
    # Prompt user for the prefix to ignore
    prefix_to_ignore = input("Enter the prefix to ignore for .s4p files: ")
    # Find all .s4p files in the directory and its subdirectories
    s4p_files = find_s4p_files(directory, prefix_to_ignore)
    if not s4p_files:
        print("No .s4p files found in the directory.")
        return

    # Prompt user for location of the 2xcal file
    cal_file = input("Enter the location of the 2xcal file (e.g., C:\\path\\to\\file.s4p): ")
    if not os.path.isfile(cal_file):
        print("2xcal file not found.")
        return

    # Prompt user for the location to save the output file
    output_dir = input("Enter the directory where you want to save the output file (e.g., C:\\Scripts\\): ")
    output_filename = input("Enter the name of the output file (e.g., mel-1100): ")
    output_file = os.path.join(output_dir, output_filename + ".txt")

    # Write sample extraction text file
    write_sample_extraction_txt(s4p_files, cal_file, output_file)
    print("Sample extraction text file created successfully.")


if __name__ == "__main__":
    main()
