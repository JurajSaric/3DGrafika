# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 17:29:50 2023

@author: juraj
"""

import math

# Parameters
cylinder_radius = 1.0 
cylinder_height = 2.0
cylinder_segments = 16  # Complexity of the cylinder

# Generating vertices
def generate_cylinder_vertices():
    vertices = []
    for i in range(cylinder_segments): 
        theta = 2.0 * math.pi * i / cylinder_segments 
        x = cylinder_radius * math.cos(theta)    
        z = cylinder_radius * math.sin(theta)    
        vertices.append((x, 0.0, z))    
        vertices.append((x, cylinder_height, z)) 
    return vertices

# Generating normals
def generate_cylinder_normals():
    normals = []
    for i in range(cylinder_segments):
        theta = 2.0 * math.pi * i / cylinder_segments
        normal_x = math.cos(theta)
        normal_z = math.sin(theta)
        normals.append((normal_x, 0.0, normal_z))
        normals.append((normal_x, 0.0, normal_z))
    return normals

# Generating faces
def generate_cylinder_faces():
    faces = []
    for i in range(cylinder_segments):
        base_index = 2 * i + 1
        next_index = (base_index + 2) % (2 * cylinder_segments)
        faces.append((base_index, next_index, next_index + 1, base_index + 1))
        
    # Face for the bottom side
    bottom_face = list(range(1, cylinder_segments * 2 + 1, 2))
    faces.append(bottom_face)

    # Face for the top side
    top_face = list(range(2, cylinder_segments * 2 + 1, 2))
    top_face.append(2)  
    faces.append(top_face)
    
    return faces

output_file = "cylinder.obj"

vertices = generate_cylinder_vertices()
normals = generate_cylinder_normals()
faces = generate_cylinder_faces()

with open(output_file, "w") as f:
    for vertex in vertices:
        f.write(f"v {vertex[0]:.6f} {vertex[1]:.6f} {vertex[2]:.6f}\n")
    
    for normal in normals:
        f.write(f"vn {normal[0]:.4f} {normal[1]:.4f} {normal[2]:.4f}\n")
    
    for face in faces:
        f.write("f")
        for vertex_index in face:
            f.write(f" {vertex_index}")
        f.write("\n")

print("Cylinder model generated")
