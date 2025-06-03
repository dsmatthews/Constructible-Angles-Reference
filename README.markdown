# Constructible Angles Reference

## Overview

The Constructible Angles Reference is a Python-based project that generates a list of angles (between 0° and 90°) that can be constructed using a compass and straightedge. It outputs an interactive HTML page where users can explore these angles, view their construction steps, and search for the closest constructible angle to a given value. This tool is designed for educational purposes, helping users understand geometric constructions and the principles of constructible angles.

## Features

- **Generate Constructible Angles**: Computes angles that can be constructed by starting with base angles (e.g., 90°, 60°, 45°) and applying operations like bisection, addition, and subtraction.
- **Interactive HTML Output**: Produces an HTML page with:
  - A table of constructible angles, grouped by degree ranges.
  - A search bar to find the closest constructible angle to a user-specified value.
  - Detailed construction steps for each angle, including how to achieve base angles.
  - A dropdown to filter angles by range (e.g., 0°–1°, 1°–2°).
- **Pedagogical Instructions**: Includes a section explaining how to construct base angles using a compass and straightedge, making it accessible for beginners.
- **Responsive Design**: Uses Tailwind CSS for a clean, user-friendly interface.

## Usage

### Prerequisites
- Python 3.x installed on your system.
- No additional libraries are required as the script uses Python's standard library.

### Running the Script
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/dsmatthews/Constructible-Angles-Reference.git
   cd constructible-angles
   ```
2. Run the Python script to generate the HTML file:
   ```bash
   python constructible_angles.py
   ```
3. Open the generated `constructible_angles.html` file in a web browser:
   - The script will print the absolute path to the file upon completion.
   - Alternatively, navigate to the file in your file explorer and double-click to open it.

### Interacting with the HTML Page
- **Search for an Angle**: Enter an angle (e.g., 3.14°) in the search bar to find the closest constructible angle and its construction steps.
- **Filter by Range**: Use the dropdown menu to display angles within a specific degree range.
- **View Construction Steps**: Click "Show Steps" next to any angle to see the sequence of geometric operations (e.g., bisection, addition) to construct it.
- **Learn Base Angles**: Refer to the "How to Construct Base Angles" section for instructions on creating the foundational angles using a compass and straightedge.

## Files

- `constructible_angles.py`: The main Python script that generates constructible angles and outputs the HTML file.
- `constructible_angles.html`: The generated HTML file (created after running the script) containing the interactive angle reference.

## Project Details

- **Base Angles**: The project starts with a set of base angles (90°, 72°, 60°, etc.) that are known to be constructible using classical geometric methods.
- **Operations**:
  - Bisection: Divides an angle into two equal parts.
  - Addition/Subtraction: Combines or subtracts angles to form new ones.
- **Constraints**:
  - Angles are computed between 0.1° and 90°.
  - Construction steps are limited to a maximum depth to ensure practicality.
- **Output Format**: The HTML page uses Tailwind CSS for styling and includes JavaScript for interactivity (e.g., search and filtering).

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them with a descriptive message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```
4. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request on the main repository, describing your changes in detail.

### Potential Improvements
- Add visualizations or diagrams for angle constructions.
- Expand the range of base angles or operations.
- Optimize the angle generation algorithm for performance.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using Python's standard library for angle computations and HTML generation.
- Styled with [Tailwind CSS](https://tailwindcss.com/) for a responsive design.
- Inspired by classical geometry and the study of constructible numbers.

---

*Generated on June 03, 2025*