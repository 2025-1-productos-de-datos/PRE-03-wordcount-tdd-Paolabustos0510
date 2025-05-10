import argparse


def parse_args(args=None):

    parser = argparse.ArgumentParser(description="Count words in files.")

    parser.add_argument(
        "input_folder", help="Path to the input folder containing files to process"
    )
    parser.add_argument("output_folder", help="Path to the output folder for results")

    parsed_args = parser.parse_args(args)

    return parsed_args.input_folder, parsed_args.output_folder
