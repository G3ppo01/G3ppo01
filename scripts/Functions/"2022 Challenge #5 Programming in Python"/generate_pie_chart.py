def generate_pie_chart(data, output_file="statuscode.png"):
    """
    Generates a pie chart of the status code occurrences and saves it as an image file.

    :param data: Dictionary of status codes and their occurrences
    :param output_file: Path to save the pie chart image
    """
    try:
        # Extract labels and sizes for the pie chart
        labels = list(data.keys())
        sizes = list(data.values())
        
        # Generate the pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title("Status Code Distribution")
        
        # Save the pie chart as an image file
        plt.savefig(output_file)
        print(f"Pie chart has been saved to {output_file}")
    except Exception as e:
        # Handle any other exception that may occur during pie chart generation
        print(f"An error occurred while generating the pie chart: {e}")
        sys.exit(1)
