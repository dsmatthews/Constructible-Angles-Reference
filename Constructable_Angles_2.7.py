import math
from collections import defaultdict
from typing import Dict, List, Tuple, Set
import os
import html

# Define base constructible angles (in degrees)
BASE_ANGLES = [
    90, 72, 60, 54, 45, 36, 30, 27, 22.5, 20, 18, 15,
    12, 10, 9, 7.5, 6, 5, 3.75, 3, 1.5
]

# Configuration constants
MIN_ANGLE = 0.1
MAX_ANGLE = 90
TOL = 0.0001
MAX_DEPTH = 6
MAX_STEPS = 10
OUTPUT_FILE = "constructible_angles.html"

def generate_constructible_angles() -> Dict[float, Tuple[int, List[str]]]:
    """Generate constructible angles using bisection, addition, and subtraction."""
    constructible: Dict[float, Tuple[int, List[str]]] = {}
    by_depth: Dict[int, Set[float]] = defaultdict(set)
    
    for angle in BASE_ANGLES:
        angle = round(angle, 4)
        constructible[angle] = (0, [f"Base angle: {angle}°"])
        by_depth[0].add(angle)
    
    for depth in range(1, MAX_DEPTH + 1):
        for angle in by_depth[depth - 1]:
            half = round(angle / 2, 4)
            if MIN_ANGLE <= half < MAX_ANGLE and half not in constructible:
                steps = constructible[angle][1] + [f"Bisect {angle}° → {half}°"]
                if len(steps) <= MAX_STEPS:
                    constructible[half] = (depth, steps)
                    by_depth[depth].add(half)
    
    iteration = 0
    while iteration < 5:
        new_angles = False
        existing = list(constructible.items())
        for i in range(len(existing)):
            a1, (d1, s1) = existing[i]
            for j in range(i, len(existing)):
                a2, (d2, s2) = existing[j]
                total = round(a1 + a2, 4)
                if (MIN_ANGLE <= total < MAX_ANGLE and total not in constructible):
                    steps = s1 + s2 + [f"Add {a1}° + {a2}° → {total}°"]
                    if len(steps) <= MAX_STEPS:
                        constructible[total] = (max(d1, d2) + 1, steps)
                        new_angles = True
                diff = round(abs(a1 - a2), 4)
                if (MIN_ANGLE <= diff < MAX_ANGLE and diff not in constructible):
                    steps = s1 + s2 + [f"Subtract {a1}° - {a2}° → {diff}°"]
                    if len(steps) <= MAX_STEPS:
                        constructible[diff] = (max(d1, d2) + 1, steps)
                        new_angles = True
        if not new_angles:
            break
        iteration += 1
    
    return constructible

def generate_html(constructible: Dict[float, Tuple[int, List[str]]]) -> None:
    """Generate an HTML file with a table of constructible angles and their steps."""
    grouped = defaultdict(list)
    for angle in sorted(constructible.keys()):
        int_part = int(angle)
        grouped[int_part].append((angle, constructible[angle][1]))
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Constructible Angles Reference</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    .angle-table { display: none; }
    .angle-table.active { display: table; }
    .steps { display: none; white-space: pre-line; }
    .steps.active { display: block; }
  </style>
</head>
<body class="bg-gray-100 font-sans p-6">
  <div class="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-md">
    <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">Constructible Angles Reference (0°–90°)</h1>
    
    <!-- Instructions for Base Angles -->
    <div class="mb-6">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">How to Construct Base Angles</h2>
      <p class="text-gray-600 mb-2">The following base angles are used to derive all other angles. Here's how to construct them using a compass and straightedge:</p>
      <ul class="list-disc list-inside text-gray-600">
        <li><strong>90°:</strong> Draw a straight line. At a point on the line, use a compass to draw a perpendicular by creating two equal arcs above and below the line, then connect the intersection points.</li>
        <li><strong>60°:</strong> Draw a line segment AB. With center A and radius AB, draw an arc intersecting the line at B. With center B and the same radius, draw another arc to intersect the first arc at C. Draw line AC to form a 60° angle at A.</li>
        <li><strong>72°:</strong> Construct a regular pentagon (e.g., using a circle and dividing it into five equal parts with a compass). Each interior angle of the pentagon is 108°, so the angle between a side and the radius to a vertex is 72°.</li>
        <li><strong>54°:</strong> Construct a regular pentagon (as for 72°). The angle between two adjacent vertices and the center is 72°. Bisect this angle to get 36°, then subtract from 90° to get 54°.</li>
        <li><strong>45°:</strong> Construct a 90° angle, then bisect it using a compass by marking equal arcs between the angle's rays.</li>
        <li><strong>36°:</strong> Construct a regular pentagon (as for 72°). The angle between two adjacent vertices and the center is 72°. Bisect this angle to get 36°.</li>
        <li><strong>30°:</strong> Construct a 60° angle, then bisect it using a compass.</li>
        <li><strong>27°:</strong> Construct a 54° angle (via a pentagon), then bisect it to get 27°.</li>
        <li><strong>22.5°:</strong> Construct a 45° angle, then bisect it to get 22.5°.</li>
        <li><strong>20°:</strong> Construct a regular pentagon, which gives a 36° angle at the center. Bisect 36° to get 18°, then add 18° + 2° (from other constructions like subtracting 10° from 12°) to get 20°.</li>
        <li><strong>18°:</strong> Construct a 36° angle (via a pentagon), then bisect it to get 18°.</li>
        <li><strong>15°:</strong> Construct a 60° angle, then bisect it to get 30°, and bisect again to get 15°.</li>
        <li><strong>12°:</strong> Construct a 60° angle, divide it by 5 (e.g., by constructing a regular pentagon inscribed in a circle and adjusting), or subtract 18° - 6° to get 12°.</li>
        <li><strong>10°:</strong> Construct a 20° angle (via pentagon constructions), then bisect it to get 10°.</li>
        <li><strong>9°:</strong> Construct an 18° angle (via a pentagon), then bisect it to get 9°.</li>
        <li><strong>7.5°:</strong> Construct a 15° angle, then bisect it to get 7.5°.</li>
        <li><strong>6°:</strong> Construct a 12° angle, then bisect it to get 6°.</li>
        <li><strong>5°:</strong> Construct a 10° angle, then bisect it to get 5°.</li>
        <li><strong>3.75°:</strong> Construct a 7.5° angle, then bisect it to get 3.75°.</li>
        <li><strong>3°:</strong> Construct a 6° angle, then bisect it to get 3°.</li>
        <li><strong>1.5°:</strong> Construct a 3° angle, then bisect it to get 1.5°.</li>
      </ul>
    </div>

    <div class="mb-6">
      <label for="angleSearch" class="block text-lg font-medium text-gray-700 mb-2">Search for an Angle:</label>
      <input type="number" id="angleSearch" step="0.0001" min="0" max="90" placeholder="Enter angle (e.g., 1.5)" 
             class="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
      <div id="searchResult" class="mt-2 text-gray-700"></div>
    </div>

    <div class="mb-6">
      <label for="rangeSelect" class="block text-lg font-medium text-gray-700 mb-2">Select Angle Range:</label>
      <select id="rangeSelect" class="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
        <option value="all">All Angles (0°–90°)</option>
"""
    for i in range(91):
        html_content += f'        <option value="{i}">{i}°–{i+1}°</option>\n'
    
    html_content += """      </select>
    </div>

    <div id="tables">
"""
    
    for k in sorted(grouped):
        active_class = ' active' if k == 0 else ''
        html_content += f'      <table class="angle-table{active_class} w-full border-collapse border border-gray-300 mb-4" data-range="{k}">\n'
        html_content += """        <thead>
          <tr class="bg-blue-500 text-white">
            <th class="p-2 border border-gray-300">Angle (degrees)</th>
            <th class="p-2 border border-gray-300">Construction Steps</th>
          </tr>
        </thead>
        <tbody>
"""
        for angle, steps in grouped[k]:
            steps_str = "\n".join(steps)
            steps_html = html.escape(steps_str).replace('\n', '<br>')
            html_content += f'          <tr><td class="p-2 border border-gray-300">{angle:.4f}°</td><td class="p-2 border border-gray-300"><button class="text-blue-600 hover:underline" onclick="toggleSteps(this)">Show Steps</button><div class="steps">{steps_html}</div></td></tr>\n'
        html_content += """        </tbody>
      </table>
"""
    
    html_content += """    </div>
  </div>

  <script>
    function toggleSteps(button) {
      const steps = button.nextElementSibling;
      steps.classList.toggle('active');
      button.textContent = steps.classList.contains('active') ? 'Hide Steps' : 'Show Steps';
    }

    document.getElementById('rangeSelect').addEventListener('change', function() {
      const selected = this.value;
      const tables = document.querySelectorAll('.angle-table');
      tables.forEach(table => {
        table.classList.remove('active');
        if (selected === 'all' || table.getAttribute('data-range') === selected) {
          table.classList.add('active');
        }
      });
    });

    document.getElementById('angleSearch').addEventListener('input', function() {
      const searchValue = parseFloat(this.value);
      const resultDiv = document.getElementById('searchResult');
      if (isNaN(searchValue) || searchValue < 0 || searchValue > 90) {
        resultDiv.textContent = 'Please enter a valid angle between 0° and 90°';
        return;
      }
      const tables = document.querySelectorAll('.angle-table');
      let closestAngle = null;
      let closestDiff = Infinity;
      let closestSteps = '';
      tables.forEach(table => {
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach(row => {
          const angleText = row.querySelector('td').textContent;
          const angle = parseFloat(angleText);
          const diff = Math.abs(angle - searchValue);
          if (diff < closestDiff) {
            closestDiff = diff;
            closestAngle = angle;
            closestSteps = row.querySelector('.steps').innerHTML;
          }
        });
      });
      if (closestDiff < 0.0001) {
        resultDiv.innerHTML = `Found: ${closestAngle.toFixed(4)}°<br>Steps: ${closestSteps}`;
      } else {
        resultDiv.innerHTML = `${searchValue}° not found. Closest angle: ${closestAngle.toFixed(4)}° (difference: ${closestDiff.toFixed(4)}°)<br>Steps: ${closestSteps}`;
      }
    });
  </script>
</body>
</html>
"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML file generated: {os.path.abspath(OUTPUT_FILE)}")

def main():
    """Main function to generate and output constructible angles to HTML."""
    constructible = generate_constructible_angles()
    generate_html(constructible)

if __name__ == "__main__":
    main()
    
