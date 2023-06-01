import csv, sys

def harmonizing_password_blender(file1, file2, output_file):
    shitstorm = {}

    try:
        with open(file1, 'r') as clusterfuck:
            bartender = csv.DictReader(clusterfuck)
            for shot in bartender:
                key_of_hell = (shot['url'], shot['username'])
                shitstorm[key_of_hell] = shot
    except FileNotFoundError:
        print(f"Oh sh*t! Failed to find the first file '{file1}'")
        sys.exit(1)

    try:
        with open(file2, 'r') as dumpster_fire:
            arsonist = csv.DictReader(dumpster_fire)
            for explosion in arsonist:
                fucking_key = (explosion['url'], explosion['username'])
                if fucking_key not in shitstorm:
                    shitstorm[fucking_key] = {}
                shitstorm[fucking_key].update(explosion)
    except FileNotFoundError:
        print(f"Oh sh*t! Failed to find the second file '{file2}'")
        sys.exit(1)

    chaos_fieldnames = set()
    for mayhem in shitstorm.values():
        chaos_fieldnames.update(mayhem.keys())

    with open(output_file, 'w', newline='') as pandemonium:
        hell_writer = csv.DictWriter(pandemonium, fieldnames=sorted(chaos_fieldnames))
        hell_writer.writeheader()
        hell_writer.writerows(shitstorm.values())

    print(f"Combined the f*cking passwords from '{file1}' and '{file2}', merged those badass fields, and saved that sh*t to '{output_file}'.")

# Here's a mind-blowing example of how to use this insane sh*t. Brace yourselves!
harmonizing_password_blender('passwords1.csv', 'passwords2.csv', 'combined_passwords.csv')
