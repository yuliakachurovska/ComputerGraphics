#version 330 core

// Явно вказуємо локації (0 та 1), щоб вони збігалися з glVertexAttribPointer
layout (location = 0) in vec2 aPos;
layout (location = 1) in vec2 aUV;

out vec2 vTexCoords;

uniform mat4 uTransformation;

void main() {
    vTexCoords = aUV;
    // Розгортаємо текстуру, щоб не була догори дриґом
    vTexCoords.y = 1.0 - vTexCoords.y;

    // Множимо матрицю на координати
    gl_Position = uTransformation * vec4(aPos, 0.0, 1.0);
}