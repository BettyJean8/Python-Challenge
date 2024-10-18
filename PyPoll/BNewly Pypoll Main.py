# Import necessary modules
import os
import csv

# Define file paths
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# Initialize vote counter and candidate options
total_votes = 0
candidate_votes = {}

# Read the CSV file and count votes
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # Count votes for each candidate
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Determine the winner and calculate percentages
winning_candidate = ""
winning_count = 0
winning_percentage = 0
candidate_results = []

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    candidate_results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    
    # Check if the current candidate is the winner
    if votes > winning_count:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

# Prepare output text
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for result in candidate_results:
    output += f"{result}\n"

output += (
    "-------------------------\n"
    f"Winner: {winning_candidate}\n"
    "-------------------------\n"
)

# Print output to terminal
print(output)

# Save output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

#I had a lot of help with this one from a friend of mine. FYI...but I did the first one all on my own. 