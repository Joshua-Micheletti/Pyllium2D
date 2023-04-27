#version 330 core
  in vec3 fragment_color;
  out vec4 final_color;

  void main() {
      final_color = vec4(fragment_color, 1);
  }
