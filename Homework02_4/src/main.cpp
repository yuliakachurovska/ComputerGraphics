#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

const char* vertexShaderSource = R"(
    #version 330 core
    layout (location = 0) in vec2 aPos;
    layout (location = 1) in vec2 aTexCoord;
    out vec2 TexCoord;
    uniform mat4 u_transform;
    void main() {
        gl_Position = u_transform * vec4(aPos, 0.0, 1.0);
        TexCoord = aTexCoord;
    }
)";

const char* fragmentShaderSource = R"(
    #version 330 core
    out vec4 FragColor;
    in vec2 TexCoord;
    uniform sampler2D u_texture;
    void main() {
        FragColor = texture(u_texture, TexCoord);
    }
)";

int main() {
    glfwInit();
    GLFWwindow* window = glfwCreateWindow(800, 800, "Rectangle Controller", NULL, NULL);
    glfwMakeContextCurrent(window);
    gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);

    GLuint vShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vShader);
    GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fShader);
    GLuint program = glCreateProgram();
    glAttachShader(program, vShader);
    glAttachShader(program, fShader);
    glLinkProgram(program);

    float vertices[] = {
        -0.3f, -0.15f,  0.0f, 0.0f,
         0.3f, -0.15f,  1.0f, 0.0f,
         0.3f,  0.15f,  1.0f, 1.0f,
        -0.3f,  0.15f,  0.0f, 1.0f
    };
    unsigned int indices[] = { 0, 1, 2, 0, 2, 3 };

    GLuint VAO, VBO, EBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));
    glEnableVertexAttribArray(1);

    GLuint texture;
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
    unsigned char pixels[] = { 255,0,0,255, 0,255,0,255, 0,0,255,255, 255,255,0,255 };
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 2, 2, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    float posX = 0.0f, posY = 0.0f, angle = 0.0f;
    float lastTime = (float)glfwGetTime();

    while (!glfwWindowShouldClose(window)) {
        float currentTime = (float)glfwGetTime();
        float deltaTime = currentTime - lastTime;
        lastTime = currentTime;

        glfwPollEvents();
        glClear(GL_COLOR_BUFFER_BIT);

        float speed = 1.0f;
        if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS)  posX -= speed * deltaTime;
        if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS) posX += speed * deltaTime;
        if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS)    posY += speed * deltaTime;
        if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS)  posY -= speed * deltaTime;

        double mx, my;
        glfwGetCursorPos(window, &mx, &my);
        float mouseX = (float)(mx / 400.0) - 1.0f;
        float mouseY = 1.0f - (float)(my / 400.0);

        if (mouseX >= posX - 0.3f && mouseX <= posX + 0.3f &&
            mouseY >= posY - 0.15f && mouseY <= posY + 0.15f) {
            angle += 100.0f * deltaTime;
        }

        glm::mat4 model = glm::mat4(1.0f);
        model = glm::translate(model, glm::vec3(posX, posY, 0.0f));
        model = glm::rotate(model, glm::radians(angle), glm::vec3(0.0f, 0.0f, 1.0f));

        glUseProgram(program);
        glUniformMatrix4fv(glGetUniformLocation(program, "u_transform"), 1, GL_FALSE, glm::value_ptr(model));

        glBindVertexArray(VAO);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        glfwSwapBuffers(window);
    }
    glfwTerminate();
    return 0;
}