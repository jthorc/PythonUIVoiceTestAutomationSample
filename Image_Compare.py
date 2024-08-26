import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

class ImageComparer:
    def __init__(self, image_path1, image_path2):
        """
        :param image_path1: The file path of the first image.
        :param image_path2: The file path of the second image.
        """
        self.image1 = cv2.imread(image_path1)
        self.image2 = cv2.imread(image_path2)

    def compare_and_highlight(self, output_path='output.png'):
        """
        Compares two images, highlights the differences, and saves the result.
        :param output_path: The file path to save the output image with differences highlighted.
        :return: Similarity score.
        """
        # Convert the images to grayscale
        gray_image1 = cv2.cvtColor(self.image1, cv2.COLOR_BGR2GRAY)
        gray_image2 = cv2.cvtColor(self.image2, cv2.COLOR_BGR2GRAY)

        # Resize images to the same size for comparison
        if gray_image1.shape != gray_image2.shape:
            gray_image2 = cv2.resize(gray_image2, (gray_image1.shape[1], gray_image1.shape[0]))

        # Compute the Structural Similarity Index (SSI) between the images
        score, diff = ssim(gray_image1, gray_image2, full=True)
        diff = (diff * 255).astype("uint8")

        # Threshold the difference image to highlight regions of difference
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # Find contours of the different regions
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around the differences on the original images
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(self.image1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(self.image2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Combine the two images side by side for output
        comparison = np.hstack((self.image1, self.image2))

        # Save the output image
        cv2.imwrite(output_path, comparison)

        return score

# Example usage
if __name__ == "__main__":
    current_dir = os.getcwd()
    base_img_full_path = os.path.join(current_dir, "base_image","200727195059.JPEG")
    target_img_full_path = os.path.join(current_dir, "target_image","201904110209.JPEG")
    output_img_full_path = os.path.join(current_dir, "imgc_result", "Output_image.png")
    # Replace 'image1.png' and 'image2.png' with paths to your images
    comparer = ImageComparer(base_img_full_path, target_img_full_path)

    # Compare the images, highlight differences, and save the result
    similarity_score = comparer.compare_and_highlight(output_img_full_path)
    print(f"Similarity score: {similarity_score:.4f}")

    if similarity_score > 0.9:
        print("The images are very similar.")
    else:
        print("The images are different. See 'comparison_output.png' for highlighted differences.")