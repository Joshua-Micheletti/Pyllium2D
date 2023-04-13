#version 150 core
  in vec2 position;
  in vec4 colors;
  out vec4 vertex_colors;

  void main() {
      gl_Position = vec4(position, 0.0, 1.0);
      vertex_colors = colors;
  }
