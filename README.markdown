# Fast File Transfer with Robocopy

Welcome to the **Fast File Transfer with Robocopy** script, a Python-based tool that leverages Windows' `robocopy` command for optimized file copying. This script automates efficient directory transfers with multithreading, restartable mode, and detailed logging, making it ideal for backing up data, syncing folders, or migrating large datasets. Designed for Windows users, it simplifies complex `robocopy` configurations while providing clear feedback and error handling.

## Features

- **Optimized File Copying**: Uses `robocopy` with multithreading (up to 32 threads, adjusted based on CPU count) for fast transfers.
- **Robust Configuration**:
  - Copies entire directories, including subdirectories and empty folders (`/E`).
  - Supports restartable mode (`/Z`) for interrupted transfers.
  - Uses unbuffered I/O (`/J`) for performance.
  - Excludes junction points (`/XJ`) to avoid loops.
  - Limits retries (`/R:2`) and wait time (`/W:2`) for reliability.
- **Automatic Destination Creation**: Creates the destination directory if it doesn't exist.
- **Timestamped Logging**: Generates detailed logs in a file (e.g., `robocopy_log_20250615_182030.txt`) for auditing.
- **Error Handling**:
  - Validates source directory existence and type.
  - Handles permission errors, disk issues, and subprocess failures.
  - Interprets `robocopy` exit codes to provide clear success/failure feedback.
- **Minimal Output**: Suppresses verbose file and directory lists (`/NFL`, `/NDL`) for cleaner console output.


## Prerequisites

- **Operating System**: Windows (tested on Windows 10/11). `robocopy` is pre-installed on Windows.
- **Python 3.x**: Ensure Python is installed. Download from python.org.
- **Permissions**: Read access to the source directory and write access to the destination directory.
- **Disk Space**: Sufficient space in the destination for copied files.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/fast-files-transfer.git
   cd fast-files-transfer
   ```

2. **Ensure Python is Installed**: Verify Python is available by running:

   ```bash
   python --version
   ```

   No additional libraries are required, as the script uses standard Python modules (`subprocess`, `os`, `datetime`).

3. **Run the Script**:

   ```bash
   python fast-files-transfer.py
   ```

   Ensure the `fast-files-transfer.py` file (rename your script accordingly) is in the project directory.

## Usage

1. **Configure Source and Destination**: Edit the script to set the `SOURCE_DIR` and `DEST_DIR` variables to your desired paths. Example:

   ```python
   SOURCE_DIR = r"C:\Data\Projects"
   DEST_DIR = r"D:\Backups\Projects"
   ```

   Use raw strings (`r"..."`) or double backslashes (`\\`) for Windows paths.

2. **Run the Script**: Execute the script in a terminal:

   ```bash
   python robocopy_transfer.py
   ```

3. **Monitor Output**:

   - The script checks if the source exists and creates the destination if missing.
   - It displays the number of threads used (based on CPU count, max 32).
   - Console output includes `robocopy` results, errors/warnings, and exit code interpretation:
     - `0`: No changes (source and destination identical).
     - `1`: Files copied successfully.
     - `2–3`: Minor issues (e.g., extra files).
     - `4+`: Transfer failed.
   - A log file (e.g., `robocopy_log_20250615_182030.txt`) is created in the script's directory with detailed transfer information.

4. **Review Logs**: Open the generated log file to audit the transfer, including copied files, skipped items, and errors.

## Project Structure

- `robocopy_transfer.py`: Main script containing the file transfer logic using `robocopy`.
- `robocopy_log_*.txt`: Generated log files with timestamped transfer details.
- `demo.gif` (optional): Add a demo GIF or screenshot to showcase the script.

## How It Works

- **Configuration**: Defines source and destination paths, with a dynamic thread count based on CPU cores (capped at 32).
- **Validation**: Checks if the source directory exists and is valid; creates the destination if needed.
- **Robocopy Command**: Constructs a `robocopy` command with optimized flags:
  - `/E`: Copies subdirectories, including empty ones.
  - `/Z`: Enables restartable mode for reliability.
  - `/J`: Uses unbuffered I/O for speed.
  - `/XJ`: Excludes junction points to prevent loops.
  - `/MT`: Enables multithreading for parallel copying.
  - `/NFL`, `/NDL`: Reduces console clutter.
  - `/LOG+`: Appends detailed logs to a timestamped file.
- **Execution**: Runs `robocopy` via `subprocess.run`, capturing output and errors.
- **Feedback**: Interprets exit codes and displays user-friendly messages for success, warnings, or failures.
- **Error Handling**: Catches permission issues, disk errors, and subprocess failures, providing actionable feedback.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes (e.g., add progress tracking, support for other copy tools, or cross-platform compatibility).
4. Commit your changes (`git commit -m "Add your feature"`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

Please ensure your code follows PEP 8 style guidelines and includes comments for clarity.

## Future Enhancements

- Add a GUI (e.g., with Tkinter) for selecting source/destination directories.
- Support progress tracking with a progress bar or file count.
- Enable scheduling for automated backups.
- Add support for other copy tools (e.g., `rsync` for Linux/macOS) for cross-platform use.
- Include file verification (e.g., checksums) to ensure data integrity.
- Allow customization of `robocopy` flags via command-line arguments.

## Known Issues

- **Windows Only**: Relies on `robocopy`, which is Windows-specific. Cross-platform alternatives (e.g., `shutil` or `rsync`) could be added.
- **Log File Growth**: Continuous use may create large log files. Consider log rotation or size limits.
- **Thread Count**: High thread counts (`/MT`) may strain system resources on low-end hardware. Adjust `MAX_THREADS` if needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspired by the need for fast and reliable file transfers on Windows.
- Thanks to the Python community and Microsoft for `robocopy`'s powerful features.
- Special thanks to the open-source community for sharing knowledge and tools.

Feel free to star ⭐ this repository if you find it useful, and share your feedback or ideas in the issues section!

*Created by Muhammad Usman*