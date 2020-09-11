from pydriller import RepositoryMining, GitRepository

for commit in RepositoryMining('../git').traverse_commits():
    print(commit.author.name)
    print(GitRepository('../git').get_head().hash)
