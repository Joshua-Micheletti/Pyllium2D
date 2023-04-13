#version 150 core
  in vec4 vertex_colors;
  out vec4 final_color;

  void main() {
      final_color = vertex_colors;
  }
