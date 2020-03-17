import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
df.head(10)

#rename the columns
names = {
        'Show Number':'show_number', 
        ' Round':'round',
        ' Air Date':'air_date',
        ' Category':'category',
        ' Value':'value',
        ' Question':'question',
        ' Answer':'answer'}
df = df.rename(columns=names)


# Filtering a dataset by a list of words
def filter_data(data, words):
  # Lowercases all words in the list of words as well as the questions. Returns true is all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return data.loc[data["question"].apply(filter)]

# Testing the filter function
filtered = filter_data(df, ["King", "England"])
#print(filtered["Question"])

# Adding a new column. If the value of the float column is not "None", then we cut off the first character (which is a dollar sign), and replace all commas with nothing, and then cast that value to a float. If the answer was "None", then we just enter a 0.
df["float_value"] = df["value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

# Filtering the dataset and finding the average value of those questions
filtered = filter_data(df, ["King"])
print(filtered["float_value"].mean())

# A function to find the unique answers of a set of data
def get_answer_counts(data):
    return data["answer"].value_counts()

# Testing the answer count function
print(get_answer_counts(filtered))
