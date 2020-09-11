from pydriller import RepositoryMining

for commit in RepositoryMining('../git').traverse_commits():
    print(commit.author.name)
    print(commit.branches)
    print("Hello")