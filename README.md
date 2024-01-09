
# <span style="font-size:1.5em;">File Compression and Decompression Tool</span>
This Python script provides a simple and efficient tool for compressing and decompressing files using the LZMA (Lempel-Ziv-Markov chain-Algorithm) compression algorithm. LZMA is known for its high compression ratio and is widely used for archive formats.

## Features
- **Compression:**
  Easily compress files using the LZMA algorithm, reducing their size while preserving data integrity.

- **Decompression:**
  Decompress LZMA-compressed files, restoring them to their original state.

## How to Use
1. **Run the script.**
2. **Choose the action:**
   - Enter 'c' to compress a file.
   - Enter 'd' to decompress a file.

3. **Follow the prompts based on your chosen action:**
   - For compression, provide the exact path to the file you want to compress.
   - For decompression, enter the original file name (including the file extension) and the exact path to the compressed file.

4. **Monitor the progress:**
   - A progress bar will display during both compression and decompression processes.

5. **Upon successful completion:**
   - For compression, the original file is replaced with the compressed file.
   - For decompression, the compressed file is replaced with the decompressed file.

-----------------------------------------------
Requirements:
  Python 3.x
  tqdm library (for progress bar visualization)
-----------------------------------------------
Usage Tips:
  Ensure that you provide the exact file path, including the file extension, to avoid errors.
  Be cautious while compressing large files, as the process may take some time depending on the file size and system resources.
  Feel free to contribute, report issues, or suggest improvements.


How it works:
https://github.com/galacticoder/comp_enc/assets/155845471/2099f67b-8c7f-4166-922d-f2575c78edb6

The compression time was 2 minutes and 8.58 secs for a file size of 1.56 GB
![Screenshot 2024-01-09 155615](https://github.com/galacticoder/comp_enc/assets/155845471/b0794c4f-7eb0-40c6-8d09-180f5e96e9a8)

When compressed the file size comes out to 
![compressed](https://github.com/galacticoder/comp_enc/assets/155845471/da652231-cc7e-41f4-b9bf-d305c381cf91)

Now for the decryption process we use the script and choose the action 'd':

https://github.com/galacticoder/comp_enc/assets/155845471/211f776e-dee2-45af-ad60-5bdbf4a1018a
The video was not altered during the decryption process it is that fast during decryption and the content of the file returns as shown in the video

That is how this script works thank you for using it.



