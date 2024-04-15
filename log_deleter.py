import os
import glob
import asyncio

async def log_remover(directory: str, prefix_of_filename: str, file_size: int):
    """
    Inputs:
    directory - Where the file lies.
    prefix_of_filename - the beginning of the filename.
    file_size - limit as to how big the file can be before removing.

    Output:
    Will detect most recent txt file with that prefix and will
    delete it if its size is greater than the file_size input
    """
    # Adding an * to the name, we add a wildcard character, indicating to glob that we are looking for a pattern
    prefix_of_filename = prefix_of_filename + '*'
    
    # Find all files that begin with the prefix
    files = glob.glob(os.path.join(directory, prefix_of_filename))
    
    # Sort all files that begin with the prefix in descending order
    files.sort(key=os.path.getmtime, reverse=True)

    if os.path.getsize(files[0]) > file_size:
        most_recent_file = files[0]
        # Remove most recent file in a separate thread to avoid blocking the event loop
        await asyncio.to_thread(os.remove, most_recent_file)
        print(f"The most recent file '{most_recent_file}' has been removed.")

# An example of how to use it:

async def main():
    # My existing trading code
    log_remover('.', 'markov_chain_trader_log#', 2000)
    # Rest of code

if __name__ == '__main__':
    asyncio.run(main())