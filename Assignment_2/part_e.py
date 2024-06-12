# Part e

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='Path to the file')
    parser.add_argument('--intvalue', type=int, help='An integer value')
    parser.add_argument('--floatvalue', type=float, help='A float value')
    args = parser.parse_args()
    print(f"File Path: {args.path}, Integer Value: {args.intvalue}, Float Value: {args.floatvalue}")

if __name__ == "__main__":
    main()
