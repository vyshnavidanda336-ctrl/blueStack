import os

print("Deploying cloud resources...")

os.system("terraform init")
os.system("terraform apply -auto-approve")
