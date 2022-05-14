from os import walk
from nightfall import Nightfall

# reads API key from NIGHTFALL_API_KEY environment variable
nightfall = Nightfall()

# update this path to point to your folder/directory/backup to scan
rootpath = os.getenv('SCAN_DIRECTORY_PATH')

# create a policy in the nightfall console, paste the UUID in NIGHTFALL_POLICY_UUID environment variable
policy_uuid = os.getenv('NIGHTFALL_POLICY_UUID')

# crawl the directory to scan all files
count = 0
for (dirpath, dirnames, filenames) in walk(rootpath):
	for filename in filenames:
		filepath = f"{dirpath}/{filename}"
		count += 1

		try:
			print(f"Scanning {filepath}")
			# scan with Nightfall
			scan_id, message = nightfall.scan_file(
				filepath, 
				policy_uuid=policy_uuid,
				request_metadata=filepath)
			print(scan_id, message)
		except Exception as err:
			print(err)
print(f"Completed. Scanned {count} file(s)")