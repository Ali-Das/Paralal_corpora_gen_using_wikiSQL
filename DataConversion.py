from utilities.DataConversionUtil import DataConversionUtil

# Create a tokenized dataset for the train, test and validation datasets
# Enables model to run faster during actual training since all data is already 
# preprocessed
data_converter = DataConversionUtil()
#print("Data conversion for training.........")
#data_converter.build_tokenized_dataset("train")
#print("Data conversion for development.........")
#data_converter.build_tokenized_dataset("dev")
print("Data conversion for testing.........")
data_converter.build_tokenized_dataset("test")
