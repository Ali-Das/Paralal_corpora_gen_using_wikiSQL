from utilities.ParallelCorporaGenUtil import ParallelCorporaGenUtil

# Create a tokenized dataset for the train, test and validation datasets
# Enables model to run faster during actual training since all data is already 
# preprocessed
parallel_corpora_generator = ParallelCorporaGenUtil()
#print("building parallel corpora for training.........")
#parallel_corpora_generator.build_parallel_corpora_from_json("train")
#print("building parallel corpora for Development Data Set.........")
#parallel_corpora_generator.build_parallel_corpora_from_json("dev")
print("building parallel corpora for testing.........")
parallel_corpora_generator.build_parallel_corpora_from_json("test")