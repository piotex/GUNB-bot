from dataclasses import dataclass, field

@dataclass
class DataModel:
    url_start: str = "https://wyszukiwarka.gunb.gov.pl/"
    user_input_data_file: str = r"C:\devops_sandbox\git\GUNB-bot\user-input.txt"

    screenshot_location: str = r"C:\Users\pkubo\Pictures\Screenshots"
    data_files_location: str = r"C:\devops_sandbox\git\GUNB-bot"




