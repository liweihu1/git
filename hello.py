from pydriller import RepositoryMining

for commit in RepositoryMining('infrastructure').traverse_commits():
    print(commit.author.name)

<<<<<<< HEAD
print("Something")
=======
print("")
>>>>>>> f55fc1c... Remove text
