import os
import shutil
from git import Repo
from scripts.get_repo_name import get_repo_name_from_url

def single_repository():
    repo_url = input("Enter the URL of the repository to clone: ")

    path_to_clone = input("Enter the path where you want to clone the repository: ")

    repo_name = get_repo_name_from_url(repo_url)
    full_path_to_clone = os.path.join(path_to_clone, repo_name)

    if os.path.exists(full_path_to_clone):
        print(f"Deleting the existing directory in {full_path_to_clone}...")
        try:
            shutil.rmtree(full_path_to_clone)
            print("Directory deleted.")
        except Exception as e:
            print(f"The directory could not be deleted: {e}")

    os.makedirs(path_to_clone, exist_ok=True)

    try:
        print(f"Cloning the repository in {full_path_to_clone}...")
        Repo.clone_from(repo_url, full_path_to_clone)
        print("Repository successfully cloned.")
    except Exception as e:
        print(f"An error occurred while cloning the repository: {e}")