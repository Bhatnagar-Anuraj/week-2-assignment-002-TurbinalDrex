"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern():

    # Grid settings
    num_rows = 5
    num_cols = 5
    spacing = 3.0

    # Create rows and Columns Of Objects
    for row in range(num_rows):
        for col in range(num_cols):

            # Position each Object in the Grid
            x_position = col * spacing
            z_position = row * spacing

            # Alternate shapes similar to checkerboard
            if (row + col) % 3 == 0:
        
                object_name = cmds.polyCube(
                    name=f"cube_{row}_{col}",
                    width=2,
                    height=2,
                    depth=2
                )[0]
            
                y_position = 1

            elif (row + col) % 3 == 1:

                object_name = cmds.polySphere(
                    name=f"sphere_{row}_{col}",
                    radius=1
                )[0]

                y_position = 1
        
            else:
            
                object_name = cmds.polyCylinder(
                    name=f"cylinder_{row}_{col}",
                    radius=1,
                    height=2
                )[0]
            
                y_position = 1
            
            # Move objects into grid like Position
            cmds.move(x_position, y_position, z_position, object_name)

# Runs the Script/Generator
generate_pattern()

cmds.viewFit(allObjects=True)
print("pattern generated SUCCESSFULLY! YAY! cool...")
