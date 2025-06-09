from face_analysis import analyze_face

if __name__ == "__main__":
    # Path to the input image
    input_image = "img1.jpg"
    # Path to the folder containing reference images (named as 'person_name.jpg')
    reference_folder = "references"

    # Analyze the image
    result = analyze_face(input_image, reference_folder)
    
    # Print the results
    print("Analysis Result:")
    print(f"Name: {result['name']}")
    print(f"Age: {result['age']}")
    print(f"Gender: {result['gender']}")
    print(f"Emotion: {result['emotion']}")
    