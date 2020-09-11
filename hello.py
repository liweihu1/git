from pydriller import RepositoryMining, GitRepository

for commit in RepositoryMining('../git').traverse_commits():
    print(commit.author.name)
    print(commit.in_main_branch)
