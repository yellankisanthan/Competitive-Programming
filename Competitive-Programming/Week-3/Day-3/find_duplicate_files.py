import os
import hashlib

def find_duplicate_files(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]
    duplicates = []
    while len(stack):
        current_path = stack.pop()
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)
        else:
            file_hash = sample_hash_file(current_path)
            current_last_edited_time = os.path.getmtime(current_path)
            if file_hash in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_hash]
                if current_last_edited_time > existing_last_edited_time:
                    duplicates.append((current_path, existing_path))
                else:
                    duplicates.append((existing_path, current_path))
                    files_seen_already[file_hash] = (current_last_edited_time, current_path)
            else:
                files_seen_already[file_hash] = (current_last_edited_time, current_path)

    return duplicates


def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())
        else:
            num_bytes_between_samples = (
                (total_bytes - num_bytes_to_read_per_sample * 3) / 2
            )
            for offset_multiplier in xrange(3):
                start_of_sample = (
                    offset_multiplier
                    * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                )
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()
    
def my_function(arg):
    return 'running with %s' % arg
print (my_function('test input'))