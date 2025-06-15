
import subprocess
import os
from datetime import datetime

#  Configuration
SOURCE_DIR = r"G:\New folder"
DEST_DIR = r"E:\test"

#  Automatically adjust thread count (safe limit)
MAX_THREADS = min(32, os.cpu_count() or 4)

#  Create timestamped log file
log_filename = f"robocopy_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def fast_copy_with_robocopy(src, dst):
    # Check source
    if not os.path.exists(src):
        print(f"❌ Error: Source directory '{src}' does not exist.")
        return
    if not os.path.isdir(src):
        print(f"❌ Error: Source '{src}' is not a directory.")
        return

    # Create destination if missing
    if not os.path.exists(dst):
        print(f"ℹ Destination '{dst}' does not exist. Creating it...")
        os.makedirs(dst, exist_ok=True)

    #  Robocopy command
    command = [
        "robocopy",
        src,
        dst,
        "/E",          # Include subdirectories
        "/Z",          # Restartable mode
        "/J",          # Unbuffered I/O
        "/XJ",         # Exclude junctions
        f"/MT:{MAX_THREADS}",  # Multithreading
        "/R:2",        # Retry count
        "/W:2",        # Wait between retries
        "/NFL",        # No file list
        "/NDL",        # No dir list
        "/NOOFFLOAD",  # Disable hardware copy offloading
        f"/LOG+:{log_filename}"  # Append logs
    ]

    print(f"\n Starting optimized transfer with {MAX_THREADS} threads...\n")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )

        print("📄 Robocopy Output:\n")
        print(result.stdout.strip())

        if result.stderr.strip():
            print("⚠️ Errors/Warnings:\n")
            print(result.stderr.strip())

        #  Interpret robocopy exit codes
        code = result.returncode
        if code == 0:
            print("\n✅ No files copied — source and destination are identical.")
        elif code == 1:
            print("\n✅ Files copied successfully.")
        elif code <= 3:
            print("\n⚠️ Minor issues (e.g., extra files or mismatched attributes), but copy mostly successful.")
        else:
            print(f"\n❌ Transfer failed with exit code {code}. Check log: {log_filename}")

    except subprocess.SubprocessError as e:
        print(f"\n❌ Subprocess error: {e}")
    except PermissionError:
        print(f"\n❌ Permission denied: Check access to '{src}' or '{dst}'.")
    except OSError as e:
        print(f"\n❌ OS error: {e} (maybe disk full, bad path, or hardware issue)")

if __name__ == "__main__":
    fast_copy_with_robocopy(SOURCE_DIR, DEST_DIR)
