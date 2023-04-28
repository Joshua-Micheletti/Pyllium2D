#version 330 core

layout (location=0) in vec3 vertex_position;
layout (location=1) in vec3 vertex_color;
layout (location=2) in vec2 texture_uv;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec3 fragment_color;
out vec2 fragment_tex_coord;

void main() {
    gl_Position = (projection * view * model) * vec4(vertex_position, 1.0);
    fragment_color = vertex_color;
    fragment_tex_coord = texture_uv;
}
