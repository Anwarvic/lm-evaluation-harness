def doc_to_choice(doc):
    return [option[0] for option in doc["choices"]]

def doc_to_target(doc):
    options = doc_to_choice(doc)
    return options.index(doc["answer"])

import datasets

def load_and_merge(**kwargs):
    #kwargs
    print("Loading and merging accounting mcq dataset with kwargs:", kwargs)
    # Load the dataset
    ds = datasets.load_dataset(kwargs['dataset_path'])
    # Return a dict with a 'test' key containing the merged data
    return {
        "test": datasets.concatenate_datasets([ds["validation"], ds["test"]])
    }
