import os
import argparse

def rename_files(placeholder, expedition_name):
    for dirpath, _, filenames in os.walk("."):
        for filename in filenames:
            if placeholder in filename:
                old_path = os.path.join(dirpath, filename)
                new_filename = filename.replace(placeholder, expedition_name)
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)
                print(f"✔ Renamed: {old_path} → {new_path}")

def main():
    parser = argparse.ArgumentParser(description="Rename expedition template files.")
    parser.add_argument("--name", required=True, help="Expedition name to use (e.g. DEEP_REEF_2025)")
    args = parser.parse_args()

    placeholder = "###EXPEDITIONNAME###"
    rename_files(placeholder, args.name)

if __name__ == "__main__":
    main()
