from PIL import Image

# Path to the PNG file
png_file = "ico/ico.png"

# Path to save the ICO file
ico_file = "ico/ico.ico"

# Convert PNG to ICO
# You can specify the sizes for the ICO file (e.g., [16, 32, 48, 64])
#icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]

# Open the PNG image
img = Image.open(png_file)

# Save as ICO
#img.save(ico_file, format='ICO', sizes=icon_sizes)
img.save(ico_file, format='ICO')

print(f"Converted {png_file} to {ico_file}")