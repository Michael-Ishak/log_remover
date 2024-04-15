import os
import glob
import asyncio
import logging

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
    while True: # Continuously check for files
        prefix_of_filename = prefix_of_filename + '*'
        files = glob.glob(os.path.join(directory, prefix_of_filename))
        files.sort(key=os.path.getmtime, reverse=True)

        for file in files:
            if os.path.getsize(file) > file_size:
                await asyncio.to_thread(os.remove, file)
                logging.info(f"The file '{file}' has been removed.")

        await asyncio.sleep(60) # Wait for 60 seconds before checking again to reduce average CPU usage on that thread

async def main():
    # Other trading code
    # Start the log remover in the background
    asyncio.create_task(log_remover('.', 'test1', 3000))
    # Rest of the code

if __name__ == '__main__':
    asyncio.run(main())