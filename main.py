from data_extractor.data_extractor.extractorHelper import ExtractData
from data_extractor.storage.save_data import SaveData

def validate_file_path(file_path: str) -> str:
    """Validate if the file path is given and return it."""
    if not file_path:
        raise ValueError("FILE_PATH is not given.")
    return file_path

def extract_data(file_path: str) -> dict:
    """Extract data from the given file path."""
    helper = ExtractData(file_path)
    return helper.extractData()

def save_data_to_all_destinations(data: dict, file_path: str):
    """Save data to all specified destinations."""
    # List of saving strategies
    saving_strategies = [SaveData.saveToLocal, SaveData.saveToSQLDatabase]

    # Save using each strategy
    saver = SaveData(data, file_path)
    for strategy in saving_strategies:
        strategy(saver)

def main():
    # Get the file path
    file_path = input("Enter the file path: ")
    validated_file_path = validate_file_path(file_path)

    # Extract the data
    extracted_data = extract_data(validated_file_path)

    # Save the extracted data
    save_data_to_all_destinations(extracted_data, validated_file_path)

if __name__ == "__main__":
    main()
