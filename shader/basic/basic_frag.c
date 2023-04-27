#version 330 core

in vec3 fragment_color;
in vec2 fragment_tex_coord;

out vec4 final_color;

uniform sampler2D texture_image;

void main() {
    final_color = vec4(fragment_color, 1) * texture(texture_image, fragment_tex_coord);
}
