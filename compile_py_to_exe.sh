#!/bin/bash

# Change to the directory containing your Python script
# cd "/path/to/your/script"

# Use PyInstaller to compile the Python script to an executable
pyinstaller --onefile --icon=ico/ico.ico --noconsole Main_UI.py

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "PyInstaller encountered an error."
    exit 1
fi

# Define paths for the source and destination
SOURCE_DIR="dist"
DESTINATION_DIR="."
NEW_EXE_NAME="Main_UI_Rev00"
DESKTOP_SHORTCUT_NAME="Main_UI_Shortcut.desktop"

# Move and rename the executable
echo "Moving and renaming executable..."
mv "${SOURCE_DIR}/Main_UI" "${DESTINATION_DIR}/${NEW_EXE_NAME}"

if [ $? -ne 0 ]; then
    echo "Failed to move or rename the executable."
    exit 1
fi

TARGET_PATH="${DESTINATION_DIR}/${NEW_EXE_NAME}"

# Create a shortcut on the desktop
echo "Creating shortcut on the desktop..."
DESKTOP_PATH="${HOME}/Desktop/${DESKTOP_SHORTCUT_NAME}"
cat <<EOF >"${DESKTOP_PATH}"
[Desktop Entry]
Type=Application
Name=${NEW_EXE_NAME}
Exec=${TARGET_PATH}
Path=${DESTINATION_DIR}
Icon=${DESTINATION_DIR}/ico/ico.ico
Terminal=false
EOF

chmod +x "${DESKTOP_PATH}"

# Delete the build directory and other temporary files
echo "Cleaning up build files..."
rm -rf build dist Main_UI.spec

# Optional: Keep the terminal open
exec "$SHELL"
