import ID3

Data = []
Labels = set()

Columns = [
    'buying',
    'maint',
    'doors',
    'persons',
    'lug_boot',
    'safety',
    'label'
]

Attributes = {
    'buying':['vhigh', 'high', 'med', 'low'],
    'maint':['vhigh', 'high', 'med', 'low'],
    'doors':['2', '3', '4', '5more'],
    'persons':['2', '4', 'more'],
    'lug_boot':['small', 'med', 'big'],
    'safety':['low', 'med', 'high']
}

# read file into Data
with open('./car/train.csv', 'r') as train_data:
    for line in train_data:
        row = line.strip().split(',')
        Data.append(row)

for row in Data:
    label = row[len(row) - 1]
    if label not in Data:
        Labels.add(label)

print(ID3.proportions(Data, Labels))
print(ID3.majority_error(Data, Labels))
print(ID3.gini_index(Data, Labels))
print(ID3.entropy(Data, Labels))
