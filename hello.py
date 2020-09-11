from pydriller import RepositoryMining

for commit in RepositoryMining('infrastructure').traverse_commits():
    print(commit.author.name)

print("")
